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
    pl.check_attribs(element, required_attribs=[], optional_attribs=['collapsible'])


def render(element_html, data):

    # Get the content
    element = lxml.html.fragment_fromstring(element_html)
    content = pl.inner_html(element)

    # Create and return html
    html_params = {'text': content}
    with open('pl-tip.mustache', 'r', encoding='utf-8') as f:
        html = chevron.render(f, html_params).strip()

    return html