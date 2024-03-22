assert __name__ == '__main__', "lib/test cannot be imported as a module."

import requests

from abc import ABC
from collections import defaultdict
from itertools import cycle
from json import JSONDecoder, dumps
from unittest import TestCase, main
from unittest.mock import patch, mock_open

from lib.consts import DEFAULT_BLANK_PATTERN, BLANK_SUBSTITUTE
from lib.tokens import Lexer, lex
from generate_fpp import parse_fpp_regions

def flatten_into_region_map(tokens: Lexer) -> dict[str, list[str]]:
    col = defaultdict(list)
    for t in tokens.data:
        col[t.region].append(t.text)
    return { k: ''.join(v) for k, v in col.items() }

def make_region(name: str, body: str) -> str:
    return f'## {name} ##\n{body}\n## {name} ##'

def make_import(path: str, name: str) -> str:
    return f'## import {path} as {name} ##'

def make_metadata_region(**metadata):
    return make_region('metadata', dumps(metadata))

def lines(*lines): return '\n'.join(lines)
def n_lines(n: int, body: str): return '\n'.join(n * [body])

class TestLexABC(TestCase, ABC):
    def assertLexesTo(self, src: str, *, no_region='', **output):
        lexed = lex(src)
        rmap = flatten_into_region_map(lexed)
        output.setdefault('', no_region)
        self.assertDictEqual(output, rmap, msg=f'\n\nSource:\n{src}')

    def assertMetadataIs(self, src: str, **output):
        lexed = lex(src)
        self.assertDictEqual(output, lexed.metadata, msg=f'\n\nSource:\n{src}')

    def assertNoRegions(self, src: str):
        self.assertLexesTo(src, no_region=src)

    def assertSyntaxError(self, src: str):
        with self.assertRaises(SyntaxError):
            _ = lex(src)


