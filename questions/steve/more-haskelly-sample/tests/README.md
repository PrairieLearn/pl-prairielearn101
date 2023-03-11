# Question

Copied from `tests-template` folder.

You may especially want to edit:

[`question.cabal`](question.cabal)
: Cabal setup file. Add dependencies you may need here.

[`test/Spec.hs`](test/Spec.hs)
: The tests for the student submission.

[`src/Lib.hs`](src/Lib.hs)
: Sample solution, for use in testing. Overwritten by student code in grading.

[`src/Lib-header.hs`](src/Lib-header.hs)
: Header fragment, inserted above student code to create the new `src/Lib.hs` file during grading.

You can also create `.mustache` versions of any of these, which will be rendered with the `data`
source into non-mustache versions. E.g., if you have `src/Lib-header.hs.mustache`, it will be 
rendered before grading into `src/Lib-header.hs`. (The .mustache extension can go anywhere
in the list of extensions at the end of the filename.)
