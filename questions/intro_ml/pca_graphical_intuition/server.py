import random, copy
import prairielearn as pl
import ece6143
import numpy as np

import math

def correct_origin(left, top, angle, width):
    groupOffsetY = width + 2
    groupOffsetX = groupOffsetY / 2.0
    angle_rad = (math.pi / 180) * (360 - angle)
    correct_left = (left - groupOffsetX) + math.cos(angle_rad) * groupOffsetX + math.sin(angle_rad) * groupOffsetY
    correct_top = (top - groupOffsetY) + math.cos(angle_rad) * groupOffsetY - math.sin(angle_rad) * groupOffsetX
    return (correct_left, correct_top)

def grade(data):
    
    angle_tol = 10
    center_tol = 20
    
    for c in ['pca-coords']:
        data['partial_scores'][c] = {'score': 0}
                    
    if 'pca-coords' in data['submitted_answers']:
        data['partial_scores']['pca-coords']['score'] = 0
        for item in data['submitted_answers']['pca-coords']:
            if 'placed_by_user' in item and item['placed_by_user']==1:
                correct_left, correct_top = correct_origin( item['left'], item['top'], item['angle'], item['width']  )
                if any( [
                    ( abs(data['params']['mean-x1'] - correct_left) <= center_tol and abs(data['params']['mean-x2'] - correct_top) <= center_tol),
                    (  abs(data['params']['mean-x2'] - correct_left) <= center_tol and abs(data['params']['mean-x1'] - correct_top) <= center_tol )
                     ] ):
                    data['partial_scores']['pca-coords']['score'] += 0.5
                else:
                    data['feedback']['pca-center'] = '<br><span class="badge badge-info">Submission Feedback</span>  The origin of your new coordinate system should be in the center of the data.'
                if any( [
                        abs(data['params']['angle'] - item['angle']) <= angle_tol,
                        abs(data['params']['angle'] - (item['angle']-180)) <= angle_tol,
                        abs( (data['params']['angle']-180) - item['angle']) <= angle_tol
                        ] ):
                    data['partial_scores']['pca-coords']['score'] += 0.5
                else:
                    data['feedback']['pca-angle'] = '  <br><span class="badge badge-info">Submission Feedback</span>  The PC1 axis of your new coordinate system should point in the direction of greatest variance of the data.'

    for c in ['pca-coords']:
        if data['partial_scores'][c]['score'] == 1:
            data['feedback'][c + '-badge'] = '<span class="badge badge-success">100%</span><br>'
        elif data['partial_scores'][c]['score'] == 0:
            data['feedback'][c + '-badge'] = '<span class="badge badge-danger">0%</span><br>'
        else:
            data['feedback'][c + '-badge'] = '<span class="badge badge-warning">' + str(round(100*data['partial_scores']['pca-coords']['score'])) + '%</span><br>'

    
    data['score'] = sum([ data["partial_scores"][c]['score'] for c in  data["partial_scores"].keys() ])/len(data["partial_scores"].keys())


def generate(data):
    
    data['params']['colors'] = ece6143.solarized_colors()
    n = 50
    coef = random.choice([random.uniform(-3,-1.5), random.uniform(1.5,3)])
    intercept = random.uniform(-1,1)
    data['correct_answers']['intercept'] = intercept
    X, y = ece6143.generate_linear_regression_data(n=n, sigma=0.6, coef=[-coef], intercept=-1*intercept)
    
    data['params']['coef'] = coef
    data['params']['angle'] = (360-15*coef)%360
    data['params']['data-dict'] = [{'x': 200*X[i,0]+200, 'y': 50*y[i]+200} for i in range(n)]
    data['params']['mean-x1'] = 200*np.mean(X)+200
    data['params']['mean-x2'] = 50*np.mean(y)+200
    data['params']['rl'] = {'x1': 0, 'x2': 400, 'y1': 200+(50*coef-50*intercept), 'y2': 200+(-50*coef-50*intercept)}
    data['correct_answers']['coef'] = coef
