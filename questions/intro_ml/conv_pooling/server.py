import random, copy
import numpy as np
from numpy.lib.stride_tricks import as_strided


# source: https://stackoverflow.com/a/54966908/3524528
def pool2d(A, kernel_size, stride, padding=0, pool_mode='max'):
    '''
    2D Pooling
    
    Parameters:
    A: input 2D array
    kernel_size: int, the size of the window over which we take pool
    stride: int, the stride of the window
    padding: int, implicit zero paddings on both sides of the input
    pool_mode: string, 'max' or 'avg'
    '''
    # Padding
    A = np.pad(A, padding, mode='constant')
    
    # Window view of A
    output_shape = ((A.shape[0] - kernel_size) // stride + 1,
                (A.shape[1] - kernel_size) // stride + 1)
    
    shape_w = (output_shape[0], output_shape[1], kernel_size, kernel_size)
    strides_w = (stride*A.strides[0], stride*A.strides[1], A.strides[0], A.strides[1])
    
    A_w = as_strided(A, shape_w, strides_w)
    
    # Return the result of pooling
    if pool_mode == 'max':
        return A_w.max(axis=(2, 3))
    elif pool_mode == 'avg':
        return A_w.mean(axis=(2, 3))


def generate(data):
    
  data['params'] = random.choice([
      {'filter': 2, 'stride': 1, 'pooltype': 'max', 'in_size': 4, 'pad': 0},
      {'filter': 2, 'stride': 2, 'pooltype': 'max', 'in_size': 6, 'pad': 0},
      {'filter': 3, 'stride': 3, 'pooltype': 'max', 'in_size': 9, 'pad': 0},
      {'filter': 2, 'stride': 2, 'pooltype': 'avg', 'in_size': 4, 'pad': 0}


      ])    

  X = np.random.randint(-10,10,(data['params']['in_size'] , data['params']['in_size'] ))
  data['params']['input'] = X.tolist()

  pooled = pool2d(X, data['params']['filter'] , data['params']['stride'] , padding = data['params']['pad'], pool_mode = data['params']['pooltype'] )
  data['correct_answers']['output'] = pooled.tolist()
