import random, copy
import numpy as np
import prairielearn as pl


def generate(data):

    data['params']['id'] = random.randint(10000, 65535)
    data['params']['totlen'] = random.randint(3000, 6000) 
    data['params']['mtu'] = random.choice([1420, 1460, 1300]) # only use MTUs where mtu-20 is a multiple of 8

    payloadSize = data['params']['totlen'] - 20
    lastFragPayloadSize = payloadSize % (data['params']['mtu']-20)
    nFragments = int(np.ceil(  payloadSize / (data['params']['mtu'] - 20)  ))
    
    hlens =  np.repeat(5,nFragments)
    totalLens = np.append( np.repeat(data['params']['mtu'], nFragments - 1), lastFragPayloadSize + 20)
    ids = np.repeat(data['params']['id'], nFragments)
    dfs = np.repeat(0, nFragments)
    mfs = np.append( np.repeat(1, nFragments - 1), 0)
    offsets = np.append(0, np.cumsum(totalLens-20)/8)

    
    mat = np.column_stack(( hlens, totalLens, ids, dfs, mfs, offsets[0:-1])).astype('int').tolist()
    keys = ['hlen', 'totalLen', 'id', 'df', 'mf', 'offset']
    data['params']['frags'] = [dict(zip(keys, l)) for l in mat ]
