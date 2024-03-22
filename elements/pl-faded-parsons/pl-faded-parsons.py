import prairielearn as pl
import lxml.html as xml
import chevron
import os
import base64
import json
import re
import random


#
# Helper functions
#
def read_file_lines(data, filename, error_if_not_found=True):
    """Return a string of newline-separated lines of code from some file in serverFilesQuestion."""
    path = os.path.join(data["options"]["question_path"], 'serverFilesQuestion', filename)
    try:
        f = open(path, 'r')
        return f.read()
    except FileNotFoundError as e:
        if error_if_not_found:
            raise e
        else:
            return False


def get_answers_name(element_html):
    # use answers-name to namespace multiple pl-faded-parsons elements on a page
    element = xml.fragment_fromstring(element_html)
    answers_name = pl.get_string_attrib(element, 'answers-name', None)
    if answers_name is not None:
        answers_name = answers_name + '-'
    else:
        answers_name = ''
    return answers_name


def get_student_code(element_html, data):
    answers_name = get_answers_name(element_html)
    student_code = data['submitted_answers'].get(answers_name + 'student-parsons-solution', None)
    return student_code


class Parser:

    def __init__(self, raw_lines):
        
        lines = raw_lines.split('\n')
        self.line_segments = [ line.strip().split('!BLANK') for line in lines ]

        # line_dict example:
        # {
        #     "language" : "py",
        #     "indent"   : 4,
        #     "segments" : [
        #         { "code"  : { "content" : "return"  }},
        #         { "blank" : { "default" : "lst[__]" }}
        #     ]
        # }

    def old_state(self, language, old_starter, old_submission, indent_size=4):
        scrambled = []
        given = []

        for line in old_starter:
            segments = []

            old_segments = line['segments']['given_segments']
            segments = [{ "code" : { "content" : old_segments[0] }}]

            for segment, fill in zip(old_segments[1:], line['segments']['blank_values']):
                segments.append({ "blank" : { "default" : fill    }})
                segments.append({ "code"  : { "content" : segment }})

            scrambled.append({
                "language" : language,
                "segments" : segments
            })

        for line in old_submission:
            segments = []

            old_segments = line['segments']['given_segments']
            segments = [{ "code" : { "content" : old_segments[0] }}]

            for segment, fill in zip(old_segments[1:], line['segments']['blank_values']):
                segments.append({ "blank" : { "default" : fill    }})
                segments.append({ "code"  : { "content" : segment }})

            given.append({
                "language" : language,
                "indent" : line['indent'] * indent_size,
                "segments" : segments
            })
        
        return scrambled, given

    def get_scrambled_and_given(self, language, indent_size=4, max_distractors=10):

        scrambled = []
        given = []
        distractors = []

        for segments in self.line_segments:
            new_line = { "language": language }

            matches = re.findall(r'#blank [^#]*', segments[-1])
            tail = re.sub(r'#blank [^#]*', '', segments[-1])
            blank_count = len(segments) - 1
            fills = list(map(lambda e: e.replace('#blank ', ""), matches)) + [""] * (blank_count-len(matches))
            segments[-1] = tail
            
            parsed_segments = [{ "code" : { "content" : segments[0] } }]
            for segment, pre_fill in zip(segments[1:], fills):
                width = str(len(pre_fill)+1) if pre_fill != "" else "4"
                parsed_segments.append({ "blank" : { "default" : pre_fill, "width" : width } })
                parsed_segments.append({ "code"  : { "content" : segment  } })

            matches = re.search(r'#([0-9]+)given', tail)
            if matches is not None:
                indent = int(matches.group(1))
                new_line['indent'] = indent * indent_size
                parsed_segments[-1] = {
                    "code" : { "content" : re.sub(r'#([0-9]+)given', '', tail).strip() }
                }
                new_line['segments'] = parsed_segments
                given.append(new_line)
                continue

            if re.match(r'#distractor', tail):
                parsed_segments[-1] = {
                    "code" : { "content" : re.sub(r'#distractor', '', tail).strip() }
                }
                new_line['segments'] = parsed_segments
                distractors.append(new_line)
                continue

            new_line['segments'] = parsed_segments
            scrambled.append(new_line)
        
        
        for _ in range(max_distractors):
            if len(distractors) == 0:
                break
            index = random.randint(len(distractors))
            scrambled.append(distractors.pop(index))

        return scrambled, given


def base64_encode(s):
    return base64.b64encode(s.encode("ascii")).decode("ascii")


