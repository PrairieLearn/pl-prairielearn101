from os.path import *
from typing import *

from argparse import Namespace, ArgumentParser, RawTextHelpFormatter, BooleanOptionalAction
from functools import partial
from os import getcwd, listdir, makedirs, PathLike
from re import compile

from lib.consts import Bcolors, PROGRAM_DESCRIPTION


def format_ln(source_path, line_number: int):
    return '({}:{})'.format(source_path or 'line', line_number)


def file_name(file_path: PathLike[AnyStr]) -> AnyStr:
    """Returns the basename in the path without the file extensions"""
    return splitext(basename(file_path))[0]


def file_ext(file_path: PathLike[AnyStr]) -> AnyStr:
    """Returns the file extension (or '' if none exists)"""
    return splitext(basename(file_path))[1]


def write_to(parent_dir: PathLike[AnyStr], file_path: PathLike[AnyStr], data: str):
    """Opens ./`parent_dir`/`file_path` and writes `data` to it"""
    with open(join(parent_dir, file_path), 'w+') as f:
        f.write(data)


def make_if_absent(dir_path: str):
    """ Creates the director(ies - nested ok) if they do not yet exist.
        Otherwise it does nothing
    """
    makedirs(dir_path, exist_ok=True)


def read_region_source_lines(source_path: str, region_source: str) -> str:
    """ Reads the region_source and returns its contents, or raises
        a FileNotFoundError or other OSError in opening the file.

        Searches in ./ and ./`source_path`/ for `region_source`
    """
    if not exists(region_source) and source_path:
        region_source = join(dirname(source_path), region_source)

    with open(region_source, 'r') as f:  # may raise OSError
        return ''.join(f.readlines())


def auto_detect_sources(questions_dir: Optional[PathLike[AnyStr]] = None) -> list[PathLike[AnyStr]]:
    if not questions_dir:
        Bcolors.warn('** No paths provided, auto-detecting questions directory **')

    try:
        questions_dir = questions_dir or resolve_path(
            'questions', path_is_dir=True, silent=True)
    except FileNotFoundError as e:
        Bcolors.fail(
            '** Auto-detection failed. Please provide paths to sources. (use --help for more info) **')
        if e.args:
            Bcolors.fail(*e.args)

    resolve = partial(join, questions_dir)
    def is_valid(f):
        return isfile(f) and file_ext(f).endswith('py')
    return list(filter(is_valid, map(resolve, listdir(questions_dir))))


def resolve_path(path: str, *,
                 silent: bool = False,
                 path_is_dir: bool = False,
                 ) -> str:
    """ Attempts to find a matching source path in the following destinations:

        ```
        standard course directory structure:
        + <course>
        | ...        << search here 3rd
        |-+ elements/pl-faded-parsons
        | |-generate_fpp.py
        | | ...      << search here 1st
        |
        |-+ questions
        | | ...      << search here 2nd
        |
        ```
        Will search ./questions/ 4th, in case this is run from <course>/
    """
    if not path_is_dir and (isdir(path) or not file_ext(path)):
        path += '.py'

    if exists(path):
        return path

    def warn():
        if not silent:
            Bcolors.warn('- Could not find', original,
                         'in current directory. Proceeding with detected file.')

    original = path

    # if this is in 'elements/pl-faded-parsons', back up to course directory
    h, t0 = split(getcwd())
    _, t1 = split(h)
    if t0 == 'pl-faded-parsons' and t1 == 'elements':
        # try original in a questions directory on the course level
        new_path = join('..', '..', 'questions', original)
        if exists(new_path):
            warn()
            return new_path

        # try original in course directory
        new_path = join('..', '..', original)
        if exists(new_path):
            warn()
            return new_path

    new_path = join('questions', original)
    if exists(new_path):
        warn()
        return new_path

    raise FileNotFoundError('Could not find ' +
                            ('directory ' if path_is_dir else 'file ') + original)


