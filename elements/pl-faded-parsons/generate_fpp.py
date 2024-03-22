
from json import dumps
from os import path, PathLike
from shutil import copyfile
from uuid import uuid4
from dataclasses import dataclass
from argparse import Namespace

from lib.consts import *
from lib.io_helpers import *

from lib.tokens import lex
from lib.name_visitor import AnnotatedName
from lib.autograde import AutograderConfig, new_autograder_from_ext
from lib.parse import parse_fpp_regions

@dataclass
class Options:
    def __init__(self, cli_args: Namespace, metadata: Dict = {}):
        self.force_generate_json = False

        self.cli_args: Namespace = cli_args
        self.profile: bool = cli_args.profile
        self.source_paths: list = cli_args.source_paths
        self.verbosity: int = cli_args.verbosity

        self.metadata: dict = metadata
        self.do_parse: bool = metadata.get("parse", cli_args.parse)
        self.ag_extension: str = metadata.get("autograder", '')
        self.make_dir: bool = metadata.get("make-dir", cli_args.make_dir)

        self.out_path: str = cli_args.output_path or metadata.get("output-path", '')

    def update(self, **metadata):
        self.metadata.update(metadata)
        self.do_parse: bool = metadata.get("parse", self.do_parse)
        self.ag_extension: str = metadata.get("autograder", self.ag_extension)
        self.make_dir: bool = metadata.get("make-dir", self.make_dir)

        self.out_path = self.cli_args.output_path or metadata.get("output-path", self.out_path)
        
    def dump(self) -> str:
        """Produce a json dump of this object"""

        return dumps({
            "autograder" : self.ag_extension,
            "parse" : self.do_parse,
            "make-dir" : self.make_dir,
            "output-path" : self.out_path
        })


def generate_question_html(
    prompt_code: str, *,
    question_text: str = None,
    tab: str = '  ',
    setup_names: List[AnnotatedName] = None,
    answer_names: List[AnnotatedName] = None
) -> str:
    """Turn an extracted prompt string into a question html file body"""
    indented = prompt_code.replace('\n', '\n' + tab)

    if question_text is None:
        question_text = tab + '<!-- Write the question prompt here -->'
    elif setup_names or answer_names:
        question_text = tab + '<h3> Prompt </h3>\n' + tab + question_text

        question_text += '\n\n<markdown>\n'

        def format_annotated_name(name: AnnotatedName) -> str:
            out = ' - `' + name.id
            if name.annotation:
                out += ': ' + name.annotation
            out += '`'
            if name.description:
                out += ', ' + name.description
            return out

        if setup_names:
            question_text += '### Provided\n'
            question_text += '\n'.join(map(format_annotated_name, setup_names))
            if answer_names:
                question_text += '\n\n'

        if answer_names:
            question_text += '### Required\n'
            question_text += '\n'.join(
                map(format_annotated_name, answer_names))

        question_text += '\n</markdown>\n'

    return """<!-- AUTO-GENERATED FILE -->
<pl-question-panel>
{question_text}
</pl-question-panel>

<!-- see README for where the various parts of question live -->
<pl-faded-parsons>
{tab}{indented}
</pl-faded-parsons>""".format(question_text=question_text, tab=tab, indented=indented)


def generate_info_json(question_name: str, autograder: AutograderConfig, *, indent=4) -> str:
    """ Creates the default info.json for a new FPP question, with a unique v4 UUID.
        Expects `question_name` to be lower snake case.
    """
    question_title = ' '.join(l.capitalize() for l in question_name.split('_'))

    info_json = {
        'uuid': str(uuid4()),
        'title': question_title,
        'topic': '',
        'tags': ['berkeley', 'fp'],
        'type': 'v3',
    }

    info_json.update(autograder.info_json_update())

    return dumps(info_json, indent=indent) + '\n'


