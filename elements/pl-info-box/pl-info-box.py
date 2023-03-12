import prairielearn as pl
import lxml.html
import chevron

TYPE_DEFAULT = 'note'
NOTE_BACKGROUND = "#eeeeee"
VIDEO_RECAP_BACKGROUND = "#ecf5e1"
INFO_BACKGROUND = "#e1f1f5"
WARNING_BACKGROUND = "#faf9d2"

def prepare(element_html, data):
    element = lxml.html.fragment_fromstring(element_html)
    pl.check_attribs(element, required_attribs=[], optional_attribs=['type'])


def render(element_html,data):

    # Get the content
    element = lxml.html.fragment_fromstring(element_html)

    content = pl.inner_html(element)

    # Get type (optional)
    type = pl.get_string_attrib(element, 'type', TYPE_DEFAULT)

    if type == "video-recap":
        backgroundColor = VIDEO_RECAP_BACKGROUND
        label = "Video Recap"
    if type == "info":
        backgroundColor = INFO_BACKGROUND
        label = "Heads Up"
    if type == "warning":
        backgroundColor = WARNING_BACKGROUND
        label = "Warning!"
    if type == "note":
        backgroundColor = NOTE_BACKGROUND
        label = "Note"

    # Create and return html
    html_params = {'type':type, 'background-color':backgroundColor, 'content':content, 'label':label}
    with open('pl-info-box.mustache', 'r', encoding='utf-8') as f:
        html = chevron.render(f, html_params).strip()
    return html