class TestLex(TestLexABC):
    def test_empty_src(self):
        """ An empty source should return `{ '': '' }` """
        self.assertLexesTo('')

    def test_simple_region_delims(self):
        """ Single char names and ws only contents """
        txt = '## r ##\n## r ##'
        self.assertLexesTo(txt, r='')
        txt += '\n'
        self.assertLexesTo(txt, r='')
        txt += '\n'
        self.assertLexesTo(txt, no_region='\n', r='')

        # these seem iffy!
        txt = '## r ##\n\n## r ##'
        self.assertLexesTo(txt, r='')
        txt = '## r ##\n\n\n## r ##'
        self.assertLexesTo(txt, r='\n')

    def test_dirty_region_delims(self):
        """ Whitespace before and text after region delim tags is ignored """
        txt = """
           \t ## dirty ## hi there! ##
        all good
        ## dirty #### random text $$%$%"""
        self.assertLexesTo(txt, dirty='        all good')

    def test_unbalanced_region_delims(self):
        """ Checks unbalanced delims throw SyntaxErrors """
        with self.subTest('unbalanced w/valid start'):
            txt = "## not_okay ##\n"
            self.assertSyntaxError(txt)
            # with contents/no-region text
            txt = "outer text\n\n## not_okay ##\n\ninner text...\n"
            self.assertSyntaxError(txt)
            # dirty start
            txt = f"\t\t## region ### hi"
            self.assertSyntaxError(txt)

        with self.subTest('integration'):
            # after good regions
            txt = f"a \n{make_region('r0', 'hi there')} \nb \n## bad ##\n inner"
            self.assertSyntaxError(txt)

    def test_start_region_without_closing_previous(self):
        """ Region delimiters appearing in regions throw SyntaxErrors """
        # balanced
        txt = make_region('okay', "text\n " + make_region("not okay", "bad") + "\n more text")
        self.assertSyntaxError(txt)
        # unbalanced, after good
        txt = f"a \n{make_region('r0', 'hi there')} \n{make_region('r1', '## bad ##')}"
        self.assertSyntaxError(txt)

    def test_import_region_without_closing_previous(self):
        """ Import regions appearing in regions throw SyntaxErrors """
        i_r = make_import("file.txt", "bad")
        txt = make_region('okay', f"text\n{i_r}\n more text")
        self.assertSyntaxError(txt)
        # after good
        txt = f"a \n{make_region('r0', 'hi there')} \n{make_region('r1', i_r)}"
        self.assertSyntaxError(txt)

    def test_almost_region_delim_false_positives(self):
        """ Test things that almost qualify as region delims """
        with self.subTest('regions must be named'):
            self.assertNoRegions('####')
            self.assertNoRegions('#####')

        with self.subTest('regions must be named non whitespace'):
            self.assertNoRegions('## ##')
            self.assertNoRegions('## \t ##')
            self.assertNoRegions('## \t   ##')

        with self.subTest('regions begin with exactly ## and end with at least ##'):
            self.assertNoRegions('### region ##')
            # self.assertNoRegions('## region ###') << this is a valid (but dirty ended) delim!
            self.assertNoRegions('# region ##')
            self.assertNoRegions('### region ###')
            self.assertNoRegions('#### region ####')

    def test_region_concat(self):
        """ Regions with the same name should concatenate in the order they appear """
        rbody = 'body 0\nbody1\nbody2\n\n'
        r = make_region('r', rbody) + '\n'
        self.assertLexesTo(3 * r, r = n_lines(3, rbody))
        sbody = 'body a\nbodyb\nbodyc\n\n'
        s = make_region('s', sbody) + '\n'
        self.assertLexesTo(r + s + r + s + r, s = n_lines(2, sbody), r = n_lines(3, rbody))

        txt = '\n'.join((make_region('r', '1'), make_region('r', '2'), make_region('r', '3')))
        self.assertLexesTo(txt, r=lines('1', '2', '3'))

    def test_empty_metadata(self):
        """ Empty input or metadata regions should both yield {} metadata """
        self.assertMetadataIs('')
        self.assertMetadataIs(make_region('metadata', ''))

    def test_falsy_metadata(self):
        """ Falsy objects in metadata is interpreted as {} """
        self.assertMetadataIs('')
        self.assertMetadataIs(make_region('metadata', '0'))
        self.assertMetadataIs(make_region('metadata', '[]'))
        self.assertMetadataIs(make_region('metadata', '{}'))
        self.assertMetadataIs(make_region('metadata', '""'))
        self.assertMetadataIs(make_region('metadata', 'null'))
        # stitch together many
        txt = make_region('metadata', '') + '\n' + make_region('metadata', '{}') + \
            '\n' + make_region('metadata', '')
        self.assertMetadataIs(txt)

    def test_import_concat(self):
        """ Check that import regions concat to themselves like regular regions """
        file_data = 'imported file:\n3\n2\n1'
        with patch('builtins.open', mock_open(read_data=file_data)):
            i_r = make_import('file.txt', 'imported')
            txt = i_r + '\n' + make_region('r', 'data') + ('\n' + i_r) * 2
            self.assertLexesTo(txt, r='data', imported=3*file_data)

    def test_multiple_imports(self):
        """ Importing multiple sources is possible """
        file_data = 'imported file:\n3\n2\n1'
        with patch('builtins.open', mock_open(read_data=file_data)):
            txt = make_region('r', 'data') + '\n' + \
                make_import('f1.txt', 'i1') + '\n' + \
                    make_import('f2.txt', 'i2')
            self.assertLexesTo(txt, i1=file_data, i2=file_data, r='data')

    def test_valid_import(self):
        """ Valid imports read file contents """
        path = 'README.md'
        with open(path) as rdme:
            lines = ''.join(rdme.readlines())
        txt = make_import(path, 'readme')
        self.assertLexesTo(txt, readme=lines)

    def test_valid_import_content(self):
        """ Valid imports read file contents and do not edit other regions """
        file_data = 'imported file:\n3\n2\n1'
        with patch('builtins.open', mock_open(read_data=file_data)):
            i_r = make_import('file.txt', 'imported')
            self.assertLexesTo(i_r, imported=file_data)

            txt = make_region('r', 'data') + '\n' + i_r
            self.assertLexesTo(txt, imported=file_data, r='data')

    def test_import_bad_path(self):
        """ Bad import paths result in FileNotFoundErrors or OSErrors """
        with self.subTest('absolute dir'):
            path = '~/Documents'
            with self.assertRaises(OSError):
                _ = lex(make_import(path, 'imported'))

        with self.subTest('absolute non-existent file'):
            path = '~/badsasdfasdfasdfasdfsadfas.txt'
            with self.assertRaises(FileNotFoundError):
                _ = lex(make_import(path, 'imported'))

        with self.subTest('relative dir'):
            path = './lib'
            with self.assertRaises(OSError):
                _ = lex(make_import(path, 'imported'))

        with self.subTest('relative non-existent file'):
            path = './dont-readme.md'
            with self.assertRaises(FileNotFoundError):
                _ = lex(make_import(path, 'imported'))

        with self.subTest('unix-style relative non-existent file'):
            path = 'badsasdfasdfasdfasdfsadfas.txt'
            with self.assertRaises(FileNotFoundError):
                _ = lex(make_import(path, 'imported'))

    def test_import_json_as_metadata(self):
        """ Reading a metadata json with imports is the same as with decoders """
        with open('./info.json') as f:
            ls = ''.join(f.readlines())
        txt = make_import('info.json', 'metadata') # a fixture of PL elements
        json = JSONDecoder().decode(ls)
        self.assertMetadataIs(txt, **json)


