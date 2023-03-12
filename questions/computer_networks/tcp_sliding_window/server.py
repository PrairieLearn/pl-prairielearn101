import random, copy

def grade(data):

    data['partial_scores']['window'] = {'feedback': {'correct': False, 'matches': {}, 'missing': {}}, 'score': 0, 'weight': 1}

    placed =  [d for d in data['submitted_answers']['window'] if 'placed_by_user' in d.keys() and d['type']=='pl-rectangle']
    if len(placed)==1:
        if (data['params']['rwnd_new']['width']-7 <= placed[0]['width'] <= data['params']['rwnd_new']['width'] + 7) and (data['params']['rwnd_new']['x']-7 <= placed[0]['left'] <= data['params']['rwnd_new']['x'] + 7):
            data['partial_scores']['window'] =   {'feedback': {'correct': True, 'matches': {}, 'missing': {}}, 'score': 1, 'weight': 1}

    #print(data['params']['rwnd_new'])
    #print(placed)
    #print(data['partial_scores'])
    data['score'] = sum([data["partial_scores"][c]['weight']*data["partial_scores"][c]['score'] for c in data["partial_scores"].keys()])/sum([data["partial_scores"][c]['weight'] for c in data["partial_scores"].keys()])
    
def generate(data):
    
    data['params']['segs'] = [{'y': 70, 'x': 40+40*i, 'n': i+1} for i in range(14)]
    
    rwnd_size = random.choice([4, 5, 6])
    rwnd_start = random.choice([2, 3, 4])
    rwnd_end = rwnd_start + rwnd_size - 1
    rwnd_next = rwnd_start + random.choice([2, 3])
    data['params']['rwnd_init'] = {'y': 70, 'x': 40*rwnd_start+20*rwnd_size-20, 'width': rwnd_size*40, 'start': rwnd_start, 'xnext': -20+40*(rwnd_next)} 
    
    n_sent_not_acked = rwnd_next-rwnd_start
    n_not_sent = rwnd_size - rwnd_next + 1
    
    data['params']['ack'] = random.choice( [rwnd_start+1, rwnd_start+2,  rwnd_next ] )
    min_new_rwnd = rwnd_size + (rwnd_start - data['params']['ack'] )
    data['params']['new_rwnd'] = random.choice([min_new_rwnd, min_new_rwnd+1, min_new_rwnd+random.randint(2, 4)]) 
    
    data['params']['rwnd_new'] = {'y': 70, 'x': 40*data['params']['ack']+20*data['params']['new_rwnd']-20, 'width': data['params']['new_rwnd']*40, 'start': data['params']['ack']} 

    data['params']['send'] = [{'i': i, 'ans': rwnd_next <= i < data['params']['ack']+data['params']['new_rwnd']} for i in range(rwnd_start,15)]