import prairielearn as pl
import lxml.html
import chevron
import os



TYPE_DEFAULT = 'static'
DIRECTORY_DEFAULT = 'clientFilesQuestion'
COLLAPSIBLE_DEFAULT = "True"
SETUP_DEFAULT = ""
TEXT_AREA_DEFAULT = ""


def prepare(element_html, data):
    element = lxml.html.fragment_fromstring(element_html)
    pl.check_attribs(element, required_attribs=[], optional_attribs=['collapsible','setup-variables', 'text-area'])


def render(element_html, data):
    element = lxml.html.fragment_fromstring(element_html)

    # Get setting for if this is in a collapsible button thing
    collapsible = pl.get_string_attrib(element, 'collapsible', COLLAPSIBLE_DEFAULT)

    # Get setup variables
    setup_variables = pl.get_string_attrib(element, 'setup-variables', SETUP_DEFAULT)

    # Get text area text
    text_area = pl.get_string_attrib(element, 'text-area',TEXT_AREA_DEFAULT)

    # Get the location of the course files
    course_files_path = data["options"]["client_files_course_url"]

    # Create and return html
    if collapsible.lower()=="true":
        html_params = {'course-files-path': course_files_path, 'collapsible': collapsible, 'setup-variables': setup_variables, 'text-area': text_area}
    else:
        html_params = {'course-files-path': course_files_path, 'setup-variables': setup_variables, 'text-area': text_area}
    with open('pl-matcrab-workspace.mustache', 'r', encoding='utf-8') as f:
        html = chevron.render(f, html_params).strip()

    return html