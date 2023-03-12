import random, copy
import numpy as np
from scipy import stats
from scipy.spatial.distance import cdist

def sigmoid(z):
  return 1/(1+np.exp(-z))


def generate(data):
    

  # generate "true" coefficients
  n_data = 6
  w_t = np.random.randint(-5,5,size=3)
  alpha = np.round(np.random.choice(np.arange(0.1, 0.7, 0.1)), 2)
  X = np.random.randint(-15,15,(n_data,3))
  y = np.array(sigmoid(np.sum(w_t*X, axis=1)) >= 0.5).astype(int)
  
  data['params']['k'] = random.choice([1,3])
  x_test = np.random.randint(-10,10,(1,3))
  data['params']['test'] = x_test[0].tolist()

  data['params']['samples'] = np.hstack([X, y.reshape(-1,1)]).tolist()
  
  norm = random.choice([1,2])
  if norm==1:
      data['params']['metric'] = "Manhattan (L1)"
      distances = cdist(X, x_test, metric='cityblock').squeeze()

  elif norm==2:
      data['params']['metric'] = "Euclidean (L2)"
      distances = cdist(X, x_test, metric='euclidean').squeeze()

  nn = np.argsort(distances)[:data['params']['k']]
  y_pred = stats.mode(y[nn], keepdims=True).mode[0]
  
  
  data['params']['compute'] = [{'i': i, 'x': X[i].tolist(), 'y': int(y[i]), 'distance': np.round(distances[i], 4), 'neighbor': i in nn} for i in range(n_data)]

  data['params']['y_pred'] = [bool(not(y_pred)), bool(y_pred)]
