import random, copy
import numpy as np
import matplotlib.pyplot as plt
import io, base64
from sklearn.metrics import mean_squared_error
import prairielearn as pl

def sigmoid(z):
    return 1/(1+np.exp(-z))

def forward_pass(x, w):
    input = {'xb': 1, 'x1': x}
    z_h1 = w['x1-h1']*input['x1'] + w['xb-h1']*input['xb']
    z_h2 = w['x1-h2']*input['x1']  + w['xb-h2']*input['xb']
    u_h1 = sigmoid(z_h1)
    u_h2 = sigmoid(z_h2)
    z_o1 = w['h1-o1']*u_h1 + w['h2-o1']*u_h2 + w['hb-o1']*1
    u_o1 = z_o1

    return u_o1

def grade(data):
    
    for k in data['partial_scores'].keys():
        data["partial_scores"][k] = {}

    outputs_sub = forward_pass(np.array(data['params']['inputs']), data["submitted_answers"])
    mse = mean_squared_error(outputs_sub, np.array(data['params']['outputs']))

    data['feedback']['mse'] = round(mse, 5)
    if mse < 0.01:
        data['score'] = 1
    else:
        data['score'] = 0

    data['feedback']['submit_str'] = ', '.join(map(str, outputs_sub))

    # prepare plot
    plt.plot(data['params']['inputs'], data['params']['outputs'], label='Function');
    plt.plot(data['params']['inputs'], outputs_sub, label='Network output');
    plt.xlabel("Input x");
    plt.ylabel("Output y");
    plt.grid();
    plt.legend();
    
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    data['feedback']['image_result'] = base64.b64encode(buf.getvalue()).decode('utf8')
    data['feedback']['has_image'] = True

    
def file(data):
    
    if data['filename']=='function.png':
        
        plt.plot(data['params']['inputs'], data['params']['outputs']);
        plt.xlabel("Input x");
        plt.ylabel("Output y");
        plt.grid();
        
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        return buf

    if data['filename']=='output.png':
        if 'submitted_answers' in data:
            outputs = forward_pass(np.array(data['params']['inputs']), data['submitted_answers'])
            plt.plot(data['params']['inputs'], outputs);
            plt.xlabel("Input x");
            plt.ylabel("Output y");
            
            buf = io.BytesIO()
            plt.savefig(buf, format='png')
            return buf
        else:
            buf = io.BytesIO()
            plt.savefig(buf, format='png')
            return buf


def generate(data):
    
    wt = random.choice([90, 100, 110])
    w = { 'xb-h1': random.choice([-10, -20, -30, -40]),  'xb-h2': random.choice([-60, -70, -80]),
                              'x1-h2': wt,
                               'x1-h1': wt,
                               'hb-o1': random.choice([-0.2, -0.4, -0.5]), 'h2-o1': random.choice([-0.8, -1.8, 0.8, 1.8]), 'h1-o1': random.choice([-0.4, -1.4, 0.4, 1.4])}

    inputs = np.linspace(0, 1, num=100)
    outputs = forward_pass(inputs, w)
    data['params']['inputs'] = inputs.tolist()
    data['params']['outputs'] = outputs.tolist()
    
    data['params']['input_str'] = ', '.join(map(str, data['params']['inputs']))
    data['params']['output_str'] = ', '.join(map(str, data['params']['outputs']))

    data['correct_answers'] = w