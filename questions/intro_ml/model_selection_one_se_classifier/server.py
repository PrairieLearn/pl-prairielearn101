import random, copy
import numpy as np

def generate(data):

    rms = [random.uniform(0.3, 0.4), random.uniform(0.4, 0.5), random.uniform(0.4, 0.6), random.uniform(0.5, 0.8), random.uniform(0.7, 0.8), random.uniform(0.7, 0.8), random.uniform(0.5, 0.7), random.uniform(0.4, 0.6), random.uniform(0.4, 0.5), random.uniform(0.3, 0.4) ]
    alphas = [0.01, 0.05, 0.1, 0.5, 1, 5, 10, 50, 100, 500]
    data['params']['models'] = [{'name': i, 'alpha': alphas[i], 'mean': round(rms[i], 3), 'se': round(random.uniform(0.1, 0.3), 4)} for i in range(10)]
    rm_rounded = [m['mean'] for m in data['params']['models']]
    se_rounded = [m['se'] for m in data['params']['models']]
    
    idx_best = np.argmax(rm_rounded)
    target = rm_rounded[idx_best] - se_rounded[idx_best]
    idx_one_se = np.max(np.where(np.array(rm_rounded) >= target))

    data['params']['best']   =  [{'id': i, 'ans': 'true'} if i==idx_best   else {'id': i, 'ans': 'false'} for i in range(10)]
    data['params']['one_se'] =  [{'id': i, 'ans': 'true'} if i==idx_one_se else {'id': i, 'ans': 'false'} for i in range(10)]
