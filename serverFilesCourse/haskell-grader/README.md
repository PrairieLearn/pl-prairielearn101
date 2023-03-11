# Haskell Grading System

Based on Mattox Beckman's grading system. (Which is to say directly copied from and perhaps edited in the future.)

Key entry point is `run-qc-lib.sh` which in turn uses `grader-qc.py` and `mustache-process.sh`. All the other files in this folder are strictly for reference and presently unused!

# The Autograder

PrairieLearn makes it easy for your autograder to live in your course
under the `serverFilesCourse`, which gives you some customizability
within the constraints of the Docker image.

## Overview of Files

Mattox says they mostly use the `run-qc-lib.sh` script. That configures
folders with information from the student submission and a copy of the
`grader-qc.py` file. It then concatenates the provided header
(`src/Lib-header.hs`) and the student\'s code (`src/Lib.hs`) into a
single new `src/Lib.hs` file (via a temporary file arbitrarily named
`foo.hs`). Finally, it runs the student code *as non-root* (the `ag`
user) via the `grader-qc.py` script in a directory set up with the
appropriate information/ownership (`AG_DIR`, `/grade/run/` as currently
configured).

`grader-qc.py` runs `stack test` (which also builds) on the student
code. It handles errors such as testing errors (reported via Mattox\'s
`=G=` syntax, and which don\'t count as a failed run in PrairieLearn
terms, i.e., this counts as a submission), other errors in the call to
`stack` (which count as a failure to run the student code, i.e., do not
count against students), timeout expiration (again, counts as a failure
to run the student code), and unspecified exceptions.

(It actually seems to run `stack test` a second time if it was
successful the first for something related to handling large output,
maybe? The second time can presumably be faster (since the `build` stage
will be complete). Maybe the testing frameworks also do some caching?)

I've modified `run-qc-lib.sh` to also invoke `mustache-process.sh` in 
order to enable mustache template expansion for creating test file
variants (presumably to track the question variants). It finds files
named `<anything>.mustache`, uses the same data as for `question.html`,
and puts the expanded version in the corresponding filename `<anything>`.
(The `<anything>` part can be... anything... non-empty.)

## Test Result DSL

Test results can report information to the testing script via strings
(per the current `grader-qc.py` file).

Here\'s the simple version:

-   Have each test appear after some group designator. The group
    designator looks like `=G= Here is my group name`. Groups cannot be
    nested.
-   Standard property tests look like `=P= Here is my test name (n
     points): OK` for passing tests or either `=P= Test name (n points):
     FAIL` or `=P= Test name (n points): Failed` for failing ones.
    Property tests are \"normal\" tests, graded individually. `n` should
    be a non-negative integer.
-   Required tests look the same as property tests except using `=R=`
    rather than `=P=`. However, any failure on a required test zeroes
    out the whole student score. On passes, required tests act just like
    standard property tests.
-   TODO: "Error" tests look the same as property tests except using `=E=`.
    If any error test fails, no more test data will be processed, and
    the "gradable" flag to PrairieLearn will be set to false, meaning
    the run won't count against students.

A property test\'s name is its group name, followed by `" / "` (i.e., a
slash surrounded by spaces), followed by its test name. A required
test\'s name is similar except its test name has \"All Or Nothing: \"
prepended.

The script dumps a json version of a dictionary containing the keys:

-   A bunch of largely test-non-specific keys:
    -   \"succeeded\": a Boolean indicating if PrairieLearn should count
        the test as having run (i.e., \"charge\" the student one
        submission); this will be \"True\" if we get to test result
        parsing; **TODO:** I have changed this to \"gradable\" per
        <https://prairielearn.readthedocs.io/en/latest/externalGrading/#grading-results>.
        Does that seem right?
    -   \"message\": an informative message (absent for successful test
        runs, including anytime we get to test parsing)
    -   \"output\": compilation error message, if compilation failed
        (absent anytime we get to test parsing)
-   \"score\": a float in the range \[0, 1\], the score on the question.
    This is 0 if any required tests failed or if the total points
    available were 0. Otherwise, it\'s the total points in passing tests
    (of either type) divided by the total points in all tests.
-   \"tests\": a list of the test results. Each one is a dictionary
    containing:
    -   \"name\": see above
    -   \"max~points~\": the points value from above
    -   \"points\": the points value from above for passing tests; 0 for
        failing tests
    -   \"message\": present for failing tests only: the text between
        the line after the test was specified (e.g., after a line like
        `=P=
         ... (n points): FAIL` line) and the next group or test
        specification or the end of the file.

So, e.g., a line like `=G= curry` followed later by `=R= vindaloo (13
points): FAIL` would produce a (required) test failure named \"curry /
All Or Nothing: vindaloo\" (with a maximum point value of 13). (The
presence of a failed required test would also zero out the student\'s
score, regardless of other scoring.) If the next line of interest were
`=P= favor (1 points): that was OK!`, that would produce a test success
named \"curry / favor\" with both earned and maximum points of 1.
(Failed property tests and successful required tests would both also be
recorded. Nothing is recorded *separately* for a group line. It only
impacts subsequent test lines.)

