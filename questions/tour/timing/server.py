import random, copy

def generate(data):

    elems = random.sample(range(100), 4)
    data['params']['val'] = random.randint(1,10)