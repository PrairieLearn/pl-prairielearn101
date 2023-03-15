
import random, copy



def grade(data):
    data['partial_scores']['csma']  = 0 
    data['score'] = 0
    if 'csma' in data['submitted_answers']:
        placed =  [d for d in data['submitted_answers']['csma'] if 'placed_by_user' in d.keys() and d['type']=='pl-rectangle']
        for p in placed:
            # check if it's the ACK
            if (p['width']==20) and ( (data['params']['ackx']-7) <= p['left'] <= (data['params']['ackx']+7)) and ( (360-10) <= p['top'] <= (360 + 10 ) ): 
                data['partial_scores']['csma']  += 0.20
            # check if it's the data
            elif (p['width']==data['params']['width_choice']) and ( (data['params']['txBox']-7) <= p['left'] <= (data['params']['txBox']+7)) and ( (60-10) <= p['top'] <= (60 + 10 ) ): 
                data['partial_scores']['csma']  += 0.20
            elif (p['width']==20) and ( (data['params']['rtsx']-7) <= p['left'] <= (data['params']['rtsx']+7)) and ( (60-10) <= p['top'] <= (60 + 10 ) ): 
                data['partial_scores']['csma']  += 0.15
            # check if it's the data
            elif (p['width']==20) and ( (data['params']['ctsx']-7) <= p['left'] <= (data['params']['ctsx']+7)) and ( (360-10) <= p['top'] <= (360 + 10 ) ): 
                data['partial_scores']['csma']  += 0.15
            elif (p['width']==data['params']['defer']) and ( (data['params']['defer_location']-7) <= p['left'] <= (data['params']['defer_location']+7)) and ( (160-10) <= p['top'] <= (160 + 10 ) ): 
                data['partial_scores']['csma']  += 0.15
            elif (p['width']==data['params']['defer']) and ( (data['params']['defer_location']-7) <= p['left'] <= (data['params']['defer_location']+7)) and ( (260-10) <= p['top'] <= (260 + 10 ) ): 
                data['partial_scores']['csma']  += 0.15
                
    data['score'] = data['partial_scores']['csma'] 

            

def generate(data):
    
    # shuffle role of hosts
    x = [{"name": "A", "y": 60 }, {"name": "B", "y": 160}]
    data['params']['setup'] = random.sample(x, k=len(x))
    
    # width of initial data tx
    w = random.choice([5, 6, 7])
    width_choice=random.choice([60,80,100, 120, 140,160])
    data['params']['width_choice'] = width_choice
    data['params']['defer']=40+width_choice
    data['params']['txw'] = w*20
    data['params']['txx'] = 150 + 10*(w-5)
    # this determines the x position of the SIFS and DIFS line...
    data['params']['sifs4'] = {'start':180+width_choice, 'end': 200+width_choice, 'txt':175+width_choice}
    data['params']['sifs3'] = {'start':160, 'end': 180, 'txt': 155}
    data['params']['sifs2'] = {'start':120, 'end': 140, 'txt': 115}
    data['params']['difs'] = {'start': 240+20*(w-5), 'end': 280+20*(w-5), 'txt': 245+20*(w-5)}
    # the position of the ACK...
    data['params']['ackx'] = 210+width_choice
    data['params']['rtsx'] = 110
    data['params']['ctsx'] = 150
    data['params']['txBox'] = ((width_choice)/2)+180
    data['params']['defer_location']=((width_choice)/2)+200
 
    # axis ticks
    data['params']['tlabels'] = [{'label': i, 'xpos': 60+i*20, 'xoffset': -4 if i < 10 else -6} for i in range(21)]
    
    # the ACK happens after one SIFS:
    data['correct_answers']['ack-time'] = 2   + w + 1
    data['params']['ack-host-opts'] = [{"name": h, 'c': h==data['params']['setup'][1]['name']} for h in ["A", "B"]]

   

