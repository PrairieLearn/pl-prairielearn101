import sys
sys.path.insert(0, '/course/serverFilesCourse')
import scratch

def generate(data):
    pass

def parse(data):
    scratch.parse(data, 'scratch4.sb3')

def grade(data):
    score = 0
    correct_feedback = ''
    error_feedback = ''

    if 'sensing_askandwait' in data['submitted_answers']['blocks']:
        score += 0.34
        correct_feedback += 'You have an "ask and wait" block (sensing).<br>'
    else:
        error_feedback += 'You should have an "ask and wait" block (sensing).<br>'

    if 'sensing_answer' in data['submitted_answers']['blocks']:
        score += 0.33
        correct_feedback += 'You have an "answer" block (sensing).<br>'
    else:
        error_feedback += 'You should have an "answer" block (sensing).<br>'

    if 'operator_join' in data['submitted_answers']['blocks']:
        score += 0.33
        correct_feedback += 'You have a "join" block (operators).<br>'
    else:
        error_feedback += 'You should have a "join" block (operators).<br>'

    data['feedback']['correct'] = correct_feedback
    data['feedback']['error'] = error_feedback
    data['score'] = score
