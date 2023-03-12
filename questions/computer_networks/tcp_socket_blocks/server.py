import random, copy

def generate(data):
    
    x = random.sample(range(11,99), 8)
    data['params']['ip'] = "%d.%d.%d.%d" % (x[0], x[1], x[2], x[3])
    data['params']['bindip'] = "%d.%d.%d.%d" % (x[4], x[5], x[6], x[7])
    data['params']['port'] = random.choice(range(3000, 9000))
    data['params']['msg'] = "Hello"
    
    ch = random.choice(["tx", "rx"])
    if ch == "tx":
        data['params']['tx'] = True
        data['params']['rx'] = False
    else:
        data['params']['rx'] = True
        data['params']['tx'] = False
