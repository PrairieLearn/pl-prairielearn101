import random, copy
import numpy as np
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
import prairielearn as pl


def generate(data):

    X, y = load_iris(return_X_y=True)
    np.random.shuffle(X)

    data['params']['nclass'] = 3
    w = np.array([[  9.8404,  -0.4188,   0.967 ,  -2.521 ,  -1.0842],
       [  2.217 ,   0.5312,  -0.3148,  -0.2001,  -0.9486],
       [-12.0574,  -0.1125,  -0.6523,   2.7211,   2.0328]])
    x = X[0]
    x_a = np.concatenate(([1], X[0]))

    probs = np.exp(np.sum(x_a*w, axis=1))/np.sum(np.exp(np.sum(x_a*w, axis=1)), axis=0)

    
    data['params']['w'] = pl.to_json(w)
    data['params']['x'] = pl.to_json(x)
    data['params']['probs'] = pl.to_json(probs)
    data['params']['correct'] = int(np.argmax(probs))
    data['correct_answers']['prob-0'] = float(probs[0])
    data['correct_answers']['prob-1'] = float(probs[1])
    data['correct_answers']['prob-2'] = float(probs[2])

    data['params']['class'] = [{'class': i, 'ans': data['params']['correct']==i} for i in range(data['params']['nclass'] )]