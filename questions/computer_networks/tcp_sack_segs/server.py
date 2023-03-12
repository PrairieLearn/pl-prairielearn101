import random, copy

def generate(data):

    data['params']['cport'] = random.randint(49152,65535)
    data['params']['sport'] = random.randint(1000,4000)
    data['params']['client'] = "10.%d.%d.%d" % (random.randint(1, 254), random.randint(1, 254), random.randint(1, 254)) 
    data['params']['server'] = "10.%d.%d.%d" % (random.randint(1, 254), random.randint(1, 254), random.randint(1, 254)) 
    
    data['params']['isn'] = random.randint(1e9, 2e9)
    data['params']['isn2'] = random.randint(3e9, 4294967295)
    data['params']['segs'] = [{'start': data['params']['isn'] + i*1448, 'end': data['params']['isn'] + (i+1)*1448} for i in range(9)]
    data['params']['ack'] = data['params']['isn'] + random.choice([2,3])*1448
    data['params']['lsack'] = data['params']['ack'] + random.choice([1,2,3])*1448
    data['params']['rsack'] = data['params']['lsack'] + random.choice([1,2])*1448
    
    for i, s in enumerate(data['params']['segs']):
        if data['params']['segs'][i]['end'] <= data['params']['ack']:
            data['params']['segs'][i]['ans'] = "true"
        elif data['params']['segs'][i]['start'] >= data['params']['lsack'] and data['params']['segs'][i]['end'] <= data['params']['rsack']:
            data['params']['segs'][i]['ans'] = "true"
        else:
            data['params']['segs'][i]['ans'] = "false"
    