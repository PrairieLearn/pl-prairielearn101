import random, copy
import utilIAP as iap
import numpy as np
import prairielearn as pl

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
    
    # what was the tiebreaker?
    tbrk_idx = np.argmin( [len(min_root_idx), len(min_rpc_idx), len(min_sid_idx), len(min_spt_idx)])
    tbrk = ['root bridge ID', 'root path cost', 'sender bridge ID', 'sender bridge port']
    # should really return tiebreak index and winnder index too...
    
    ret = bpdus[min_spt_idx[0]]

    
    return ret # return the winning BPDU, along with reason and new RPC


def generate(data):

    # prepare the BPDUs and the configuration of the bridge
    
    macs = iap.macs(10)
    while len(np.unique(macs)) != len(macs): # make sure macs are unique
        macs = iap.macs(10)

    macs.sort()
    rpcost = ['100', '200', '300', '400', '500']
    
    bpdus = [{'rxport': int(a), 'root': str(b), 'id': str(c), 'rpc': str(d),'port': str(e)} for a, b, c, d, e in zip(
        np.arange(1,5), 
        np.random.choice(macs[0:2], size=4, replace=True, p=[0.65, 0.35]),
        np.random.choice(macs[2:8], size=4, replace=False),  # if you allow replacement, can end up with same bridge sending different root on diff ports... very weird. 
        np.random.choice(rpcost, size=4, replace=True), 
        np.random.choice(['8001', '8002', '8003', '8004'], size=4, replace=False))]
    data['params']['bid'] = macs[9]
    data['params']['bpdus'] = pl.to_json(bpdus)
        
    rootport = [False for i in range(4)]
    designated = [False for i in range(4)]
    blocking = [False for i in range(4)]

    # now, get the configuration from root port
    br_root = tiebreak(bpdus)
    data['params']['root_bpdu'] = br_root
    
    # now that I know who the root is - for each port, I can see if it is designated
    
    data['params']['feedback-port'] = ["" for i in range(4)]
    for i in range(4):
        
        new_bpdu = {'rxport': i+1, 'root': str(br_root['root']), 'id': str(data['params']['bid']), 'rpc': str(int(br_root['rpc']) + 100),'port': '800' + str(i+1)}
        ret = tiebreak([new_bpdu, bpdus[i]])
        
        if br_root['rxport'] == bpdus[i]['rxport']:
            # this is the root port
            rootport[i] = True
            data['params']['feedback-port'][i] = "Port %d is the root port." % ( i+1 )

        else:  # not a root port? check if designated
            # if I know about a better root than this BPDU, I will become designated port and announce it to everyone!
            if int(new_bpdu['root'].replace(":", "").replace(".", ""), base=16) < int(bpdus[i]['root'].replace(":", "").replace(".", ""), base=16):
                designated[i] = True
                data['params']['feedback-port'][i] = "Port %d becomes a designated port because it is aware of a lower root bridge ID (<tt>8000.%s</tt>) than the current designated bridge on this network segment (which advertises <tt>8000.%s</tt> as the root bridge)." % ( i+1, new_bpdu['root'], bpdus[i]['root'])
            elif new_bpdu['rpc'] < bpdus[i]['rpc']: # if I have a better root path cost than this BPDU, I will become designated port and announce it to everyone!
                designated[i] = True
                data['params']['feedback-port'][i] = "Port %d becomes a designated port because it has a lower root path cost (%s) than the current designated bridge on this network segment (which has root path cost %s)." % ( i+1, new_bpdu['rpc'], bpdus[i]['rpc'])
            # I won't ever win a tiebreaker on sender bridge ID, I have a high MAC
            else:
                blocking[i] = True
                data['params']['feedback-port'][i] = "Port %d is blocking because it is not a root port or a designated port." % ( i+1)

        
    data['params']['opts'] = [{"rxport": i+1, "root": rootport[i], "des": designated[i], "bl": blocking[i]} for i in range(4)]
