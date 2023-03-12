import random, copy
import numpy as np
import prairielearn as pl

from numpy.lib.stride_tricks import as_strided

# via https://stackoverflow.com/questions/65461409/convolutional-layer-in-python-using-numpy-with-strides
def conv2d(a, b, s=1):
    Hout = (a.shape[1] - b.shape[0]) // s + 1
    Wout = (a.shape[2] - b.shape[1]) // s + 1
    Stride = (a.strides[0], a.strides[1] * s, a.strides[2] * s, a.strides[1], a.strides[2], a.strides[3])
    a = as_strided(a, (a.shape[0], Hout, Wout, b.shape[0], b.shape[1], a.shape[3]), Stride)
    return np.tensordot(a, b, axes=3)
    
def generate(data):
    
    X0 = np.random.randint(-1,3, size=(5, 5))
    X1 = np.random.randint(-1,3, size=(5, 5))
    X2 = np.random.randint(-1,3, size=(5, 5))
    
    W0 = np.random.randint(-1,2, size=(3, 3))
    W1 = np.random.randint(-1,2, size=(3, 3))
    W2 = np.random.randint(-1,2, size=(3, 3))
    b0 = np.random.randint(-3, 3)
    
    
    V0 = np.random.randint(-1,2, size=(3, 3))
    V1 = np.random.randint(-1,2, size=(3, 3))
    V2 = np.random.randint(-1,2, size=(3, 3))
    b1 = np.random.randint(-3, 4)
    
    s = random.choice([2])
    
    """
    X0 = np.array([ [1,0,1,2,1], [0,0,2,2,2], [2,2,2,1,1], [1,0,0,2,2], [1,2,0,0,1]  ])
    X1 = np.array([ [1,0,1,2,1], [1,1,0,2,1], [0,1,2,1,2], [1,2,1,0,0], [0,0,0,1,1]  ])
    X2 = np.array([ [2,2,2,0,2], [2,2,0,0,2], [1,0,1,0,0], [2,1,0,0,1], [0,2,2,2,2]  ])
    
    W0 = np.array([ [-1,-1,-1], [1,1,-1], [-1,1,1] ])
    W1 = np.array([ [0,1,0], [-1,1,1], [-1,1,-1] ])
    W2 = np.array([ [0,1,1], [1,1,1], [-1,-1,1] ])
    
    V0 = np.array([ [1,1,-1], [0,0,0], [-1,0,0]])
    V1 = np.array([ [1,-1,-1], [1,-1,-1], [-1,0,1]])
    V2 = np.array([ [-1,1,-1], [0,1,0], [-1,-1,1]])
    
    b0 = 1
    b1 = 0
    s = 2
    """

    X0_p = np.pad(X0, 1, 'constant', constant_values=(0))
    X1_p = np.pad(X1, 1, 'constant', constant_values=(0))
    X2_p = np.pad(X2, 1, 'constant', constant_values=(0))
    
    
    data['params']['input_0'] = X0_p.tolist()
    data['params']['input_1'] = X1_p.tolist()
    data['params']['input_2'] = X2_p.tolist()
    
    
    data['params']['filter_0'] = W0.tolist()
    data['params']['filter_1'] = W1.tolist()
    data['params']['filter_2'] = W2.tolist()
    data['params']['bias_0'] = int(b0)
    
    data['params']['vilter_0'] = V0.tolist()
    data['params']['vilter_1'] = V1.tolist()
    data['params']['vilter_2'] = V2.tolist()
    data['params']['bias_1'] = int(b1)
    
    data['params']['stride'] = int(s)
    
    X_p = np.dstack([X0_p, X1_p, X2_p]).reshape((1,7,7,3))
    X   = np.dstack([X0, X1, X2]).reshape((1,5,5,3))
    W = np.stack(( np.dstack([W0, W1, W2]) ,  np.dstack([V0, V1, V2])), axis=3).reshape(3,3,3,2)
    b = np.array([b0, b1])
    
    c = conv2d(X_p, W, s)
    output_0 = c[0,:,:,0] + b0
    output_1 = c[0,:,:,1] + b1
    output = np.dstack([output_0, output_1])
    
    mask_0 = random.randint(0,3)
    mask_1 = random.randint(0,3)

    data['params']['output_0'] = output_0.tolist()
    data['params']['output_1'] = output_1.tolist()
    
    data['params']['output_0_tagged']  = [[{'show': True, 'value': int(output_0[i,j])} for j in range(3)] for i in range(3)]
    data['params']['output_0_tagged'][0][2]['show'] = False    

    data['params']['output_1_tagged']  = [[{'show': True, 'value': int(output_1[i,j])} for j in range(3)] for i in range(3)]
    data['params']['output_1_tagged'][1][1]['show'] = False    

    
    ###
    
    data['params']['exp_0_ip_0'] = pl.to_json(X0_p[:3, 4:])
    data['params']['exp_0_filter_0'] = pl.to_json(W0)
    data['params']['exp_0_prod_0'] = pl.to_json(np.multiply(X0_p[:3, 4:], W0))
    data['params']['exp_0_sum_0'] = int( np.sum( np.multiply(X0_p[:3, 4:], W0) ) )

    data['params']['exp_0_ip_1'] = pl.to_json(X1_p[:3, 4:])
    data['params']['exp_0_filter_1'] = pl.to_json(W1)
    data['params']['exp_0_prod_1'] = pl.to_json(np.multiply(X1_p[:3, 4:], W1))
    data['params']['exp_0_sum_1'] = int( np.sum( np.multiply(X1_p[:3, 4:], W1) ) )

    data['params']['exp_0_ip_2'] = pl.to_json(X2_p[:3, 4:])
    data['params']['exp_0_filter_2'] = pl.to_json(W2)
    data['params']['exp_0_prod_2'] = pl.to_json(np.multiply(X2_p[:3, 4:], W2))
    data['params']['exp_0_sum_2'] = int( np.sum( np.multiply(X2_p[:3, 4:], W2) ) )
    
    ####


    data['params']['exp_1_ip_0'] = pl.to_json(X0_p[2:5,2:5])
    data['params']['exp_1_filter_0'] = pl.to_json(V0)
    data['params']['exp_1_prod_0'] = pl.to_json(np.multiply(X0_p[2:5,2:5], V0))
    data['params']['exp_1_sum_0'] = int( np.sum( np.multiply(X0_p[2:5,2:5], V0) ) )

    data['params']['exp_1_ip_1'] = pl.to_json(X1_p[2:5,2:5])
    data['params']['exp_1_filter_1'] = pl.to_json(V1)
    data['params']['exp_1_prod_1'] = pl.to_json(np.multiply(X1_p[2:5,2:5], V1))
    data['params']['exp_1_sum_1'] = int( np.sum( np.multiply(X1_p[2:5,2:5], V1) ) )

    data['params']['exp_1_ip_2'] = pl.to_json(X2_p[2:5,2:5])
    data['params']['exp_1_filter_2'] = pl.to_json(V2)
    data['params']['exp_1_prod_2'] = pl.to_json(np.multiply(X2_p[2:5,2:5], V2))
    data['params']['exp_1_sum_2'] = int( np.sum( np.multiply(X2_p[2:5,2:5], V2) ) )


  
