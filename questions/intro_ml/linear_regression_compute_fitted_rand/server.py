import random, copy
import numpy as np

def generate(data):

    size = np.random.randint(3, 6)
    w = np.random.randint(-10, 10, size=(size,))
    x = np.random.randint(-3, 3, size=(size-1,))
    yhat = np.dot(w, np.insert(x, 0, 1))
    
    data['params']['w'] = w.tolist()
    data['params']['x'] = x.tolist()
    
    
    # Put the result into data['correct_answers']
    data['correct_answers']['yhat'] = int(yhat)
