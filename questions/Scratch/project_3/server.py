import sys

def generate(data):
    pass

def parse(data):
    sys.path.insert(0, data['options']['server_files_course_path'])
    import scratch
    scratch.parse(data, 'scratch3.sb3')

def grade(data):
    count = 0
    for block in data['submitted_answers']['blocks']:
        if block == 'event':
            count += 1

    score = 0
    correct_feedback = ''
    error_feedback = ''

    if count >= 2:
        score = 1
        correct_feedback += 'You used at least two events.<br>'
    else:
        error_feedback += 'You should have at least two events.<br>'
        
    data['feedback']['correct'] = correct_feedback
    data['feedback']['error'] = error_feedback
    data['score'] = score
