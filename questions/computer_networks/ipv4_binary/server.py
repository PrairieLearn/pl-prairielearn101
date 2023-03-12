import random, copy
import utilIAP as iap

def generate(data):

    data['params']['ip'] = "%d.%d.%d.%d" % ( random.choice( [random.randint(12, 120), random.randint(121, 170), random.randint(174, 218)] ), 
                                             random.randint(4, 250), 
                                             random.randint(4, 250), 
                                             random.randint(4, 250)) # "10.189.24.12"
                                             
    data['params']['prefix'] = random.randint(9, 28)
    data['params']['netmask'] = iap.prefix_length_to_subnet(data['params']['prefix'])  # "255.255.255.128"
    
    data['params']['bcaddr'] = iap.bcaddr_dotdec(data['params']['ip'], data['params']['prefix'])
    data['params']['netaddr'] = iap.netaddr_dotdec(data['params']['ip'], data['params']['prefix'])

    # if selected IP is a broadcast or network address, change it    
    if data['params']['ip']==data['params']['netaddr'] or data['params']['ip']==data['params']['bcaddr'] :
        # compute range
        net_add = iap.ip_dotdec_to_int(data['params']['netaddr'])
        net_max = net_add + int('1'*(32-data['params']['prefix']), base=2)-2
        net_min = net_add + 2
        data['params']['ip'] = iap.ip_int_to_dotdec(random.randint(net_min, net_max))
    

    data['params']['ip_bin'] = [str(format(int(x, base=10), '08b')) for x in data['params']['ip'].split('.')]
    data['params']['netmask_bin'] = [str(format(int(x, base=10), '08b')) for x in data['params']['netmask'].split('.')]
    
    
    # recompute network address and broadcast address in case these changed
    data['params']['netaddr'] = iap.netaddr_dotdec(data['params']['ip'] , iap.subnet_to_prefix_length(data['params']['netmask']) )
    data['params']['netaddr_bin'] = [str(format(int(x, base=10), '08b')) for x in data['params']['netaddr'].split('.')]
    data['params']['bcaddr'] = iap.bcaddr_dotdec(data['params']['ip'] , iap.subnet_to_prefix_length(data['params']['netmask']) )
    data['params']['bcaddr_bin'] = [str(format(int(x, base=10), '08b')) for x in data['params']['bcaddr'].split('.')]
    data['params']['minaddr'] = iap.ip_int_to_dotdec( iap.ip_dotdec_to_int( data['params']['netaddr'] ) + 1 )
    data['params']['maxaddr'] = iap.ip_int_to_dotdec( iap.ip_dotdec_to_int( data['params']['bcaddr'] ) - 1 )
    
    data['correct_answers']['netaddr']  = data['params']['netaddr'] 
    data['correct_answers']['bcaddr']   = data['params']['bcaddr'] 
    data['correct_answers']['minaddr'] = data['params']['minaddr']
    data['correct_answers']['maxaddr'] = data['params']['maxaddr']