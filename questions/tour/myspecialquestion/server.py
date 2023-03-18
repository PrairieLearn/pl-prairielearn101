import random, copy
import prairielearn as pl

def generate(data):
    
    data['params']['random_number'] = random.randint(0,500)
    data['params']['random_number_hint'] = data['params']['random_number']  / 2
