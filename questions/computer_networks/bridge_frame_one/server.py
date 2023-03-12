import random, copy
import utilIAP as iap

def generate(data):

    macs = iap.macs(2)
    ports = random.sample([1,2,3,4], k=2)
    data['params']['macs'] = macs
    data['params']['ports'] = ports

    optsSrc = [
        {'desc1': 'There is already an entry in the bridge forwarding table for', 'desc2': 'associated with port ' + str(ports[0]), 'tags': ["false", "false", "true"]},
        {'desc1': 'There is no entry for', 'desc2': 'in the bridge forwarding table',                            'tags': ["false", "true", "false"]}
        ]

    optsDst =  [
        {'dst': macs[1], 'desc': "is associated with port " + str(ports[0]) + " in the bridge forwarding table",                               'tags': ["true", "false", "false", "false", "false"]},
        {'dst': "ff:ff:ff:ff:ff:ff", 'desc': "is the broadcast address",                                                  'tags': ["false", "false", "true", "false", "false"]},
        {'dst': macs[1], 'desc': "is not in the bridge forwarding table",                                     'tags': ["false", "false", "true", "false", "false"]},
        {'dst': macs[1], 'desc': "is associated with port " + str(ports[1]) + " in the bridge forwarding table",                               'tags': ["false", "false", "false", "true", "false"]}
        ]

        
    data['params']['src'] = random.choice(optsSrc)
    data['params']['dst'] = random.choice(optsDst)