import sys

def generate(data):
    pass

def parse(data):
    sys.path.insert(0, data['options']['server_files_course_path'])
    import scratch
    scratch.parse(data, 'scratch7.sb3')

def grade(data):
    score = 0
    correct_feedback = ''
    error_feedback = ''

    varCount = len(data['submitted_answers']['variables'])
    if varCount > 0:
        score += 1
        correct_feedback += f'You have {varCount} variables.<br>'
    else:
        error_feedback += 'You should have at least one variable.<br>'
        
    data['feedback']['correct'] = correct_feedback
    data['feedback']['error'] = error_feedback
    data['score'] = score
