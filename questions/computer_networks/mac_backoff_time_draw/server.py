
import random, copy



def grade(data):
    data['partial_scores']['csma']  = 0 
    data['score'] = 0
    if 'csma' in data['submitted_answers']:
        placed =  [d for d in data['submitted_answers']['csma'] if 'placed_by_user' in d.keys() and d['type']=='pl-rectangle']
        for p in placed:
            # check if it's the ACK
            if (p['width']==20) and ( (data['params']['ackx']-7) <= p['left'] <= (data['params']['ackx']+7)) and ( (data['params']['setup'][3]['y']-10) <= p['top'] <= (data['params']['setup'][3]['y'] + 10 ) ): 
                data['partial_scores']['csma']  += 0.5
            # check if it's the data
            elif (p['width']==100) and ( (data['params']['txBox']-7) <= p['left'] <= (data['params']['txBox']+7)) and ( (data['params']['setup'][1]['y']-10) <= p['top'] <= (data['params']['setup'][1]['y'] + 10 ) ): 
                data['partial_scores']['csma']  += 0.5
    data['score'] = data['partial_scores']['csma'] 


            

def generate(data):
    
    # shuffle role of hosts
    x = [{"name": "A", "y": 60 }, {"name": "B", "y": 160}, {"name": "C", "y": 260}, {"name": "D", "y": 360}]
    data['params']['setup'] = random.sample(x, k=len(x))
    
    # width of initial data tx
    w = random.choice([5, 6, 7])
    data['params']['txw'] = w*20
    data['params']['txx'] = 150 + 10*(w-5)
    # this determines the x position of the SIFS and DIFS line...
    data['params']['sifs'] = {'start': 200+20*(w-5), 'end': 220+20*(w-5), 'txt': 195+20*(w-5)}
    data['params']['difs'] = {'start': 240+20*(w-5), 'end': 280+20*(w-5), 'txt': 245+20*(w-5)}
    # the position of the ACK...
    data['params']['ackx'] = 230+20*(w-5)
    
    # for the host that will send next...
    cinit = random.choice([5,4,3])
    nleft = cinit - 2
    cboxes = [{'text': i, 'x': 70+(cinit-i)*20} for i in range(1,cinit+1)]
    data['params']['initBoxes'] = cboxes[-2:]

    data['params']['nextBoxes'] = [{'text': c['text'], 'x': c['x']+80+20*w} for c in cboxes[:-2]]
    ntx = len(data['params']['nextBoxes'] )
    data['params']['txBox'] = 330+20*nleft+20*(w-5)

    # for the host that will not get a turn...
    dinit = random.choice([cinit+1,cinit+2, cinit+3])
    dboxes = [{'text': i, 'x': 70+(dinit-i)*20} for i in range(1,dinit+1)]
    data['params']['initBoxesNot'] = dboxes[-2:]
    data['params']['nextBoxesNot'] = [{'text': d['text'], 'x': d['x']+80+20*w} for d in dboxes[:-2]][-ntx:] # only use the ones until the next Tx!

    # axis ticks
    data['params']['tlabels'] = [{'label': i, 'xpos': 60+i*20, 'xoffset': -4 if i < 10 else -6} for i in range(21)]
    
    # the ACK happens after one SIFS:
    data['correct_answers']['ack-time'] = 2   + w + 1
    data['params']['ack-host-opts'] = [{"name": h, 'c': h==data['params']['setup'][3]['name']} for h in ["A", "B", "C", "D"]]

    # then the next data TX after ACK + a DIFS + remaining backoff:
    data['correct_answers']['dat-time'] = data['correct_answers']['ack-time']   + 1 + 2 + cinit-2
    data['params']['dat-host-opts'] = [{"name": h, 'c': h==data['params']['setup'][1]['name']} for h in ["A", "B", "C", "D"]]

