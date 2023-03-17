import random, copy

def generate(data):

    elems = random.sample(range(100), 4)
    data['params']['vals'] = [{'value': e, 'ans': 'true'} if e==min(elems) else {'value': e, 'ans': 'false'} for e in elems]