class TestRandomLex(TestLexABC):
    @staticmethod
    def get_bacon_ispum(paragraphs):
        res = requests.get(
            url = 'https://baconipsum.com/api/',
            params = {
                'type': 'meat-and-filler',
                'paras': paragraphs,
            }
        )
        assert res.status_code == 200, f"Bad result: {res}"
        return JSONDecoder().decode(res.text)

    @classmethod
    def setUpClass(cls):
        cls.test_strings = cls.get_bacon_ispum(10)

    def test_no_regions(self):
        """ A random text file with no regions of any kind. """
        self.assertNoRegions(self.test_strings[0])

    def test_empty_regions(self):
        """ A randomly named set of empty regions """
        rnames = self.test_strings[0].split()[:3]
        txt = '\n'.join(make_region(name, '') for name in rnames)
        output = { name: '' for name in rnames }
        self.assertLexesTo(txt, **output)

    def test_random_regions(self):
        """ A randomly filled and named set of regions """
        rnames = self.test_strings[0].split()[:3]
        rbodies = self.test_strings[1:4]
        txt = '\n'.join(make_region(name, body) for name, body in zip(rnames, rbodies))
        output = defaultdict(str)
        for name, body in zip(rnames, rbodies):
            output[name] += body
        output[''] += ''
        self.assertLexesTo(txt, **output)

    def test_mixed_regions_and_no_region(self):
        """ A randomly filled and named set of regions, interspersed with random text """
        str_iter = iter(self.test_strings)
        rnames = cycle(next(str_iter).split()[:3])
        txt = []
        output = defaultdict(list)
        unmatched = ''
        for name, body, no_r in zip(rnames, str_iter, str_iter):
            txt.append(make_region(name, body))
            output[name].append(body)

            txt.append(no_r)
            unmatched += no_r

        output = { name: lines(*body) for name, body in output.items() }
        output[''] = unmatched
        self.maxDiff = 5000
        self.assertLexesTo(lines(*txt), **output)

def scrub_blank(txt: str): return txt.replace('?', '')
def sub_blank(txt: str): return DEFAULT_BLANK_PATTERN.sub(lambda _: BLANK_SUBSTITUTE, txt)

