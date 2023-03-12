import random, copy

def grade(data):
    
    # accept any positive number of hidden units
    if data["submitted_answers"]["hidden"] > 0:
        data['correct_answers']['hidden'] = data["submitted_answers"]["hidden"]
        data["partial_scores"]['hidden']["score"]=1
    # accept any valid hidden unit activation function
    if data["submitted_answers"]["act-hidden"] in ['a','b','c']:
        data["partial_scores"]['act-hidden']["score"]=1
        if data["submitted_answers"]["act-hidden"] == 'a':
            data['correct_answers']['act-hidden'] = {'key': 'a', 'html': 'relu', 'feedback': None}
        elif data["submitted_answers"]["act-hidden"] == 'b':
            data['correct_answers']['act-hidden'] = {'key': 'b', 'html': 'sigmoid', 'feedback': None}
        elif data["submitted_answers"]["act-hidden"] == 'c':
            data['correct_answers']['act-hidden'] = {'key': 'c', 'html': 'tanh', 'feedback': None}

    data['score'] = sum([data["partial_scores"][c]['weight']*data["partial_scores"][c]['score'] for c in data["partial_scores"].keys()])/sum([data["partial_scores"][c]['weight'] for c in data["partial_scores"].keys()])


def generate(data):
    
    data['params']['dims'] = random.choice([(200, 100), (180, 90), (320, 200), (86, 64)])
    data['params']['pixels'] = 3*data['params']['dims'][0]*data['params']['dims'][1]

