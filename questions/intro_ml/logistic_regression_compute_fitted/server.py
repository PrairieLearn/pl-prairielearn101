import random, copy
import numpy as np

def generate(data):

    size = np.random.randint(3, 6)
    w = np.random.randint(-10, 10, size=(size,))
    x = np.random.randint(-3, 3, size=(size-1,))/10
    yhat = np.dot(w, np.insert(x, 0, 1))
    
    data['params']['w'] = w.tolist()
    data['params']['x'] = x.tolist()

    z = np.dot(w, np.concatenate( ([1],x)) )
    data['params']['z'] = float(round(z, 9))
    data['correct_answers']['prob'] = float(round(1/(1 + np.exp(-1*z)), 9))

    data['params']['threshold'] = float(round(np.random.uniform(0.2, 0.8), 2))
    # don't let it be too ambiguous
    while abs(data['params']['threshold'] - data['correct_answers']['prob'] ) < 0.02:
        data['params']['threshold'] = float(round(np.random.uniform(0.2, 0.8), 2))

    data['params']['isPos'] = bool(data['correct_answers']['prob'] >  data['params']['threshold'])
    data['params']['isNeg'] = bool(data['correct_answers']['prob'] <  data['params']['threshold'])
