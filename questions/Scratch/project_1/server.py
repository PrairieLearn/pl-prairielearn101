import sys
sys.path.insert(0, '/course/serverFilesCourse')
import scratch

def generate(data):
    pass

def parse(data):
    scratch.parse(data, 'scratch1.sb3')

def grade(data):
    score = 0
    correct_feedback = ''
    error_feedback = ''

    # look for two stages
    if len(data['submitted_answers']['stages']) >= 2:
        score += 0.25
        correct_feedback += 'You have two stages.<br>'
    else:
        error_feedback += 'We expected two stages.<br>'

    # look for three sprite
    if len(data['submitted_answers']['sprites']) >= 3:
        score += 0.75
        correct_feedback += 'You have three sprites.<br>'
    else:
        error_feedback += 'We expected three sprites.<br>'
        
    data['feedback']['correct'] = correct_feedback
    data['feedback']['error'] = error_feedback
    data['score'] = score
