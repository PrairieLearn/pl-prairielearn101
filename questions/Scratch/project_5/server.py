import sys
sys.path.insert(0, '/course/serverFilesCourse')
import scratch

def generate(data):
    pass

def parse(data):
    scratch.parse(data, 'scratch5.sb3')

def grade(data):
    score = 0
    correct_feedback = ''
    error_feedback = ''

    if 'control_if' in data['submitted_answers']['blocks']:
        score += 0.5
        correct_feedback += 'You have an "if" block (control).<br>'
    else:
        error_feedback += 'You should have an "if" block (control).<br>'

    if 'control_if_else' in data['submitted_answers']['blocks']:
        score += 0.5
        correct_feedback += 'You have an "if-else" block (control).<br>'
    else:
        error_feedback += 'You should have an "if-else" block (control).<br>'
        
    data['feedback']['correct'] = correct_feedback
    data['feedback']['error'] = error_feedback
    data['score'] = score
