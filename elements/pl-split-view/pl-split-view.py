import prairielearn as pl
import lxml.html
import chevron


DEFAULT_TITLE = 'Split View'
DEFAULT_BUTTON_TEXT = 'Open split view'


def prepare(element_html, data):
    element = lxml.html.fragment_fromstring(element_html)
    required_attribs = ['left-ids', 'right-ids']
    optional_attribs = ['title']
    pl.check_attribs(element, required_attribs, optional_attribs)


def render(element_html, data):
    # Currently only supports the question panel.
    if data['panel'] != 'question':
        return ''

    element = lxml.html.fragment_fromstring(element_html)
    title = pl.get_string_attrib(element, 'title', DEFAULT_TITLE)

    left_ids = pl.get_string_attrib(element, 'left-ids')
    left_ids = [id.strip() for id in left_ids.split()]
    if not left_ids:
        raise Exception("Must specify at least one element to split left.")

    right_ids = pl.get_string_attrib(element, 'right-ids')
    right_ids = [id.strip() for id in right_ids.split()]
    if not right_ids:
        raise Exception("Must specify at least one element to split right.")

    intersect = set(left_ids).intersection(set(right_ids))
    if intersect:
        raise Exception("Cannot have same element in both left and right splits.")

    inner_html = pl.inner_html(element).strip()
    if not inner_html:
        inner_html = DEFAULT_BUTTON_TEXT

    html_params = {
        'question': True,
        'left_ids': left_ids,
        'right_ids': right_ids,
        'title': title,
        'inner_html': inner_html,
        'uuid': pl.get_uuid()
    }

    with open('pl-split-view.mustache', 'r', encoding='utf-8') as f:
        html = chevron.render(f, html_params).strip()

    return html
