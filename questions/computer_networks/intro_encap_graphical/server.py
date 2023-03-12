import random, copy

def generate(data):
    data['params']['opt'] = random.choice([ 
        {'name': "application-layer message",   'ans': ["true", "false", "false", "false"]}, 
        {'name': "transport-layer segment",     'ans': ["false", "true", "false", "false"] }, 
        {'name': "network-layer datagram",      'ans': ["false", "false", "true", "false"]}, 
        {'name': "link-layer frame",            'ans': ["false", "false", "false", "true"]}
        ])
    data['params']['net'] = random.choice(["IPv4", "IPv6"])
    data['params']['link'] = random.choice(["Ethernet", "802.11"])
    data['params']['trans'] = random.choice(["TCP", "UDP"])