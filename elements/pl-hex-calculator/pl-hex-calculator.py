import prairielearn as pl
import lxml.html
import chevron
import os


def prepare(element_html, data):
    element = lxml.html.fragment_fromstring(element_html)
    required_attribs = []
    optional_attribs = []
    pl.check_attribs(element, required_attribs, optional_attribs)

def render(element_html, data):
    
    render_obj = {
        'element_files_url': data["options"]["client_files_element_url"],
        'uuid': pl.get_uuid()
    }

    with open('pl-hex-calculator.mustache', 'r', encoding='utf-8') as f:
        html = chevron.render(f, render_obj).strip()

    return html