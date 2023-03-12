import random, copy

def generate(data):

    data['params']['sn_a'] = random.randint(5000, 9000)
    data['params']['sn_b'] = random.randint(1000, 4000)
    data['params']['ack_b'] = data['params']['sn_a'] + 1
    data['params']['sn_c'] = data['params']['sn_a'] + 1
    data['params']['ack_c'] = data['params']['sn_b'] + 1

    data['params']['len_d'] = random.randint(100, 2000)
    data['params']['sn_d'] = data['params']['ack_c']
    data['params']['ack_d'] = data['params']['ack_b'] 


    data['params']['sn_e'] = data['params']['sn_c'] 
    data['params']['ack_e'] = data['params']['sn_d'] + data['params']['len_d']

    data['correct_answers'] = data['params']
    
    data['params']['flags'] = [
        {'ack': False, 'syn': True,  'fin': False, 'none': False},
        {'ack': True, 'syn': True,  'fin': False, 'none': False},
        {'ack': True, 'syn': False,  'fin': False, 'none': False}
        ]