def render_question_panel(element_html, data):
    """Render the panel that displays the question (from code_lines.txt) and interaction boxes"""
    element = xml.fragment_fromstring(element_html)
    answers_name = get_answers_name(element_html)

    format = pl.get_string_attrib(element, "format", "right").replace("-", '_')
    if format not in ("bottom", "right", "no_code"):
        raise Exception(f"Unsupported pl-faded-parsons format: \"{format}\". Please see documentation for supported formats")

    lang = pl.get_string_attrib(element, "language", None)

    html_params = {
        "code_lines": str(element.text),
    }

    def get_child_text_by_tag(element, tag: str) -> str:
        """get the innerHTML of the first child of `element` that has the tag `tag`
        default value is empty string"""
        return next((elem.text for elem in element if elem.tag == tag), "")

    def get_code_lines():
        code_lines = get_child_text_by_tag(element, "code-lines") or \
            read_file_lines(data, 'code_lines.txt', error_if_not_found=False)

        if not code_lines:
            raise Exception("A non-empty code_lines.txt or <code-lines> child must be provided in right (horizontal) placement.")
        
        return code_lines

    # pre + post text
    pre_text = get_child_text_by_tag(element, "pre-text") \
        .rstrip("\n") # trim trailing newlines
    post_text = get_child_text_by_tag(element, "post-text") \
        .lstrip("\n") # trim leading newlines

    pre  = { "text" : pre_text  }
    post = { "text" : post_text }

    if lang:
        pre.update({ "language" : lang })
        post.update({ "language" : lang })

    if pre_text:
        html_params.update({ 
            "pre_text" : pre,
        })
    if post_text:
        html_params.update({
            "post_text" : post,
        })

    try:
        raw_lines = get_code_lines()
    except:
        raw_lines = str(element.text)
    
    parse = Parser(raw_lines.strip())

    starter_lines_data_available    = 'starter-lines' in data['submitted_answers'] and \
        data['submitted_answers']['starter-lines'] != []
    submission_lines_data_available = 'submission-lines' in data['submitted_answers'] and \
        data['submitted_answers']['submission-lines'] != []

    if starter_lines_data_available or submission_lines_data_available:
        start_lines = data['submitted_answers']['starter-lines'] if starter_lines_data_available else []
        scrambled_lines, solution_lines = parse.old_state(
            lang, start_lines, data['submitted_answers']['submission-lines'] )
    else:
        source_lines, given_lines = parse.get_scrambled_and_given(lang, indent_size=4)
        scrambled_lines = source_lines.copy()
        solution_lines = given_lines.copy()

        if format in ("right", "bottom", "no_code", ):
            random.shuffle(scrambled_lines)
        if format in ("no_code", ):
            random.shuffle(solution_lines)

    scrambled = { "lines" : scrambled_lines, "answers_name" : answers_name }
    given     = { "lines" : solution_lines , "answers_name" : answers_name }

    if format == "right":
        if pre_text or post_text:
            raise Exception("pre-text and post-text are not supported in right (horizontal) mode. " +
                'Add/set `format="bottom"` or `format="no-code"` to your element to use this feature.')
        size = "narrow"
    elif format == "bottom":
        size = "wide"
    elif format == "no_code":
        size = "wide"
        given["lines"] = given['lines'] + scrambled['lines']
    
    scrambled[size] = {"non_empty" : "non_empty"}
    given    [size] = {"non_empty" : "non_empty"}

    if format != "no_code":
        html_params.update({
            "scrambled" : scrambled,
        })
    html_params.update({
        "given" : given
    })
    
    with open('pl-faded-parsons-question.mustache', 'r') as f:
        return chevron.render(f, html_params).strip()

def render_submission_panel(element_html, data):
    """Show student what they submitted"""
    html_params = {
        'code': get_student_code(element_html, data),
    }
    with open('pl-faded-parsons-submission.mustache', 'r') as f:
        return chevron.render(f, html_params).strip()


def render_answer_panel(element_html, data):
    """Show the instructor's reference solution"""
    html_params = {
        "solution_path": "solution",
    }
    with open('pl-faded-parsons-answer.mustache', 'r') as f:
        return chevron.render(f, html_params).strip()


#
# Main functions
#
def render(element_html, data):
    panel_type = data['panel']
    if panel_type == 'question':
        return render_question_panel(element_html, data)
    elif panel_type == 'submission':
        return render_submission_panel(element_html, data)
    elif panel_type == 'answer':
        return render_answer_panel(element_html, data)
    else:
        raise Exception(f'Invalid panel type: {panel_type}')


def parse(element_html, data):
    """Parse student's submitted answer (HTML form submission)"""
    # make an XML fragment that can be passed around to other PL functions,
    # parsed/walked, etc

    element = xml.fragment_fromstring(element_html)
    format = pl.get_string_attrib(element, "format", "right").replace("-", '_')

    def load_json_if_present(key: str, default=[]):
        if key in data['raw_submitted_answers']:
            return json.loads(data['raw_submitted_answers'][key])
        return default
    
    if format != "no_code":
        starter_lines = load_json_if_present('starter-code-order')
    submission_lines = load_json_if_present('parsons-solution-order')

    submission_code = "\n".join([
        line.get("content", "")
        for line in submission_lines
    ]) + "\n" 

    data['submitted_answers']['student-parsons-solution'] = submission_code
    if format != "no_code":
        data['submitted_answers']['starter-lines'] = starter_lines
    data['submitted_answers']['submission-lines'] = submission_lines

    # `element` is now an XML data structure - see docs for LXML library at lxml.de

    # only Python problems are allowed right now (lang MUST be "py")
    # lang = pl.get_string_attrib(element, 'language') # TODO: commenting is a stop gap for the pilot study, find a better solution

    file_name = pl.get_string_attrib(element, 'file-name', 'user_code.py')

    data['submitted_answers']['_files'] = [
        {
            "name": file_name,
            "contents": base64_encode(get_student_code(element_html, data))
        }
    ]

    # TBD do error checking here for other attribute values....
    # set data['format_errors']['elt'] to an error message indicating an error with the
    # contents/format of the HTML element named 'elt'
    return


def grade(element_html, data):
    """ Grade the student's response; many strategies are possible, but none are necessary.
        This is externally autograded by a custom library.
    """
    pass