import random, copy

def grade(data):
    #print(data['submitted_answers'])
    data['partial_scores']['annotate-image'] = 0
    for element in data['submitted_answers']['annotate-image']:
        if 'placed_by_user' in element:
            if (268 <= element['x1'] <= 282) and  (268 <= element['x2'] <= 282):
                data['partial_scores']['annotate-image'] += 0.5
            if (202 <= element['x1'] <= 218) and  (202 <= element['x2'] <= 218):
                data['partial_scores']['annotate-image'] += 0.5
    data['score'] =  data['partial_scores']['annotate-image']

def generate(data):
    pass