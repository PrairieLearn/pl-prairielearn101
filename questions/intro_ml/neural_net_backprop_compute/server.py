import random, copy
import math
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import io
import random, copy

def sigmoid(z):
    return 1/(1+np.exp(-z))
    
def sigmoidPrime(z):
    # derivative of sigmoid function
    return np.exp(-z)/((1+np.exp(-z))**2)

def file(data):

    if data['filename']=='figure.png':
        
        X = np.array([[0,1]])
        y = np.array([[1]])
        
        inputLayerSize  = X.shape[1]
        outputLayerSize = y.shape[1]
        hiddenLayerSize = 2
        
        nodePos = {}
        G=nx.Graph()
        graphHeight = max(inputLayerSize, outputLayerSize, hiddenLayerSize)
        
        # create nodes and note their positions
        for n in range(inputLayerSize):
          nodePos['x'+str(n+1)]=(1, n)
          G.add_node('x'+str(n+1))
        for n in range(outputLayerSize):
          nodePos['o'+str(n+1)]=(5, n)
          G.add_node('o'+str(n+1))
        for n in range(hiddenLayerSize):
          nodePos['h'+str(n+1)]=(3, n)
          G.add_node('h'+str(n+1))
        
        # add edges
        for n in range(hiddenLayerSize):
          for m in range(inputLayerSize):
            G.add_edge('x' + str(m+1), 'h' + str(n+1))
          for m in range(outputLayerSize):
            G.add_edge('h' + str(n+1), 'o' + str(m+1))
        nodePos['xb']=(1, inputLayerSize)
        G.add_node('xb')
        for n in range(hiddenLayerSize):
          G.add_edge('xb', 'h' + str(n+1))
        
        nodePos['hb']=(3, hiddenLayerSize)
        G.add_node('hb')
        for n in range(outputLayerSize):
          G.add_edge('hb', 'o' + str(n+1))
        
        plt.figure(figsize=(7,5));
        nx.draw_networkx(G, pos=nodePos, 
                         node_size=1000, node_color='pink')
        
        labels = nx.get_edge_attributes(G,'weight')
        nx.draw_networkx_edge_labels(G,nodePos,edge_labels=labels)
        
        edge_labels={
            ('x1', 'h1'): data['params']['w']['x1-h1'], ('x1', 'h2'): data['params']['w']['x1-h2'], ('x2', 'h1'): data['params']['w']['x2-h1'], ('x2', 'h2'): data['params']['w']['x2-h2'], 
            ('h1', 'o1'): data['params']['w']['h1-o1'], ('h2', 'o1'): data['params']['w']['h2-o1'], ('hb', 'o1'): data['params']['w']['hb-o1'], ('xb', 'h1'): data['params']['w']['xb-h1'], ('xb', 'h2'): data['params']['w']['xb-h2']
        }
        
        
        nx.draw_networkx_edge_labels(G,nodePos,edge_labels=edge_labels, 
                                  rotate=False, label_pos=0.22);

        # Save the figure and return it as a buffer
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        return buf

def generate(data):

    lr = random.choice([0.2, 0.3, 0.4])
    data['params']['lr'] = lr
    #w = {'xb-h2': 2, 'x2-h2': -3, 'x1-h2': -1.5,
    #                       'xb-h1': 1.5, 'x2-h1': 1, 'x1-h1': 2.5,
    #                       'hb-o1': -1, 'h2-o1': 0.5, 'h1-o1': 1}
    w = {'xb-h2': random.choice([1,2,3]), 'x2-h2': random.choice([-1, -2, -3, -4]), 'x1-h2': random.choice([-0.5, -1.5, -2.5]),
                           'xb-h1': random.choice([0.5, 1.5, 2.5]), 'x2-h1': random.choice([1,2,3]), 'x1-h1': random.choice([1.5, 2.5]),
                           'hb-o1': random.choice([-1, -2]), 'h2-o1': random.choice([-1, -0.5, 0.5, 1]), 'h1-o1': random.choice([1,2])}

    input = {'xb': 1, 'x2': 1, 'x1': 0, 'y': 1}

    z_h1 = w['x1-h1']*input['x1'] + w['x2-h1']*input['x2'] + w['xb-h1']*input['xb']
    z_h2 = w['x1-h2']*input['x1'] + w['x2-h2']*input['x2'] + w['xb-h2']*input['xb']

    u_h1 = sigmoid(z_h1)
    u_h2 = sigmoid(z_h2)
    
    
    z_o1 = w['h1-o1']*u_h1 + w['h2-o1']*u_h2 + w['hb-o1']*1
    u_o1 = sigmoid(z_o1)

    data['params']['w'] = w
    data['params']['input'] = input

    data['correct_answers']['fwd-h1'] = u_h1
    data['correct_answers']['fwd-h2'] = u_h2
    data['correct_answers']['fwd-o1'] = u_o1
    
    delta_o1 = -1*(input['y'] - u_o1)*sigmoidPrime(z_o1)
    data['correct_answers']['bp-o1'] = delta_o1
    data['correct_answers']['bp-h1'] = w['h1-o1']*delta_o1*sigmoidPrime(z_h1)
    data['correct_answers']['bp-h2'] = w['h2-o1']*delta_o1*sigmoidPrime(z_h2)
    
    
    grad_o = data['correct_answers']['bp-o1']*np.array([u_h1, u_h2, 1 ])
    data['correct_answers']['grad-o'] =  grad_o.reshape(1, -1).tolist()

    grad_h1 = data['correct_answers']['bp-h1']*np.array([input['x1'], input['x2'], 1 ])
    grad_h2 = data['correct_answers']['bp-h2']*np.array([input['x1'], input['x2'], 1 ])
    data['correct_answers']['grad-h1'] =  grad_h1.reshape(1, -1).tolist()
    data['correct_answers']['grad-h2'] =  grad_h2.reshape(1, -1).tolist()

    new_o =  np.array([w['h1-o1'], w['h2-o1'], w['hb-o1']]) - lr*grad_o
    data['correct_answers']['new-o'] = new_o.reshape(1, -1).tolist()
    
    new_h1 =  np.array([w['x1-h1'], w['x2-h1'], w['xb-h1']]) - lr*grad_h1
    data['correct_answers']['new-h1'] = new_h1.reshape(1, -1).tolist()
    
    new_h2 =  np.array([w['x1-h2'], w['x2-h2'], w['xb-h2']]) - lr*grad_h2
    data['correct_answers']['new-h2'] = new_h2.reshape(1, -1).tolist()
