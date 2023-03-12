import random, copy
import prairielearn as pl
import ece6143
import numpy as np

def grade(data):

    for c in ['mean-line', 'regression-line', 'negative-line']:
        data['partial_scores'][c] = {'score': 0}
                    
    if 'mean-line' in data['submitted_answers']:
        for item in data['submitted_answers']['mean-line']:
            if 'placed_by_user' in item and item['placed_by_user']==1:
                if   abs(item['y2'] - item['y1']) <= 10 and abs(item['y2'] - data['params']['ml']['y1']) <= 50:
                    data['partial_scores']['mean-line']['score'] = 1
                else:
                    data['partial_scores']['mean-line']['score'] = 0

    if 'regression-line' in data['submitted_answers']:
        for item in data['submitted_answers']['regression-line']:
            if 'placed_by_user' in item and item['placed_by_user']==1:
                if   item['y2'] > item['y1'] and data['params']['coef']<0: # negative slope
                    data['partial_scores']['regression-line']['score'] = 1
                elif item['y2'] < item['y1'] and data['params']['coef']>0: # positive slope
                    data['partial_scores']['regression-line']['score'] = 1
                else:
                    data['partial_scores']['regression-line']['score'] = 0

    if 'negative-line' in data['submitted_answers']:
        for item in data['submitted_answers']['negative-line']:
            if 'placed_by_user' in item and item['placed_by_user']==1:
                if   item['y2'] > item['y1'] and data['params']['coef']>0: # negative slope
                    data['partial_scores']['negative-line']['score'] = 1
                elif item['y2'] < item['y1'] and data['params']['coef']<0: # positive slope
                    data['partial_scores']['negative-line']['score'] = 1
                else:
                    data['partial_scores']['negative-line']['score'] = 0

    for c in ['mean-line', 'regression-line', 'negative-line']:
        if data['partial_scores'][c]['score'] == 1:
            data['feedback'][c + '-badge'] = '<span class="badge badge-success">100%</span><br>'
        if data['partial_scores'][c]['score'] == 0:
            data['feedback'][c + '-badge'] = '<span class="badge badge-danger">0%</span><br>'

    
    data['score'] = sum([ data["partial_scores"][c]['score'] for c in  data["partial_scores"].keys() ])/len(data["partial_scores"].keys())



def generate(data):
    
    data['params']['colors'] = ece6143.solarized_colors()
    n = 30
    coef = random.choice([random.uniform(-3,-0.75), random.uniform(0.75,3)])
    intercept = random.uniform(-1,1)
    data['correct_answers']['intercept'] = intercept
    X, y = ece6143.generate_linear_regression_data(n=n, sigma=0.5, coef=[-coef], intercept=-1*intercept)
    
    data['params']['coef'] = coef
    data['params']['data-dict'] = [{'x': 200*X[i,0]+200, 'y': 50*y[i]+200} for i in range(n)]
    data['params']['rl'] = {'x1': 0, 'x2': 400, 'y1': 200+(50*coef-50*intercept), 'y2': 200+(-50*coef-50*intercept)}
    data['params']['ml'] = {'x1': 0, 'x2': 400, 'y1': 200+(50*np.mean(y)), 'y2': 200+(50*np.mean(y))}
    data['params']['nl'] = {'x1': 0, 'x2': 400, 'y2': 200+(50*coef-50*intercept), 'y1': 200+(-50*coef-50*intercept)}
    data['correct_answers']['coef'] = coef