def generate_fpp_question(
    source_path: PathLike[AnyStr], *,
    options: Options = None,
):
    """ Takes a path of a well-formatted source (see `extract_prompt_ans`),
        then generates and populates a question directory of the same name.
    """

    if options.verbosity > -1: Bcolors.info('Generating from source', source_path)

    if options.verbosity > 0: print('- Extracting from source...')

    source_path = resolve_path(source_path)
    with open(source_path, 'r') as source:
        source_code = ''.join(source)
        tokens = lex(source_code, source_path=source_path)
        regions = parse_fpp_regions(tokens)

    def remove_region(key, default=''):
        if key in regions:
            v = regions[key]
            del regions[key]
            return v
        return default

    metadata = remove_region('metadata')
    metadata["autograder"] = metadata.get("autograder", file_ext(source_path))
    options.update(**metadata)

    autograder: AutograderConfig = new_autograder_from_ext(options.ag_extension)

    if options.out_path == '':
        dirname = path.dirname(source_path)
        q_dir = './' if dirname == '' else dirname
    else:
        q_dir = options.out_path

    question_name = file_name(source_path)
    if options.make_dir:
        # create all new content in a new folder that is a
        # sibling of the source file in the filesystem
        question_dir = path.join(q_dir, question_name)
    else:
        question_dir = q_dir
    test_dir = path.join(question_dir, 'tests')
    
    if options.verbosity > 0: print('- Creating destination directories...')
    
    make_if_absent(question_dir)
    make_if_absent(test_dir)

    copy_dest_path = path.join(question_dir, 'source.py')
    if options.verbosity > 0: 
        print('- Copying {} to {} ...'.format(path.basename(source_path), copy_dest_path))
    copyfile(source_path, copy_dest_path)

    setup_code = remove_region('setup_code', SETUP_CODE_DEFAULT)
    answer_code = remove_region('answer_code')
    server_code = remove_region('server')
    prompt_code = remove_region('prompt_code')
    question_text = remove_region('question_text')
    
    if options.verbosity > 0: print('- Populating {} ...'.format(question_dir))

    gen_server_code, setup_names, answer_names = autograder.generate_server(
        setup_code=setup_code,
        answer_code=answer_code,
        no_ast=(not options.do_parse)
    )
    server_code = server_code or gen_server_code

    question_html = generate_question_html(
        prompt_code,
        question_text=question_text,
        setup_names=setup_names,
        # show_required removed:
        # answer_names=answer_names if show_required else None
    )

    write_to(question_dir, 'question.html', question_html)
    write_to(question_dir, 'server.py', server_code)
    write_to(question_dir, 'solution', answer_code)

    json_path = path.join(question_dir, 'info.json')
    json_region = remove_region('info.json')
    missing_json = not path.exists(json_path)
    if options.force_generate_json or json_region or missing_json:
        json_text = json_region or generate_info_json(question_name, autograder)
        write_to(question_dir, 'info.json', json_text)
        if not missing_json:
            Bcolors.warn('  - Overwriting', json_path,
                         'using \"info.json\" region...' if json_region else '...')

    

    if options.verbosity > 0:
        print('- Populating {} ...'.format(test_dir))

    test_region = remove_region('test')

    autograder.populate_tests_dir(
        test_dir,
        answer_code,
        setup_code,
        test_region,
        log_details= options.verbosity > 0
    )

    if metadata:
        write_to(question_dir, 'metadata.json', options.dump())

    if regions:
        Bcolors.warn('- Writing unrecognized regions:')

    for raw_path, data in regions.items():
        if not raw_path:
            Bcolors.warn('  - Skipping anonymous region!')
            continue

        # if no file extension is given, give it .py (removed due to Gemfile)
        # if not file_ext(raw_path):
        #     raw_path += '.py'

        # ensure that the directories exist before writing
        final_path = path.join(question_dir, raw_path)
        make_if_absent(path.dirname(final_path))
        Bcolors.warn('  -', final_path, '...')

        # write files
        write_to(question_dir, raw_path, data)
    
    autograder.clean_tests_dir(test_dir)

    Bcolors.printf(Bcolors.OK_GREEN, 'Done.')


def generate_many(args: Namespace):
    if not args.source_paths:
        args.source_paths = auto_detect_sources()

    def generate_one(source_path, force_json=False):
        options = Options(args)
        options.force_generate_json = force_json

        try:
            generate_fpp_question(
                source_path,
                options=options
            )
            return True
        except SyntaxError as e:
            Bcolors.fail('SyntaxError:', e.msg)
        except OSError as e:
            Bcolors.fail('FileNotFoundError:', *e.args)

        return False

    successes, failures = 0, 0

    for source_path in args.source_paths:
        if generate_one(source_path):
            successes += 1
        else:
            failures += 1

    for source_path in args.force_json:
        if generate_one(source_path, force_json=True):
            successes += 1
        else:
            failures += 1

    # print batch feedback
    if successes + failures > 1:
        def n_files(n): return str(n) + ' file' + ('' if n == 1 else 's')
        if successes:
            Bcolors.ok('Batch completed successfully on', n_files(successes), end='')
            if failures:
                Bcolors.fail(' and failed on', n_files(failures))
            else:
                print()
        else:
            Bcolors.fail('Batch failed on all', n_files(failures))


def profile_generate_many(args: Namespace):
    from cProfile import Profile
    from pstats import Stats, SortKey

    with Profile() as pr:
        generate_many(args)

    stats = Stats(pr)
    stats.sort_stats(SortKey.TIME)
    print('\n---------------\n')
    stats.print_stats()


def main():
    args = parse_args()

    if args.profile:
        profile_generate_many(args)
    else:
        generate_many(args)


if __name__ == '__main__':
    main()
