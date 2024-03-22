import prairielearn as pl
import lxml.html
import chevron
import json


QUESTION_MAIN_FILE_DEFAULT = "main.s"
SHOW_FLOAT_REGISTERS_DEFAULT = False
SHOW_KERNEL_TOGGLES_DEFAULT = False
SHOW_DATA_PANEL = False
SHOW_STACK_PANEL = False
SHOW_OUTPUT_PANEL = True


def prepare(element_html, data):
    element = lxml.html.fragment_fromstring(element_html)
    required_attribs = ['editor-id']
    optional_attribs = ['question-main-file',
                        'default-view',
                        'show-float-registers',
                        'show-kernel-toggles',
                        'show-data-panel',
                        'show-stack-panel',
                        'show-output-panel']
    pl.check_attribs(element, required_attribs, optional_attribs)


def render(element_html, data):
    # Currently only supports the question panel.
    if data['panel'] != 'question':
        return ''

    element = lxml.html.fragment_fromstring(element_html)
    editor_id = pl.get_string_attrib(element, 'editor-id')
    question_main_file = pl.get_string_attrib(element, 'question-main-file', QUESTION_MAIN_FILE_DEFAULT)
    show_float_regs = pl.get_boolean_attrib(element, 'show-float-registers', SHOW_FLOAT_REGISTERS_DEFAULT)
    show_kernel_toggles = pl.get_boolean_attrib(element, 'show-kernel-toggles', SHOW_KERNEL_TOGGLES_DEFAULT)
    show_data_panel = pl.get_boolean_attrib(element, 'show-data-panel', SHOW_DATA_PANEL)
    show_stack_panel = pl.get_boolean_attrib(element, 'show-stack-panel', SHOW_STACK_PANEL)
    show_output_panel = pl.get_boolean_attrib(element, 'show-output-panel', SHOW_OUTPUT_PANEL)

    default_view = pl.get_string_attrib(element, 'default-view', "")
    if default_view not in ['run', 'column']:
        default_view = 'run'

    inner_html = pl.inner_html(element).strip()
    html_params = {
        'question': True,
        'editor_id': editor_id,
        'question_main_file': question_main_file,
        'default_view': default_view,
        'enable_float_regs': str(show_float_regs).lower(),
        'enable_kernel_toggles': str(show_kernel_toggles).lower(),
        'enable_data_panel': str(show_data_panel).lower(),
        'enable_stack_panel': str(show_stack_panel).lower(),
        'enable_output_panel': str(show_output_panel).lower(),
        'element_files_url': data['options']['client_files_element_url'],
        'question_files_url': data['options']['client_files_question_url'],
        'inner_html': inner_html,
        'uuid': pl.get_uuid()
    }

    with open('pl-mips-debugger.mustache', 'r', encoding='utf-8') as f:
        html = chevron.render(f, html_params).strip()

    return html