(TODO: Out of date paragraph; does not discuss `=E=`: 
In more detail: `=R=` or `=P=` can be preceeded by any number of spaces.
(As of now, `=G=` cannot have initial whitespace, which matches what
`testGroup` and `testProperty` do with test names?) The `=*=` designator
must have a space after it, and the `(n points):` block must have a
space both before and after it. Those spaces are not part of the
group/test name. The `OK`, `FAIL`, or `Failed` text can appear anywhere
up to the end of the line after the `(n points):` block (and its
subsequent space), interspersed with any other text. The `points`, `OK`,
and `FAIL` or `Failed` strings must be exactly as written (e.g., no \"(1
point):\" or \"ok\" allowed). (As written now, an \"OK\" overrides a
\"FAIL\"/\"Failed\" if both occured on the same line.) Point numbers can
only be digits and are in base 10, regardless of leading 0s.)

***All* tests should be in a group.** Tests not in a group *are* in a
group with an empty name, and there is no way to end a group except to
start another. (That also implies that groups cannot be nested.)
Indeed, in the case that a test produces an error, the framework relies
on finding an `=G=` code before the failure occurs to determine that
testing got started.

For reference, here\'s the most relevant source code (TODO: out of date: `=E=`):

``` python
propPass = re.match(" *=[RP]= (.*) \(([0-9]+) points\): .*OK.*",line)
propFail = re.match(" *=P= (.*) \(([0-9]+) points\): .*(FAIL|Failed).*",line)
reqFail = re.match(" *=R= (.*) \(([0-9]+) points\): .*(FAIL|Failed).*",line)
groupStart = re.match("=G= (.*)",line)
wereDone = re.match("( *Properties *Total|[0-9]+ out of [0-9]+ tests)",line)
```

Note that `propPass` covers both property and required tests.

## Setting Up a Question

**Caution:** If this is your first question using your Docker image in
your instance of PrairieLearn, you may need to explicitly sync the
Docker image in the PL interface. Check out the sync menu once you have
installed your question to look for warnings to that effect.

Use [stack](https://haskellstack.org/) to set up a question
appropriately. You\'ll want roughly the following file structure for
your question, beyond the usual for any PrairieLearn question and
[external
grading](https://prairielearn.readthedocs.io/en/latest/externalGrading/):

+ `question.html`: Set this up so that students will submit a file named `Lib.hs`.
+ `info.json`: Configuration for external grading. You'll want something like the
   following:
   
   ``` javascript
   "gradingMethod": "External",
   "externalGradingOptions": {
     "enabled": true,
     "image": "cswolf/haskell-prairielearn",
     "enableNetworking": false,
     "serverFilesCourse": [
       "haskell-grader/"
     ],
     "entrypoint": "/grade/serverFilesCourse/haskell-grader/run-qc-lib.sh"
   }
   ```
   
   You will likely change the image name. You may want to enable
   networking, depending on your needs. This assumes you have the
   Haskell grading files under your PrairieLearn course\'s
   `serverFilesCourse` folder in `haskell-grader`.
   
   You may want to add a timeout (inside the `externalGradingOptions`
   block; it defaults to 30 seconds). You may also want to set
   `singleVariant` to true.
+ `tests`: Folder with test contents.
  
  + Standard stack files: stack information needed to prepare and run your tests, but with
    special notes below.
    
    (You'll probably want `.stack-work` in your `.gitignore` file.)
  + `stack.yaml`:   Ensure this refers to the **same LTS version** as in the Docker
    image, to avoid having to redownload/recache ghc and packages
    (which will blow the timeout on students' tests!)
  + `src/Lib-header.hs`:   A header to prepend to the student's submitted work. For
    example, something like:
     
    ``` haskell
    module Lib where
    import Prelude hiding (map, foldl, foldr, zip, zipWith)
    ```
     
    will set up the module for students and explicitly import the
    `Prelude`, hiding certain functions so they're not usable by
    students. (Be sure to give instructions to students about what
    they're not allowed to use if you do this!)
     
    This file plus the student\'s submission will become a new
    `src/Lib.hs` file before testing begins.
     
  + `src/Lib.hs`:   Put your own reference solution here to run tests against during
    development. (It will be replaced when testing student code as
    described in the previous point.)
    
  + `test/Spec.hs`:   Put the tests to run against student code here or in whatever
    other location you configure `stack test` to expect.
    
**Additionally**, much like `question.html` goes through Mustache
template expansion using the `data` JSON object, any file anywhere
within the `tests` subdirectory tree named `*.mustache` will go through
Mustache template expansion with the same data. The result is stored
with the same filename/path except without the `.mustache` extension.
This can be handy for testing question variants.
