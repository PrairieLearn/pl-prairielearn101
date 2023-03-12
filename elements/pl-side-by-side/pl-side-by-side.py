import prairielearn as pl
import lxml.html
import chevron


def prepare(element_html, data):

  # parse element html
  element = lxml.html.fragment_fromstring(element_html)

  # check element attributes (currently none required, so this is commented)
  # pl.check_attribs(element, required_attribs=[], optional_attribs=[])


  for child in element:

    # skip comments
    if isinstance(child, lxml.html.HtmlComment):
      continue

    # # background
    # if child.tag in ['pl-content', 'pl_content']:
    #   pl.check_attribs(child, required_attribs=[], optional_attribs=['left', 'right', 'top', 'bottom', 'valign', 'halign'])

      


def render(element_html, data):
  # if data['panel'] == 'question':
  #   element = lxml.html.fragment_fromstring(element_html)
  #   return "<table><tr><th>Question</th><th>Reference</th></tr><tr><td>" + pl.inner_html(element) + "</td><td>" + pl.inner_html(element) + "</td></tr></table>"
  # else:
  #   return ''

  # parse element html
  element = lxml.html.fragment_fromstring(element_html)

  for child in element:

    # skip comments
    if isinstance(child, lxml.html.HtmlComment):
      continue

    # content child
    if child.tag in ['pl-content', 'pl_content']:
      content_html = pl.inner_html(child)
      continue

    # reference child
    if child.tag in ['pl-reference', 'pl_reference']:
      reference_html = pl.inner_html(child)
      continue
  
  html_params = {
    'content': content_html,
    'reference': reference_html,
  }
  with open('pl-side-by-side.mustache', 'r', encoding='utf-8') as f:
    html = chevron.render(f, html_params).strip()
  return html
