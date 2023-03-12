import random, copy
import numpy as np

def sigmoid(z):
  return 1/(1+np.exp(-z))


def crossEntropyLoss(w, X, y):
  y_pred = sigmoid(np.dot(X,w))
  loss_pos = y*np.log(y_pred)
  loss_neg = (1-y)*np.log(1-y_pred)
  loss = np.sum(-1*(loss_pos + loss_neg))
  return loss


def gd_step(w, X, y, lr):
  y_hat = sigmoid(np.dot(X,w)) 
  gradient = np.dot(X.T, y - y_hat)
  w = w + lr * gradient
  l = crossEntropyLoss(w,X,y)
  return w, l, gradient


def generate(data):
    
    l_init = 0
    # choose an example with real non-zero loss
    while l_init < 5:

      # generate "true" coefficients
      n_data = 4
      w_t = np.random.randint(-5,5,size=3)
      alpha = np.round(np.random.choice(np.arange(0.1, 0.7, 0.1)), 2)
      X = np.hstack([np.ones((n_data,1)), np.random.randint(-3,3,(n_data,2))])
      y = np.array(sigmoid(np.sum(w_t*X, axis=1)) >= 0.5).astype(int)
      w_init = np.random.randint(-5,5,size=3)

      data['params']['samples'] = np.hstack([X, y.reshape(-1,1)]).tolist()
      data['params']['w_init'] = w_init.tolist()
      data['params']['alpha'] = alpha
      
      z = np.dot(X, w_init)
      p = sigmoid(z)
      yhat = np.array(p >= 0.5).astype('int')

      l_init = crossEntropyLoss(w_init, X, y)
      data['params']['compute'] = [{'i': i, 'x': X[i].tolist(), 'y': int(y[i]), 'p': float(np.round(p[i],6)), 'z': float(z[i]), 'yhat': int(yhat[i]), 'correct': bool(y[i]==yhat[i]), 'incorrect': bool(y[i]!=yhat[i]), 'pos': bool(y[i]), 'notlast': bool(i<(n_data-1))} for i in range(n_data)]
      data['correct_answers']['l_init'] = l_init
      
      w_new, l_new, grad = gd_step(w_init, X, y, alpha)
      data['correct_answers']['l_new'] = l_new
      data['params']['w_new'] = w_new.tolist()
      data['params']['w_new_r'] = [np.round(w,5) for w in w_new]

      # for explanation:
      data['params']['grad'] = [np.round(g, 5) for g in grad]
      z_new = np.dot(X, w_new)
      p_new = sigmoid(z_new)
      yhat_new = np.array(p_new >= 0.5).astype('int')

      data['params']['compute_new'] = [{'i': i, 'x': X[i].tolist(), 'y': int(y[i]), 'p': float(p_new[i]), 'z': float(np.round(z_new[i], 5)), 'yhat': int(yhat_new[i]), 'correct': bool(y[i]==yhat_new[i]), 'incorrect': bool(y[i]!=yhat_new[i]), 'pos': bool(y[i]), 'notlast': bool(i<(n_data-1))} for i in range(n_data)]
