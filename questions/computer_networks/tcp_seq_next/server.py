import random, copy

def generate(data):

    data['params']['cport'] = random.randint(49152,65535)
    data['params']['sport'] = random.randint(1000,4000)
    data['params']['client'] = "10.%d.%d.%d" % (random.randint(1, 254), random.randint(1, 254), random.randint(1, 254)) 
    data['params']['server'] = "10.%d.%d.%d" % (random.randint(1, 254), random.randint(1, 254), random.randint(1, 254)) 

    x = [random.randint(1e9, 2e9), random.randint(3e9, 4294967295)]
    random.shuffle(x)
    data['params']['sn1'] = x[0] 
    data['params']['sn2'] = x[1]

    data['params']['l1'] = random.randint(5, 512)

    types = ['S', 'F', 'A', 'D']
    inc = [1, 1, 0, data['params']['l1']]


    data['params']['sit'] = random.choice(types)
    for i, t in enumerate(types):
        if data['params']['sit']==t:
            data['params'][t] = True
            data['correct_answers']['seq'] = data['params']['sn1'] + inc[i]
        else:
            data['params'][t] = False

