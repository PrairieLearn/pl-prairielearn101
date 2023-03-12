import random, copy

def grade(data):
    
    data['score'] = 1

    if '_files' in data['submitted_answers']:
        for f in data['submitted_answers']['_files']:
            if f['name']=="plot.png":
                data['submitted_answers']['raw_image']=f['contents']


def generate(data):
    pass