import sys
sys.path.insert(0, '/course/serverFilesCourse')
import scratch

def generate(data):
    pass

def parse(data):
    scratch.parse(data, 'scratch6.sb3')

def grade(data):
    score = 0
    correct_feedback = ''
    error_feedback = ''

    if 'control_repeat' in data['submitted_answers']['blocks']:
        score += 0.5
        correct_feedback += 'You have a "repeat" block (control).<br>'
    else:
        error_feedback += 'You should have a "repeat" block (control).<br>'

    if 'control_forever' in data['submitted_answers']['blocks']:
        score += 0.5
        correct_feedback += 'You have a "forever" block (control).<br>'
    else:
        error_feedback += 'You should have a "forever" block (control).<br>'
        
    data['feedback']['correct'] = correct_feedback
    data['feedback']['error'] = error_feedback
    data['score'] = score
