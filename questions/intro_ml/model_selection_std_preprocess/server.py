import random


def generate(data):
    data['params']['use_sklearn'] = random.choice([True, False])