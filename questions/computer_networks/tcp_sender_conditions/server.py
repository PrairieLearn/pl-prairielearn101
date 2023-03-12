import random, copy

def generate(data):

    data['params']['scenarios'] = {'app': False, 'cwnd': False, 'rwnd': False}
    
    data['params']['mss'] = 1000
    s = random.choice(['app', 'cwnd', 'rwnd'])
    
    if s=="app": # application limited
        data['params']['scenarios']['app'] = True
        data['params']['inflight'] = random.randint(5, 900)
        data['params']['buffer'] = random.randint(1200, 5000)
        data['params']['cwnd'] = random.randint(6000, 10000)
        data['params']['awnd'] = random.randint(10000, 60000)

    if s=="cwnd": # cwnd limited
        data['params']['scenarios']['cwnd'] = True
        data['params']['inflight'] = random.choice([2000, 3000, 4000, 5000])
        data['params']['buffer'] = random.randint(20000, 50000)
        data['params']['cwnd'] = random.choice([7000, 8000, 9000, 10000, 11000, 12000])
        data['params']['awnd'] = random.randint(20000, 50000)
        

    if s=="rwnd": # application limited
        data['params']['scenarios']['rwnd'] = True
        data['params']['inflight'] = random.choice([2000, 3000, 4000, 5000])
        data['params']['buffer'] = random.randint(20000, 50000)
        data['params']['cwnd'] = random.choice([16000, 17000, 18000, 19000, 20000, 21000])
        data['params']['awnd'] = random.randint(6000, 10000)
        
        
    data['correct_answers']['bytes'] = min( data['params']['buffer'], min(data['params']['cwnd'], data['params']['awnd']) - data['params']['inflight'])
