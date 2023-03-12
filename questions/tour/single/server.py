import random, copy

def grade(data):
    if data['submitted_answers']['guess'] > data['params']['val']:
        data['feedback']['number'] = "Your guess is too high."
    elif data['submitted_answers']['guess'] < data['params']['val']:
        data['feedback']['number'] = "Your guess is too low."

def generate(data):

    elems = random.sample(range(100), 4)
    data['params']['val'] = random.randint(1,10)