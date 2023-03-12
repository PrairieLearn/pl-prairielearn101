import random, copy

def grade(data):
    keylist = ['var-line']
    for k in keylist:
        if k in data['partial_scores']:
            if data['partial_scores'][k]['score'] == 1:
                data['feedback'][k + '-badge'] = '<span class="badge badge-success">100%</span>'
            elif data['partial_scores'][k]['score'] == 0:
                data['feedback'][k + '-badge'] = '<span class="badge badge-danger">0%</span>'
            else:
                data['feedback'][k + '-badge'] = '<span class="badge badge-warning">' + str(int(data['partial_scores'][k]['score']*100)) + '%</span>'

def generate(data):

    # Sample two random integers between 5 and 10 (inclusive)
    a = random.randint(5, 10)
    b = random.randint(5, 10)

    # Put these two integers into data['params']
    data['params']['a'] = a
    data['params']['b'] = b

    # Compute the sum of these two integers
    c = a + b

    # Put the sum into data['correct_answers']
    data['correct_answers']['c'] = c