def make_blank_re(config):
    """ expects config to be
        `delim_str  | { "pattern": regex }  | { "start": str, "end": str }`
    """
    def validate(re_str: str) -> Pattern:
        if any(c in re_str for c in '#`\'"'):
            raise SyntaxError('custom patterns for blank delimiter ' +
                'cannot use #, \', ", or `')

        re = compile(re_str)

        if re.groups != 1:
            raise SyntaxError('custom patterns for blankDelimiter must ' +
                'capture exactly one group (the text to fade out)')

        if re.match('') is not None:
            raise SyntaxError('custom patterns for blankDelimiter must' +
                'not match the empty string')

        return re

    reserved = r'.+*?^$()[]{}|'
    def validate_l_r(l, r):
        if not l or not r:
            raise SyntaxError('blankDelimiter must not be empty')
        def esc(x):
            for c in reserved:
                if c == x:
                    return '\\' + c
            return x
        return validate(esc(l) + r'(.+?)' + esc(r))

    if isinstance(config, str):
        return validate_l_r(config, config)

    if not isinstance(config, dict):
        raise SyntaxError('blankDelimiter metadata must either be a ' +
            'delimiter string or a config object')

    if 'pattern' in config:
        return validate(config['pattern'])

    if 'start' in config and 'end' in config:
        s, e = config['start'], config['end']

        if not isinstance(s, str) or not isinstance(e, str):
            raise SyntaxError('custom blank delimiter start and end ' +
                'must be strings')

        return validate_l_r(s, e)

    raise SyntaxError('''blankDelimiter must be a string or adhere to schema:
    { "start": start_delimiter_string, "end": end_delimiter_string } |
    { "pattern": regex_string_that_captures_faded_text }''')


def parse_args(arg_text: str = None) -> Namespace:
    """ Returns a Namespace containing all the flag and path data.
        If arg_text is not provided, uses `sys.argv`.
    """
    parser = ArgumentParser(description=PROGRAM_DESCRIPTION,
                            formatter_class=RawTextHelpFormatter)

    parser.add_argument('--profile', action='store_true',
                        help='prints profile data after running')
    parser.add_argument('--verbose', '-v', action='count', default=1,
                        help='specify the verbosity with which to run (max 3)')
    parser.add_argument('--quiet', '-q', action='count', default=0,
                        help='specify the reduction in verbosity with which to run (max 3)')
    parser.add_argument('--parse', action=BooleanOptionalAction,
                        help='parse the code with py.ast to derive content (also --no-parse)')
    parser.add_argument('--make-dir', '--duplicate-directory', action=BooleanOptionalAction, default=True,
                        help='create a directory with the name of the question in the output path')
    parser.add_argument('--output-path', '-o', action='store', nargs='?', metavar='path',
                        help='specify what directory to write the generated question to (see --duplicate-directory)\n' +\
                             'default is next to the source path')
    parser.add_argument('source_path', action='append', nargs='*', metavar='paths')
    parser.add_argument('--questions-dir', action='append', metavar='path',
                        help='target all .py files in directory as sources')
    parser.add_argument('--force-json', action='append', metavar='path',
                        help='will overwrite the question\'s info.json file with auto-generated content')

    # if arg_text is not set, then it gets from the command line
    ns = parser.parse_intermixed_args(args=arg_text)

    # unpack weird nesting, delete confusing name
    ns.source_paths = [p for l in ns.source_path for p in l]
    del ns.source_path

    # combine verbose-ness and quiet-ness and cut off into domain [-3, 3]
    ns.verbosity = ns.verbose - ns.quiet
    ns.verbosity = min(ns.verbosity, 3)
    ns.verbosity = max(-3, ns.verbosity)
    del ns.verbose

    if ns.questions_dir:
        for qd in ns.questions_dir:
            ns.source_paths.extend(auto_detect_sources(qd))
        del ns.questions_dir

    ns.force_json = ns.force_json or list()
    return ns
