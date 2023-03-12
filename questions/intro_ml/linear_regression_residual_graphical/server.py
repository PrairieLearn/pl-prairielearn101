import random, copy
import prairielearn as pl
import ece6143
import numpy as np

def grade(data):
    keylist = ['var-line', 'mse-line', 'expl-line']
    for k in keylist:
        if k in data['partial_scores']:
            if data['partial_scores'][k]['score'] == 1:
                data['feedback'][k + '-badge'] = '<span class="badge badge-success">100%</span>'
            elif data['partial_scores'][k]['score'] == 0:
                data['feedback'][k + '-badge'] = '<span class="badge badge-danger">0%</span>'
            else:
                data['feedback'][k + '-badge'] = '<span class="badge badge-warning">' + str(int(data['partial_scores'][k]['score']*100)) + '%</span>'

def generate(data):
    
    data['params']['colors'] = ece6143.solarized_colors()
    n = 30
    coef = random.choice([random.uniform(-3,-0.75), random.uniform(0.75,3)])
    intercept = random.uniform(-1,1)
    data['correct_answers']['intercept'] = intercept
    X, y = ece6143.generate_linear_regression_data(n=n, sigma=0.7, coef=[-coef], intercept=-1*intercept)

    # add a point
    x_sel = 0.5
    y_sel_true = -1*coef*x_sel - intercept
    y_sel = y_sel_true - np.sign(coef)*np.random.uniform(0.8, 1.5)

    data['params']['data-sel'] =  {'x': 200*x_sel+200, 'y': 50*y_sel+200}

    data['params']['vl'] = {'x1': 200*x_sel+200, 'x2': 200*x_sel+200, 'y1': 200+(50*np.mean(y)), 'y2': 200+(50*y_sel)}
    data['params']['el'] = {'x1': 200*x_sel+200, 'x2': 200*x_sel+200, 'y1': 200+(50*y_sel_true), 'y2': 200+(50*y_sel)}
    data['params']['expl'] = {'x1': 200*x_sel+200, 'x2': 200*x_sel+200, 'y1': 200+(50*np.mean(y)),'y2': 200+(50*y_sel_true)}

    
    data['params']['coef'] = coef
    data['params']['data-dict'] = [{'x': 200*X[i,0]+200, 'y': 50*y[i]+200} for i in range(n)]
    data['params']['rl'] = {'x1': 0, 'x2': 400, 'y1': 200+(50*coef-50*intercept), 'y2': 200+(-50*coef-50*intercept)}
    data['params']['ml'] = {'x1': 0, 'x2': 400, 'y1': 200+(50*np.mean(y)), 'y2': 200+(50*np.mean(y))}


    data['correct_answers']['coef'] = coef