class TestParseFPP(TestCase):
    def assertParsesTo(self, src: str, *, answer_code='', prompt_code='', metadata=None, **output):
        lexed = lex(src)
        parsed = parse_fpp_regions(lexed)
        output.setdefault('metadata', metadata or {})
        output.setdefault('answer_code', answer_code)
        output.setdefault('prompt_code', prompt_code)
        self.assertDictEqual(output, parsed, msg=f'\n\nSource:\n{src}')

    def assertSyntaxError(self, src: str):
        lexed = lex(src)
        with self.assertRaises(SyntaxError):
            _ = parse_fpp_regions(lexed)

    def test_empty_src(self):
        """ Empty source results in {} metadata and blank answer_code and prompt_code """
        self.assertParsesTo('') # defaults are all blank...

    def test_no_comments_in_strings(self):
        """ Comments are not captured in str literals """
        for c in ["'", '"', '`', '"""', "'''"]:
            with self.subTest(f'no comments within {c}s'):
                txt = 's = " line# 7 "'
                self.assertParsesTo(
                    txt,
                    answer_code=txt,
                    prompt_code=txt,
                )

    def test_docstring_question_text(self):
        """ Leading docstrings are appended to the question_text region """
        q_html = '<question> text </question>'
        ans = 'answer = 3'
        self.assertParsesTo(
            lines(f"'''{q_html}'''", '', ans),
            answer_code=ans,
            prompt_code=ans,
            question_text=q_html
        )
        t = '<i>hello</i>'
        r = make_region('question_text', t)
        self.assertParsesTo(
            lines(f"'''{q_html}'''", '', ans, r),
            answer_code=ans,
            prompt_code=ans,
            question_text=lines(q_html, t)
        )
        self.assertParsesTo(
            lines(r, f"'''{q_html}'''", '', ans, r),
            answer_code=ans,
            prompt_code=ans,
            question_text=lines(t, q_html, t)
        )

    def test_regular_comment_splitting(self):
        """ Regular comments should only appear in prompt_code not answer_code """
        txt = lines('# c0', 'a = 4  # c1', 'a += 2', '\t\t# c1', '')
        self.assertParsesTo(
            txt,
            answer_code = txt.strip(),
            prompt_code = lines('a = 4', 'a += 2')
        )

    def test_blank_parsing(self):
        """ Blanks appear between ?'s by default, are substituted with lib.consts.BLANK_DEFAULT
            in the answer_code. The question marks are removed from the answer code.
        """
        txt = lines('for ?i? in range(?1, 10?):', '\t?a? += i', '?return a?')
        self.assertParsesTo(
            txt,
            answer_code = scrub_blank(txt),
            prompt_code = sub_blank(txt)
        )

        # ignores incomplete fades, and fades completed in comments or strs
        txt = lines('for _ in range?(1, 10):', '\ta? += "?"', 'return a.is_odd? # fun?')
        self.assertParsesTo(
            txt,
            answer_code = txt,
            prompt_code = lines('for _ in range?(1, 10):', '\ta? += "?"', 'return a.is_odd?')
        )

    def test_given_special_comment(self):
        """ Special comments appear in the prompt_code, but not the answer_code.
            The special comment that indicates a line as given in the prompt are
            /#<indentation level>given/
        """
        txt = lines('def foo(x): #0given', '\tx *= x', '\treturn x #1given', '')
        self.assertParsesTo(
            txt,
            answer_code = lines('def foo(x):', '\tx *= x', '\treturn x'),
            prompt_code = txt.strip()
        )

        txt = lines('def foo(x): #10000given', '\tx *= x', '\treturn x #000given', '')
        self.assertParsesTo(
            txt,
            answer_code = lines('def foo(x):', '\tx *= x', '\treturn x'),
            prompt_code = txt.strip()
        )

        with self.subTest('poorly formatted special comments become regular comments'):
            # poorly formatted
            txt = lines('def foo(x): #-10000given', '\tx *= x', '\treturn x #given', '')
            self.assertParsesTo(
                txt,
                answer_code = txt.strip(),
                prompt_code = lines('def foo(x):', '\tx *= x', '\treturn x')
            )

    def test_blank_default_special_comment(self):
        """ Special comments appear in the prompt_code, but not the answer_code.
            The special comment that indicates placeholder text for a fade is
            /#blank <blank placeholder text>/
        """
        txt = lines('x, y = a[?3:-3?]  #blank _:_')
        self.assertParsesTo(
            txt,
            answer_code = 'x, y = a[3:-3]',
            prompt_code = sub_blank(txt)
        )
        txt = lines('x, y = a[?3:-3?]  #blank')
        self.assertParsesTo(
            txt,
            answer_code = 'x, y = a[3:-3]',
            prompt_code = sub_blank(txt)
        )

        with self.subTest('poorly formatted special comments become regular comments'):
            txt = lines('x, y = a[?3:-3?]  #blahblah _:_')
            self.assertParsesTo(
                txt,
                answer_code = scrub_blank(txt),
                prompt_code = sub_blank('x, y = a[?3:-3?]')
            )

    def test_many_comments(self):
        """ Interspersing special and regular comments does not effect behavior """
        txt = lines(
            'def func(x: ?str?): #0given #blank _type_',
            '\tx.modify(42) # 42 is always magic ',  # << !! trailing space is cut
            '\treturn ?x.finish()? #1given #blank x._ # huzzah!'
        )
        self.assertParsesTo(
            txt,
            answer_code = scrub_blank(lines(
                'def func(x: ?str?):',
                '\tx.modify(42) # 42 is always magic',
                '\treturn ?x.finish()? # huzzah!'
            )),
            prompt_code=sub_blank(lines(
                'def func(x: ?str?): #0given #blank _type_',
                '\tx.modify(42)',
                '\treturn ?x.finish()? #1given #blank x._'
            ))
        )

    def test_custom_fading(self):
        """ Blank delimiters can be set through a field 'blankDelimiter' in the metadata
            by one of three values:
                - a str that is the stop & start delimiter
                - an `{ 'start': str, 'stop': str }` object
                - an `{ 'pattern': regex_str }` object

            Delimiters may be special characters in regex, but are not treated as regex
            unless the 'pattern' tag is specified. (e.g. 'blankDelimiter': '$' means
            that $x$ is a valid fade.)
        """
        metadata = { 'blankDelimiter': '--' }
        self.assertParsesTo(
            lines(
                make_metadata_region(**metadata),
                '',
                '4.--times-- do #blank _verb_',
                '\tputs --i.?dis?belief??--',
                'end',
                ''
            ),
            metadata = metadata,
            answer_code = lines(
                '4.times do',
                '\tputs i.?dis?belief??',
                'end'
            ),
            prompt_code = lines(
                f'4.{BLANK_SUBSTITUTE} do #blank _verb_',
                f'\tputs {BLANK_SUBSTITUTE}',
                'end'
            )
        )

        with self.subTest('works with regex reserved chars'):
            metadata = { 'blankDelimiter': '$' }
            self.assertParsesTo(
                lines(
                    make_metadata_region(**metadata),
                    '',
                    '4.$times$ do #blank _verb_',
                    '\tputs $i.?dis?belief??$',
                    'end',
                    ''
                ),
                metadata = metadata,
                answer_code = lines(
                    '4.times do',
                    '\tputs i.?dis?belief??',
                    'end'
                ),
                prompt_code = lines(
                    f'4.{BLANK_SUBSTITUTE} do #blank _verb_',
                    f'\tputs {BLANK_SUBSTITUTE}',
                    'end'
                )
            )

            metadata = { 'blankDelimiter': { 'start': '^', 'end': '$' } }
            self.assertParsesTo(
                lines(
                    make_metadata_region(**metadata),
                    '',
                    '4.^times$ do #blank _verb_',
                    '\tputs ^i.?dis?belief??$',
                    'end',
                    ''
                ),
                metadata = metadata,
                answer_code = lines(
                    '4.times do',
                    '\tputs i.?dis?belief??',
                    'end'
                ),
                prompt_code = lines(
                    f'4.{BLANK_SUBSTITUTE} do #blank _verb_',
                    f'\tputs {BLANK_SUBSTITUTE}',
                    'end'
                )
            )

        with self.subTest('custom regex pattern'):
            metadata = { 'blankDelimiter': { 'pattern': r'--(.+?)%-%' } }
            self.assertParsesTo(
                lines(
                    make_metadata_region(**metadata),
                    '',
                    '4.--times%-% do #blank _verb_',
                    '\tputs --i.?dis?belief??%-%',
                    'end',
                    ''
                ),
                metadata = metadata,
                answer_code = lines(
                    '4.times do',
                    '\tputs i.?dis?belief??',
                    'end'
                ),
                prompt_code = lines(
                    f'4.{BLANK_SUBSTITUTE} do #blank _verb_',
                    f'\tputs {BLANK_SUBSTITUTE}',
                    'end'
                )
            )


    def test_illegal_custom_fading(self):
        """ Custom fading cannot use a builtin delimiter (` ' " #), must
            capture exactly one substring when it matches, and must not
            match on the empty string
        """
        def assertBadCustomDelim(*args, **kwargs):
            delim = args[0] if args else kwargs
            metadata = make_metadata_region(blankDelimiter=delim)
            self.assertSyntaxError(metadata)

        for c in '#`\'"':
            with self.subTest(f'cannot shadow builtin delimiter {c}'):
                assertBadCustomDelim(c)
                assertBadCustomDelim(start = '-', end = c )
                assertBadCustomDelim(start = c, end = '-' )
                assertBadCustomDelim(pattern = c + r'(.+?)-')
                assertBadCustomDelim(pattern = r'-(.+?)' + c)

        with self.subTest('custom groups must capture exactly one substring'):
            assertBadCustomDelim(pattern = r'-.*?-') # no captures
            assertBadCustomDelim(pattern = r'-(.*?):(.*?)-') # too many captures

        with self.subTest('blankDelimiter must not match empty string'):
            assertBadCustomDelim(pattern='.*')

        with self.subTest('blankDelimiter must adhere to schema'):
            assertBadCustomDelim(0)
            assertBadCustomDelim('')
            assertBadCustomDelim([])
            assertBadCustomDelim(badSchema = '-')

    def test_standard_input(self):
        """ Generates a standard input (polynomial_evaluation.py) and tests the output """
        q_lines = (
            'Write a function <code>poly</code> that calculates the values of a  ',
            'polynomial with the given coefficients at the given value of <code>x</code>,',
            '\tie, evaluate $$f(x) = \sum_i \textrm{coeffs}_i ~ x^i$$\t'
        )
        q_text = "\n".join(q_lines)
        q_trim = "\n".join(map(str.rstrip, q_lines))

        setup = lines(
            'a: int = 3',
            'b = a + 4',
            'l: list[int] = [1, 2, 3]',
            'c = l[0] = 3'
        )

        raw = lines(
            'def poly(coeffs, x): #0given',
            '    # Keep track of the total as we iterate through each term.',
            '    # Each term is of the form coeff*(x**power).',
            '    total = ?0? #blank test #1given # total starts at 0',
            '    ',
            '    # Extract the power and coefficient for each term.',
            '    for ?power, coeff? in enumerate(coeffs):',
            '        # Add the value of the term to the total.',
            '        ?total? = total + coeff * (x ** power) #2given',
            '    return total #1given',
        )

        ans = lines(
            'def poly(coeffs, x):',
            '    # Keep track of the total as we iterate through each term.',
            '    # Each term is of the form coeff*(x**power).',
            '    total = 0 # total starts at 0',
            '',
            '    # Extract the power and coefficient for each term.',
            '    for power, coeff in enumerate(coeffs):',
            '        # Add the value of the term to the total.',
            '        total = total + coeff * (x ** power)',
            '    return total',
        )
        ppt = lines(
            'def poly(coeffs, x): #0given',
            '    total = !BLANK #blank test #1given',
            '    for !BLANK in enumerate(coeffs):',
            '        !BLANK = total + coeff * (x ** power) #2given',
            '    return total #1given',
        )

        test = lines(
            'from pl_helpers import name, points',
            'from pl_unit_test import PLTestCase',
            'from code_feedback import Feedback',
            '',
            'class Test(PLTestCase):',
            '    @points(1)',
            '    @name("testing single case")',
            '    def test_0(self):',
            '        case = [[10], 3]',
            '        points = 0',
            '        user_val = Feedback.call_user(self.st.poly, *case)',
            '        ref_val = self.ref.poly(*case)',
            '        if Feedback.check_scalar(f"args: {case}", ref_val, user_val):',
            '            points += 1',
            '        Feedback.set_score(points)',
            ''
        )

        src = lines(
            f'"""{q_text}"""',
            '',
            make_region('setup_code', setup),
            '',
            raw,
            '',
            '',
            make_region('test', test),
            ''
        )

        self.assertParsesTo(
            src,
            answer_code = ans,
            prompt_code = ppt,
            test = test.strip(),
            setup_code = setup,
            question_text = q_trim,
        )


main()