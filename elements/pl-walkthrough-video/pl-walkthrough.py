import prairielearn as pl
import lxml.html
import chevron
import os



TYPE_DEFAULT = 'static'
DIRECTORY_DEFAULT = 'clientFilesQuestion'
INLINE_DEFAULT = False
ALT_TEXT_DEFAULT = 'YouTube link'
NOTES_DEFAULT = ""


def prepare(element_html, data):
    element = lxml.html.fragment_fromstring(element_html)
    pl.check_attribs(element, required_attribs=['url'], optional_attribs=['alt', 'notes'])


def render(element_html, data):
    element = lxml.html.fragment_fromstring(element_html)

    # Get file name or raise exception if one does not exist
    url = pl.get_string_attrib(element, 'url')

    # Get alternate-text text 
    alt_text = pl.get_string_attrib(element, 'alt', ALT_TEXT_DEFAULT)

    # Get notes text 
    notes = pl.get_string_attrib(element, 'notes', NOTES_DEFAULT)

    # Create and return html
    html_params = {'url': url, 'alt': alt_text, 'notes': notes}
    with open('pl-walkthrough.mustache', 'r', encoding='utf-8') as f:
        html = chevron.render(f, html_params).strip()

    return html