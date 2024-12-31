import sys
sys.path.insert(0, '/course/serverFilesCourse')
import scratch

def generate(data):
    pass

def parse(data):
    scratch.parse(data, 'scratch8.sb3')

def grade(data):
    score = 0
    correct_feedback = ''
    error_feedback = ''

    if 'procedures_definition' in data['submitted_answers']['blocks']:
        score += 1
        correct_feedback += 'You have a custom block.<br>'
    else:
        error_feedback += 'You should have a custom block.<br>'
        
    data['feedback']['correct'] = correct_feedback
    data['feedback']['error'] = error_feedback
    data['score'] = score
