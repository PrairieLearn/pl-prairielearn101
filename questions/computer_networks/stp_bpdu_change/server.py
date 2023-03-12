import random, copy
import utilIAP as iap
import numpy as np
import prairielearn as pl

def parse(data):
    pass
    
def tiebreak(bpdus):
    roots = np.array([int(b['root'].replace(":", "").replace(".", ""), base=16)  for b in bpdus])
    rpcs  = np.array([int(b['rpc']) for b in bpdus])
    sids  = np.array([int(b['id'].replace(":", "").replace(".", ""), base=16) for b in bpdus])
    spts  = np.array([int(b['port']) for b in bpdus])
    min_root_idx = np.where(roots == min(roots) )[0] # index of port with min root bridge ID
    min_rpc = min(rpcs[min_root_idx])
    min_rpc_idx  = np.where((roots == min(roots)) & (rpcs==min_rpc))[0]  # index of port with min root bridge ID and min RPC
    min_sid = min(sids[min_rpc_idx])
    min_sid_idx  = np.where((roots == min(roots)) & (rpcs==min_rpc) & (sids==min_sid))[0]  # index of port with min root bridge ID and min RPC and min sender bridge ID
    min_spt = min(spts[min_sid_idx])
    min_spt_idx  = np.where((roots == min(roots)) & (rpcs==min_rpc) & (sids==min_sid) & (spts==min_spt))[0] # tiebreak winner for sure
    
    ret = bpdus[min_spt_idx[0]].copy()
    return ret 

def generate(data):
    
    macs = iap.macs(6)
    while len(np.unique(macs)) != len(macs):
        macs = iap.macs(6)
    macs.sort()
    rpcost = ['100', '200', '300', '400', '500']
    
    isRoot = random.choice([0, 0, 1])
    if isRoot:
        # option 1: my id is the lowest, I am new root bridge
        data['params']['mac'] = macs[0]
        data['params']['id'] = macs[0]
    else:
        # option 2: my is the highest
        data['params']['mac'] = macs[5]
        data['params']['id'] = macs[5]

    bpdus = [{'rxport': int(a), 'root': str(b), 'id': str(c), 'rpc': str(d),'port': str(e), 'new_rpc': str(int(d) + 100) } for a, b, c, d, e in zip(
        np.arange(1,3), 
        np.random.choice(macs[1:3], size=2, replace=True, p=[0.65, 0.35]),
        np.random.choice(macs[3:5], size=2, replace=False), 
        np.random.choice(rpcost, size=2, replace=True), 
        np.random.choice(['8001', '8002', '8003', '8004'], size=2, replace=False))]

    data['params']['rx-bpdus'] = pl.to_json(bpdus)

    # get the "winning" BPDU
    bpdu_own = {'rxport': 0, 'root': str(data['params']['mac']), 'id': str(data['params']['mac']), 'rpc': '0','port': 0, 'new_rpc': '0'} 
    winner_bpdu = tiebreak([bpdu_own, bpdus[0], bpdus[1]])
    winner_bpdu['id'] = data['params']['mac'] 
    winner_bpdu['rpc'] = str(max(0, int(winner_bpdu['new_rpc'])))
    #print(bpdus)
    data['params']['win-bpdu'] = pl.to_json(winner_bpdu)

    data['params']['opts'] = [{"rxport": i+1, "root": False, "des": False, "bl": False} for i in range(2)]
    if isRoot:
        data['params']['chk'] = [True, True, False]
        data['params']['opts'][0]["des"] =  True
        data['params']['opts'][1]["des"] =  True

    else:
        # if I'm not the root, the port that the winning BPDU came on is the root port and I won't send a BPDU on it
        data['params']['chk'] = [True, True, True]
        data['params']['chk'][winner_bpdu['rxport']-1] = False
        data['params']['opts'][(winner_bpdu['rxport']-1)]["root"] =  True

        # now check if the OTHER port should be DP
        other_port = (winner_bpdu['rxport']%2)
        dp_bpdu = tiebreak([winner_bpdu, bpdus[other_port]])
        if dp_bpdu['id']==data['params']['mac']:
            # I am DP
            data['params']['chk'][2] = False # it's not "None of the above"
            data['params']['opts'][(winner_bpdu['rxport']%2)]["des"] =  True  # the non-winner-port is DP
        else:
            data['params']['chk'][other_port] = False
            data['params']['opts'][(winner_bpdu['rxport']%2)]["bl"] =  True  # the non-winner-port is blocked
