import random


def generate(data):
    data['params'] = random.choice([
        {'scenario': "translate user-supplied text from one language to another", 'approach': "ask users for explicit feedback on each translation (thumbs up or thumbs down)",
        'correct': ["The response rate is likely to be low", "The user may not be a reliable judge of whether the prediction is good or not"],
        'incorrect': [""]
        ])