""" 
for testing

# fixed values

X0 = np.array([ [1,0,1,2,1], [0,0,2,2,2], [2,2,2,1,1], [1,0,0,2,2], [1,2,0,0,1]  ])
X1 = np.array([ [1,0,1,2,1], [1,1,0,2,1], [0,1,2,1,2], [1,2,1,0,0], [0,0,0,1,1]  ])
X2 = np.array([ [2,2,2,0,2], [2,2,0,0,2], [1,0,1,0,0], [2,1,0,0,1], [0,2,2,2,2]  ])

W0 = np.array([ [-1,-1,-1], [1,1,-1], [-1,1,1] ])
W1 = np.array([ [0,1,0], [-1,1,1], [-1,1,-1] ])
W2 = np.array([ [0,1,1], [1,1,1], [-1,-1,1] ])

V0 = np.array([ [1,1,-1], [0,0,0], [-1,0,0]])
V1 = np.array([ [1,-1,-1], [1,-1,-1], [-1,0,1]])
V2 = np.array([ [-1,1,-1], [0,1,0], [-1,-1,1]])

b0 = 1
b1 = 0

Should have

>>> output_0
array([[7, 6, 2],
       [7, 3, 2],
       [5, 9, 3]])
>>> output_1
array([[ 2, -2, -3],
       [-1, -7,  3],
       [-1, -1,  7]])

"""