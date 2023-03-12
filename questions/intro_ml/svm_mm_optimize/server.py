import random, copy
import prairielearn as pl
import ece6143
import numpy as np
import sympy
import prairielearn as pl


def parse(data):
    
    if 'w_0' in data['submitted_answers'] and 'w_1' in data['submitted_answers'] and 'w_2' in data['submitted_answers']:

        w_2 = data['submitted_answers']['w_2']
        w_1 = data['submitted_answers']['w_1']
        w_0 = data['submitted_answers']['w_0']

        if isinstance(w_2, (int, float)) and isinstance(w_1, (int, float)) and isinstance(w_0, (int, float)) and w_2 != 0:

            data['submitted_answers']['w_0'] = 3*w_0/w_2
            data['submitted_answers']['w_1'] = 3*w_1/w_2
            data['submitted_answers']['w_2'] = 3*w_2/w_2

        
def grade(data):
    """
    angle_tol = 5
    width_tol = 10
    
    if 'mm' in data['submitted_answers']:
        score_line = data['partial_scores']['mm']['score']
        score_rect = 0
        
        for item in data['submitted_answers']['mm']:
            if 'placed_by_user' in item and item['placed_by_user']==1 and item['gradingName']=="pl-rectangle":
                if (abs(data['params']['angle'] - item['angle']) <= angle_tol) or (abs(data['params']['angle'] - (item['angle']-180)) <= angle_tol):
                    if (abs(data['params']['margin-width'] - item['width']) <= width_tol) or (abs(data['params']['margin-width'] - item['height']) <= width_tol):
                        score_rect = 1


        data['partial_scores']['mm']['score'] = 0.5*score_line + 0.5*score_rect
    
    for c in ['mm']:
        if data['partial_scores'][c]['score'] == 1:
            data['feedback'][c + '-badge'] = '<span class="badge badge-success">100%</span><br>'
        elif data['partial_scores'][c]['score'] == 0:
            data['feedback'][c + '-badge'] = '<span class="badge badge-danger">0%</span><br>'
        else:
            data['feedback'][c + '-badge'] = '<span class="badge badge-warning">' + str(round(data['partial_scores']['mm']['score']*100)) + '%</span><br>'
            
    data['score'] = sum([ data["partial_scores"][c]['score'] for c in  data["partial_scores"].keys() ])/len(data["partial_scores"].keys())
    """
    pass

def generate(data):
    
    alpha1, alpha2, alpha = sympy.symbols('alpha_1 alpha_2 alpha')

    data['params']['colors'] = ece6143.solarized_colors()
    X =  np.array( [ [-2, 4], [-1,1],  [0, 0], [1, 1], [-3, 9], [3, 9]]  )
    y =   ["blue", "red",  "red", "red", "blue", "blue"]  
    y_int = [1, -1,  -1, -1, 1, 1]
    
    data['params']['margin-width'] = 56.568
    data['params']['angle'] = 45
    data['params']['data-dict'] = [{'i': i+1, 'x': float(40*X[i,0]+200), 'y': float(-40*X[i, 1]+400), 'color':  data['params']['colors'][ y[i] ] } for i in range(len(y))]
    data['params']['samples'] = [{'i': i+1, 'x1': int(X[i,0]), 'x2': int(X[i,1]), 'y': y[i], 'y_int': y_int[i] } for i in range(len(y))]

    data['correct_answers']['objective'] = pl.to_json(alpha1 + alpha2 - (10*alpha1**2 - 6*alpha1*alpha2 + alpha2**2) )
    data['correct_answers']['constraint'] = pl.to_json( 2*alpha - 5*alpha**2 )
    data['correct_answers']['derivative'] = pl.to_json( 2 - 10*alpha )
    data['correct_answers']['w0star'] = -9/5
    data['correct_answers']['w1star'] = -1/5
    data['correct_answers']['w2star'] =  3/5
    data['correct_answers']['alpha'] =  1/5
