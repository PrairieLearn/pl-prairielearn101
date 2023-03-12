import random, copy
import numpy as np

def generate(data):

    size = np.random.randint(3, 6)
    w = np.random.randint(-10, 10, size=(size,))
    x = np.random.randint(1, 5, size=(size-1,))
    x_trans = np.log(x)
    yhat = np.dot(w, np.insert(x_trans, 0, 1))
    
    data['params']['w'] = w.tolist()
    data['params']['x'] = x.tolist()
    
    
    # Put the result into data['correct_answers']
    data['correct_answers']['yhat'] = float(yhat)
