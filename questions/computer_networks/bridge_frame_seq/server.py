import random, copy
import numpy as np
import utilIAP as iap

def parse(data):
    data['format_errors'] = {}


def generate(data):


    data['params']['exampleNone'] = []
    data['params']['exampleFlood'] = []
    data['params']['exampleFwd'] = []

    nports = random.randint(3,4)
    nhosts = random.randint(6,8)
    
    nFramesLocal = 4
    nFramesNonLocal = 1
    nFramesBcast = 1
    nFramesNone = 1
    nInTable = nhosts - 3
    
    data['params']['brmacs'] = [{'portno': i, 'mac': iap.macs(1)[0]} for i in range(nports)]
    data['params']['hostmacs'] = [{'mac': iap.macs(1)[0], 'port': i % nports } for i in range(nhosts)]
    data['params']['hostmacs'] = random.sample(data['params']['hostmacs'], len(data['params']['hostmacs'])) # shuffle
    
    data['params']['knownhosts'] = random.sample(data['params']['hostmacs'], nInTable)
    for i in range(nInTable):
        data['params']['knownhosts'][i]['age'] = round(random.uniform(0,10), 2)
        
    # get a definite "None"
    rx = random.sample(data['params']['knownhosts'], 1)
    framesNone = [{'src': iap.macs(1)[0],  'dst': rx[0]['mac'], 'port': rx[0]['port']} ]
    framesLocal = [{'src': data['params']['hostmacs'][i]['mac'], 'dst': data['params']['hostmacs'][random.choice([j for j in range(0,nhosts) if i!=j])]['mac'], 'port': data['params']['hostmacs'][i]['port']} for i in random.choices(range(0,nhosts-1), k=nFramesLocal)]
    framesNonLocal = [{'src': data['params']['hostmacs'][i]['mac'], 'dst': iap.macs(1)[0], 'port': data['params']['hostmacs'][i]['port']} for i in random.choices(range(0,nhosts), k=nFramesNonLocal)]
    framesBcast = [{'src': data['params']['hostmacs'][i]['mac'], 'dst': "ff:ff:ff:ff:ff:ff", 'port': data['params']['hostmacs'][i]['port']} for i in random.choices(range(0,nhosts), k=nFramesNonLocal)]


    data['params']['frames'] = random.sample([*framesNone, *framesLocal, *framesNonLocal, *framesBcast], nFramesNone+nFramesLocal+nFramesNonLocal+nFramesBcast)

    # now keep track of what bridge will learn
    macsKnown = [[] for i in range(nports)]
    for h in data['params']['knownhosts']:
        macsKnown[h['port']].append(h['mac'])
        
    for i, frame in enumerate(data['params']['frames']):
        
        data['params']['frames'][i]['k'] = i        

        # first, add src to forwarding table if not there yet
        ckSrc = [frame['src']  in l for l in macsKnown]
        if not any(ckSrc): # if new MAC
            macsKnown[frame['port']].append(frame['src'])
            
        # then, check if dst is in forwarding table
        ckDst = [frame['dst']  in l for l in macsKnown]
        if not any(ckDst): # if don't know the MAC, forward on all ports except arrival port
            data['params']['frames'][i]['ans'] = [{'p': j+1, 'a': "true"} if j!= frame['port'] else {'p': j+1, 'a': "false"} for j in range(nports)]
            data['params']['frames'][i]['ans'].append({'p': 'None', 'a': "false"})
            data['params']['exampleFlood'].append(data['params']['frames'][i])
            
        else:
            pt = np.where([frame['dst'] in l for l in macsKnown])[0][0]
            if pt==frame['port']: # if src and dst port are same
                data['params']['frames'][i]['ans'] =  [{'p': j+1, 'a': "false"} for j in range(nports)]
                data['params']['frames'][i]['ans'].append({'p': 'None', 'a': "true"})
                data['params']['exampleNone'].append(data['params']['frames'][i])
            else:
                data['params']['frames'][i]['ans'] =  [{'p': j+1, 'a': "true"} if j==pt else {'p': j+1, 'a': "false"} for j in range(nports)]
                data['params']['frames'][i]['ans'].append({'p': 'None', 'a': "false"})
                data['params']['exampleFwd'].append(data['params']['frames'][i])

        
    #data['params']['srcPorts'] = ["false" if i!=data['params']['num'][0] else "true" for i in range(4)]
    #data['params']['fwdPorts'] = ["false" if i==data['params']['num'][0] else "true" for i in range(4)]
    #data['params']['dstPorts'] = ["false" if i!=data['params']['num'][1] else "true" for i in range(4)]
    
    # make port numbers start at 1
    for i,x in enumerate(data['params']['brmacs']):
        data['params']['brmacs'][i]['portno'] =  data['params']['brmacs'][i]['portno'] + 1
    for i,x in enumerate(data['params']['knownhosts']):
        data['params']['knownhosts'][i]['port'] =  data['params']['knownhosts'][i]['port'] + 1
    for i,x in enumerate(data['params']['frames']):
        data['params']['frames'][i]['port'] =  data['params']['frames'][i]['port'] + 1
