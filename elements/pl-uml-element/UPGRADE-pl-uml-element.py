import json
import randomgeneration as rg
import randomgrader as grader
import chevron
import lxml.html
import prairielearn as pl
import random

# Initialize Global Parameters
RANDOMIZED_QUESTION = False
FEEDBACK = True
MARKERFEEDBACK = False
MAX_GRADE = 10

# Marking Weights
MARKING_WEIGHTS = {
    'ENTITY_NAME': 0.2,
    'ENTITY_ATTRIBUTES': 0.1,
    'ENTITY_KEY': 0.2,
    'EXTRA_ENTITY_PENALTY': 0.25,
    'WEAK_ENTITY': 0.5,
    'RELATIONSHIP': 0.5,
    'CARDINALITY': 0.25,
    'EXTRA_RELATIONSHIP_PENALTY': 0.25,
}


def prepare(element_html, data):
    try:
        element = lxml.html.fragment_fromstring(element_html)
        handle_preparation(element, data)
    except Exception as e:
        print(f"Error in prepare(): {e}")


def handle_preparation(element, data):
    randomized_question = pl.get_boolean_attrib(element, 'random', RANDOMIZED_QUESTION)
    data['params']['oldAnswer'] = None
    data['params']['feedback'] = None
    data['params']['answer'] = []

    if not randomized_question:
        setup_question(element, data)
        setup_answer(element, data)
    else:
        setup_random_question(data)


def setup_random_question(data):
    question = rg.generate_random(data)
    data['params']['question_data'] = question['question']
    data['params']['answer'] = [{"answer": question['answer']}]


def setup_question(element, data):
    for child in element:
        is_question = (child.tag in ['uml-question', 'uml_question'])
        if is_question:
            data['params']['question_data'] = pl.inner_html(child)


def setup_answer(element, data):
    for child in element:
        is_answer = (child.tag in ['uml-answer', 'uml_answer'])
        if is_answer:
            data['params']['answer'].append({"answer": (pl.inner_html(child))})


def setup_marking(element, data):
    try:
        for attr, default_value in MARKING_WEIGHTS.items():
            MARKING_WEIGHTS[attr] = pl.get_float_attrib(element, attr.lower().replace('_', '-'), default_value)
        
        maximum_grade = pl.get_float_attrib(element, 'max-grade', MAX_GRADE)
        grader.setMaxGrade(maximum_grade)
        grader.setMarkingCriteria(**MARKING_WEIGHTS)
        
        return maximum_grade
    except Exception as e:
        print(f"Error in setup_marking(): {e}")


def render(element_html, data):
    try:
        element = lxml.html.fragment_fromstring(element_html)
        handle_rendering(element, data)
    except Exception as e:
        print(f"Error in render(): {e}")


def handle_rendering(element, data):
    give_feedback = pl.get_boolean_attrib(element, 'feedback', FEEDBACK)
    final_feedback = pl.get_boolean_attrib(element, 'marker-feedback', MARKERFEEDBACK)
    data['params']['oldAnswer'] = data['submitted_answers'].get('c', '')

    if data['panel'] == 'question':
        render_question(data)
    elif data['panel'] == 'submission':
        render_submission(data, give_feedback)
    elif data['panel'] == 'answer':
        render_answer(data, final_feedback)


def render_question(data):
    html_params = {'question_data': data['params']['question_data'], 'oldAnswer': data['params']['oldAnswer']}
    with open('uml-element.mustache', 'r', encoding='utf-8') as f:
        return chevron.render(f, html_params).strip()


def render_submission(data, give_feedback):
    feedback = ''
    if give_feedback:
        feedback = data['partial_scores']['uml_answer'].get('feedback', '')
    html_params = {'submission': True, 'feedback': feedback, 'oldAnswer': data['params']['oldAnswer']}
    with open('uml-submission.mustache', 'r', encoding='utf-8') as f:
        return chevron.render(f, html_params).strip()


def render_answer(data, final_feedback):
    marker_feedback = ''
    if final_feedback:
        marker_feedback = data['partial_scores']['uml_answer'].get('marker_feedback', '')
    html_params = {'answer': True, 'finalFeedback': marker_feedback, 'oldAnswer': data['params']['oldAnswer']}
    with open('uml-answer.mustache', 'r', encoding='utf-8') as f:
        return chevron.render(f, html_params).strip()


def grade(element_html, data):
    try:
        maximum_grade = setup_marking(element_html, data)
        handle_grading(data, maximum_grade)
    except Exception as e:
        print(f"Error in grade(): {e}")


def handle_grading(data, maximum_grade):
    graded_question = grader.grade_question(data)
    score = graded_question['params']['score']
    feedback = graded_question['params']['feedback']
    marker_feedback = graded_question['params']['marker_feedback']

    data['params']['feedback'] = feedback
    data['partial_scores']['uml_answer'] = {
        'score': score,
        'weight': maximum_grade,
        'feedback': feedback,
        'marker_feedback': marker_feedback
    }
