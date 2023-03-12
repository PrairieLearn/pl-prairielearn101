import random, copy
import utilIAP as iap

def generate(data):
    
    # generate a random prefix length and compute netmask
    data['params']['prefix'] = random.randint(16, 29)
    data['params']['netmask'] = iap.netmask_from_prefix(data['params']['prefix'])
    
    # generate a random IP address
    oct1 = random.choice([10, 192])
    if oct1 == 10:
        data['params']['address'] = "10.%d.%d.%d" % (random.randint(4, 250), random.randint(4, 250), random.randint(4, 250))
    else:
        data['params']['address'] = "192.168.%d.%d" % (random.randint(4, 250), random.randint(4, 250))

    # compute some addresses inside range
    ips = iap.ips_in_subnet(data['params']['address'], data['params']['prefix'] , 3)
    data['params']['address'] = ips[2]

    # get broadcast address and network address
    data['params']['bcast'] = iap.bcaddr_dotdec(data['params']['address'], data['params']['prefix'])
    net_add_dotdec = iap.netaddr_dotdec(data['params']['address'], data['params']['prefix'])
    
    
    # compute range
    net_add = iap.ip_dotdec_to_int(net_add_dotdec)
    net_max = net_add + int('1'*(32-data['params']['prefix']), base=2)-2
    net_min = net_add + 2
    

    
    # compute some addresses inside range
    ip_yes1 = ips[0]
    if data['params']['prefix'] < 24:
        ip_yes_bc = int(iap.ip_dotdec_to_binstr(data['params']['address']) [0:data['params']['prefix']] + '0'*(32-data['params']['prefix']), base=2) + 255
        ip_yes2 = iap.ip_int_to_dotdec(ip_yes_bc)
    else: 
        ip_yes2 = ips[1]
        
    if ip_yes2 == data['params']['address']:
        ip_yes2 = ips[1]

    # compute some addresses outside of range        
    ip_no_1 = iap.ip_int_to_dotdec( iap.ip_dotdec_to_int(data['params']['bcast']) + random.randint(2, 255) )
    ip_no_2 = iap.ip_int_to_dotdec( net_add - random.randint(2, 255) )

    data['params']['choices'] = [{'ans': ip_yes1, 'tag': 'true'}, {'ans': ip_yes2, 'tag': 'true'}, {'ans': ip_no_1, 'tag': 'false'}, {'ans': ip_no_2, 'tag': 'false'}]
    data['correct_answers']['prefix'] = data['params']['prefix']
    data['correct_answers']['network'] = net_add_dotdec + '/' + str(data['params']['prefix'])
    data['correct_answers']['bcast'] = data['params']['bcast']
    data['correct_answers']['netaddr'] = net_add_dotdec
    
    data['params']['netmask_bin'] = iap.ip_dotdec_to_binstr_sp( data['params']['netmask']  )
    data['params']['maskinv_bin'] = ''.join(['1' if s=='0' else '0' if  s=="1" else " " for s in data['params']['netmask_bin']])
    data['params']['address_bin'] = iap.ip_dotdec_to_binstr_sp( data['params']['address']  )
    data['params']['netaddr_bin'] = iap.ip_dotdec_to_binstr_sp( net_add_dotdec  )
    data['params']['bcast_bin'] = iap.ip_dotdec_to_binstr_sp( data['params']['bcast']  )
    data['params']['min_ip'] = iap.min_ip_in_subnet(data['params']['address'], data['params']['prefix'])
    data['params']['max_ip'] = iap.max_ip_in_subnet(data['params']['address'], data['params']['prefix'])
