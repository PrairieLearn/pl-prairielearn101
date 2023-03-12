import random, copy
import prairielearn as pl
import ece6143
import numpy as np



def generate(data):
    
    data['params']['colors'] = ece6143.solarized_colors()
    X =  np.array( [ [1,1], [2.5, 2.5], [4, 5], [3, 1.5], [5, 4], [6,6]]  )
    y =   ["violet", "violet", "violet", "blue", "blue", "blue"]  
    

    data['params']['data-dict'] = [{'x': float(50*X[i,0]), 'y': float(40*X[i, 1]+50), 'color':  data['params']['colors'][ y[i] ] } for i in range(len(y))]

