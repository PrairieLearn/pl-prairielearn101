import random, copy
import utilIAP as iap
import numpy as np

# directly connected: 17.14.28.20/24 (Internet)
# directly connected: 10.0.0.64/26
# directly connected: 10.0.0.160/30
# directly connected: 10.0.0.164/30

def generate(data):
    
    data['params']['routes'] = [
        {'dest': "0.0.0.0",     'prefix': 0,    'netmask': '0.0.0.0',                       'gw': '17.14.28.1',    'flags': 'UG','iface': 'eth0', 'k': 0},  # always matches
        {'dest': "17.14.28.0",  'prefix': 24,   'netmask': iap.prefix_length_to_subnet(24), 'gw': '0.0.0.0',       'flags': 'U', 'iface': 'eth0', 'k': 1},  # only specific WAN
        {'dest': "10.0.0.64",   'prefix': 26,   'netmask': iap.prefix_length_to_subnet(26), 'gw': '0.0.0.0',       'flags': 'U', 'iface': 'eth1', 'k': 2},  # matches 10.0.0.65 - 10.0.0.126
        {'dest': "10.0.0.160",  'prefix': 30,   'netmask': iap.prefix_length_to_subnet(30), 'gw': '0.0.0.0',       'flags': 'U', 'iface': 'eth2', 'k': 3},  # 10.0.0.162 (router-a)
        {'dest': "10.0.0.164",  'prefix': 30,   'netmask': iap.prefix_length_to_subnet(30), 'gw': '0.0.0.0',       'flags': 'U', 'iface': 'eth3', 'k': 4},  # 10.0.0.165 (router-c)
        {'dest': "10.0.0.0",    'prefix': 24,   'netmask': iap.prefix_length_to_subnet(24), 'gw': '10.0.0.165',    'flags': 'UG','iface': 'eth3', 'k': 5},  # matches 10.0.0.1 - 10.0.0.254, but especially 194-222, 34-62, 66-94
        {'dest': "10.0.0.160",  'prefix': 28,   'netmask': iap.prefix_length_to_subnet(28), 'gw': '10.0.0.165',    'flags': 'UG','iface': 'eth3', 'k': 6},  # matches 10.0.0.161 - 10.0.0.174, but especially 10.0.0.169, 170, 173, 174
        {'dest': "10.0.0.128",  'prefix': 26,   'netmask': iap.prefix_length_to_subnet(26), 'gw': '10.0.0.162',    'flags': 'UG','iface': 'eth2', 'k': 7}   # matches 10.0.0.129 - 10.0.0.190
        ]
        
        
    netAdds = [r['dest'] for r in data['params']['routes']] # don't use a network address as destination

    choices = [
        {'address': "10.0.0.162"}, # router-a
        {'address': "10.0.0.165"}, # router-c
        {'address': "10.0.0.%s" % random.choice([169, 170, 173, 174]) }, # router-d or router-e
        {'address': "10.0.0.%s" % random.randint(66,126) }, # lan B
        {'address': "10.0.0.%s" % random.randint(170, 188) }, # lan A
        {'address': "10.0.0.%s" % random.randint(34, 62) }, # lan D
        {'address': "10.0.0.%s" % random.randint(66, 94) }, # lan E
        {'address': "10.0.0.%s" % random.randint(194, 222) } # lan C
        ]
        

        
    data['params']['sol'] = random.choice(choices)
    data['params']['sol']['matches'] = [ "", "", "", "", "", "", "", "" ]


    
    # add binary representation, for explanation
    data['params']['addressbin'] = iap.ip_dotdec_to_binstr_sp(data['params']['sol']['address'])

    

    # also add binary representation, for explanation
    for i,r in enumerate(data['params']['routes']):
        data['params']['routes'][i]['destbin'] = iap.ip_dotdec_to_binstr_sp(data['params']['routes'][i]['dest'])
        data['params']['routes'][i]['netmaskbin'] = iap.ip_dotdec_to_binstr_sp(data['params']['routes'][i]['netmask'])
        data['params']['routes'][i]['andresult'] = iap.ip_dotdec_to_binstr_sp( iap.netaddr_dotdec(data['params']['sol']['address'], data['params']['routes'][i]['prefix'] ) )
        if data['params']['routes'][i]['andresult'] == data['params']['routes'][i]['destbin']:
            data['params']['sol']['matches'][i] = "true"
        else:
            data['params']['sol']['matches'][i] = "false"

    data['params']['solRoutes'] = [data['params']['routes'][i] for i,m in enumerate(data['params']['sol']['matches']) if m=="true"]
    idx_match = np.argmax([ x['prefix'] for x in data['params']['solRoutes'] ])

    data['params']['finalRoute'] = data['params']['solRoutes'][idx_match]
    #print(data['params']['finalRoute'])

    data['params']['rule'] = [{'name': i, 'tag': 'false'} if i!=data['params']['finalRoute']['k'] else {'name': i, 'tag': 'true'} for i in range(0,7+1) ]
    data['params']['iface'] = [{'name': i, 'tag': 'false'} if i!=data['params']['finalRoute']['iface'] else {'name': i, 'tag': 'true'} for i in ['eth0', 'eth1', 'eth2', 'eth3']]
    
    # if a direct route
    if data['params']['finalRoute']['gw']=="0.0.0.0":
         data['params']['finalRoute'] = ""
