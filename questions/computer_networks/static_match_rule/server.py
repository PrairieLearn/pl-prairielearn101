import random, copy
import utilIAP as iap

def parse(data):
    data['format_errors'] = {}


def generate(data):
    
    # generate a random prefix length and compute netmask
    data['params']['prefix'] = random.choice([18,19,20,21,22,23,25,26,27,28])
    data['params']['netmask'] = iap.netmask_from_prefix(data['params']['prefix'])
    data['params']['iface'] = random.choice(["eth0", "eth1", "eth2", "eth3"])
    
    # generate a random IP address
    oct1 = random.choice([10, 192])
    if oct1 == 10:
        data['params']['address'] = "10.%d.%d.%d" % (random.randint(4, 250), random.randint(4, 250), random.randint(4, 250))
    else:
        data['params']['address'] = "192.168.%d.%d" % (random.randint(4, 250), random.randint(4, 250))

    # get broadcast address and network address
    data['params']['bcast'] = iap.bcaddr_dotdec(data['params']['address'], data['params']['prefix'])
    net_add_dotdec = iap.netaddr_dotdec(data['params']['address'], data['params']['prefix'])
    
    
    # compute range
    net_add = iap.ip_dotdec_to_int(net_add_dotdec)
    net_max = net_add + int('1'*(32-data['params']['prefix']), base=2)-2
    net_min = net_add + 2
    
    if data['params']['address']==net_add_dotdec or data['params']['address']==data['params']['bcast'] :
        data['params']['address'] = iap.ip_int_to_dotdec(random.randint(net_min, net_max))
    
    
    # compute some addresses inside range
    ips = iap.ips_in_subnet(net_add_dotdec, data['params']['prefix'] , 3)

    # compute some addresses outside of range        
    ip_no_1 = iap.ip_int_to_dotdec( iap.ip_dotdec_to_int(data['params']['bcast']) + random.randint(3, 15) )
    ip_no_2 = iap.ip_int_to_dotdec( net_add - random.randint(3, 5) )
    ip_no_3 = iap.ip_int_to_dotdec( net_add - random.randint(6, 10) )

    data['params']['choices'] = [{'ans': ips[0], 'tag': 'true'}, {'ans': ips[1], 'tag': 'true'}, {'ans': ips[2], 'tag': 'true'}, {'ans': ip_no_1, 'tag': 'false'}, {'ans': ip_no_2, 'tag': 'false'}, {'ans': ip_no_3, 'tag': 'false'}]
    data['correct_answers']['prefix'] = data['params']['prefix']
    data['correct_answers']['network'] = net_add_dotdec + '/' + str(data['params']['prefix'])
    data['correct_answers']['bcast'] = data['params']['bcast']
    data['correct_answers']['netaddr'] = net_add_dotdec
    

    data['params']['netaddr'] = net_add_dotdec
    
    
    data['params']['netmask_bin'] = iap.ip_dotdec_to_binstr_sp( data['params']['netmask']  )
    data['params']['maskinv_bin'] = ''.join(['1' if s=='0' else '0' if  s=="1" else " " for s in data['params']['netmask_bin']])

    data['params']['netaddr_bin'] = iap.ip_dotdec_to_binstr_sp( net_add_dotdec  )
    data['params']['bcast_bin'] = iap.ip_dotdec_to_binstr_sp( data['params']['bcast']  )

    

    
