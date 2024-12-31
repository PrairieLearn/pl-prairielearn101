import sys
sys.path.insert(0, '/course/serverFilesCourse')
import scratch

def generate(data):
    pass

def parse(data):
    scratch.parse(data, 'scratch2.sb3')

def grade(data):
    score = 0
    correct_feedback = ''
    error_feedback = ''

    if 'motion' in data['submitted_answers']['blocks']:
        score += 0.34
        correct_feedback += 'You have a "motion" block.<br>'
    else:
        error_feedback = 'We expected a "motion" block to be used.<br>'

    if 'looks' in data['submitted_answers']['blocks']:
        score += 0.33
        correct_feedback += 'You have a "looks" block.<br>'
    else:
        error_feedback += 'We expected a "looks" block to be used.<br>'

    if 'sound' in data['submitted_answers']['blocks']:
        score += 0.33
        correct_feedback += 'You have a "sound" block.<br>'
    else:
        error_feedback += 'We expected a "sound" block to be used.<br>'
        
    data['feedback']['correct'] = correct_feedback
    data['feedback']['error'] = error_feedback
    data['score'] = score
