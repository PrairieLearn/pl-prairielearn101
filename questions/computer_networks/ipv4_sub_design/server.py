import random, copy
import utilIAP as iap
import numpy as np

def generate(data):
    
    # problem parameters
    if random.choice([0,1]):
        data['params']['subnet'] = random.choice([random.randint(129,254), random.randint(12, 125)])
        data['params']['rangemin'] = "10.1.%d.0" % data['params']['subnet'] 
        data['params']['rangemax'] = "10.1.%d.255" % data['params']['subnet'] 
        data['params']['nhosts'] = random.sample([random.randint(17, 27), random.randint(33,59), random.randint(66, 120)], k=3)
    else:
        data['params']['subnet'] = random.choice([random.randint(129,254), random.randint(12, 125)])
        data['params']['rangemin'] = "10.1.%d.0" % data['params']['subnet'] 
        data['params']['rangemax'] = "10.1.%d.127" % data['params']['subnet'] 
        data['params']['nhosts'] = random.sample([random.randint(17, 27), random.randint(33,59), random.randint(9, 11)], k=3)


    
    # given number of hosts, get max prefix length and corresponding netmask for each LAN
    data['params']['prefix'] = [iap.nhosts_to_prefix_length(n) for n in data['params']['nhosts']]
    data['params']['mask']   = [iap.prefix_length_to_subnet(n) for n in data['params']['prefix']]
    
    # intialize network addresses to bottom of range, but don't keep it like that!
    data['params']['netaddr'] = [data['params']['rangemin'], data['params']['rangemin'], data['params']['rangemin']]
    
    # figuring out network addresses
    # go from largest to smallest LAN, get number of hosts in each LAN and overall
    net_order = np.argsort(data['params']['prefix'])
    hosts_per_lan = 2**(32-np.array( data['params']['prefix'] ))
    hosts_cum_sum = np.cumsum(hosts_per_lan[net_order])
    # then increment network address by number of hosts in previous LAN
    range_min_int = iap.ip_dotdec_to_int( data['params']['rangemin'] )
    range_top_net = [0, 0, 0]

    for i in range(3):
        range_top_net[net_order[i]] = range_min_int + hosts_cum_sum[i] - 1
        
    data['params']['netaddr'] = [iap.netaddr_dotdec( iap.ip_int_to_dotdec(range_top_net[i]),  data['params']['prefix'][i] ) for i in range(3) ]

    data['params']['bcastaddr'] =  [iap.bcaddr_dotdec(data['params']['netaddr'][i], data['params']['prefix'][i]) for i in range(3)]
    data['params']['minaddr'] =  [iap.min_ip_in_subnet(data['params']['netaddr'][i], data['params']['prefix'][i]) for i in range(3)]
    data['params']['maxaddr'] =  [iap.max_ip_in_subnet(data['params']['netaddr'][i], data['params']['prefix'][i]) for i in range(3)]
    

    
def parse(data):
    
    # remove whitespace
    for tag in data['submitted_answers'].keys():
        data['submitted_answers'][tag] = data['submitted_answers'][tag].strip()
    
def grade(data):
    
    # easiest check: number of hosts per LAN should match params
    sub_ans_tags = ["lana-netmask", "lanb-netmask", "lanc-netmask"]
    
    sub_OK = [False, False, False]
    sub_mask = ["", "", ""]
    prefix = [0, 0, 0]
    
    for i in range(3):
        
        ans = sub_ans_tags[i]
        
        # check if dotted decimal value
        if iap.is_dotdec(data['submitted_answers'][ans]):
            
            # check if a valid subnet mask
            if iap.is_subnet_mask(data['submitted_answers'][ans]):
                
                sub_OK[i] = True  # then the subnet mask is at least valid enough to check other stuff!
                
                # check if subnet supports enough hosts
                prefix[i] = iap.subnet_to_prefix_length(data['submitted_answers'][ans])
                if 2**(32-prefix[i] ) >= data['params']['nhosts'][i] + 2:
                    
                    data["partial_scores"][ans]['score']  = 1
                    sub_mask[i] = data['submitted_answers'][ans]
                    
                    if iap.subnet_to_prefix_length(data['submitted_answers'][ans]) < iap.subnet_to_prefix_length(data['correct_answers'][ans]):
                        data['feedback'][ans] = "%s is a valid subnet, but is bigger than is strictly required. If you use subnets that are too big, you may not be able to satisfy some other constraints of the problem (for example: you may not be able to keep everything within the permitted IP range, or you may not be able to support the number of hosts required on a different LAN.)"  % (data["submitted_answers"][ans])

                
                else: # not enough hosts in subnet
                    data["partial_scores"][ans]['score']  = 0
                    data['feedback'][ans] = "%s supports fewer than the required number of host addresses (%d)." % (data["submitted_answers"][ans], data['params']['nhosts'][i])

            
            else: # not a valid subnet mask
            
                data["partial_scores"][ans]['score']  = 0
                data['feedback'][ans] = "%s is not a valid subnet mask." % (data["submitted_answers"][ans])


        else: # not a dotted decimal value     
            data["partial_scores"][ans]['score']  = 0
            if len(data['submitted_answers'][ans]):
                data['feedback'][ans] = "%s is not a valid subnet mask in dotted decimal notation." % (data["submitted_answers"][ans])
    
    # first: make sure none of the assigned addresses are outside the range!
    range_min_int = iap.ip_dotdec_to_int( data['params']['rangemin'] )
    range_max_int = iap.ip_dotdec_to_int( data['params']['rangemax'] )
    

    ip_ans_tags = [['lana-network', 'lana-small', 'lana-large', 'lana-broadcast'],
                    ['lanb-network', 'lanb-small', 'lanb-large', 'lanb-broadcast'],
                    ['lanc-network', 'lanc-small', 'lanc-large', 'lanc-broadcast']]
                    
                    
    net_OK = [False, False, False]
    net_addr = ["", "", ""]
    bcast_addr = ["", "", ""]
    
    for i in range(3): # loop over 3 LANs
        
        for ans in ip_ans_tags[i]:
    
            # check if dotted decimal value
            if iap.is_dotdec(data['submitted_answers'][ans]):
    
                # check if is in acceptable range 
                if range_min_int <= iap.ip_dotdec_to_int(data['submitted_answers'][ans]) <= range_max_int:
                    
                    # check if network addresses are all network addresses
                    if "network" in ans and sub_OK[i]:
                        
                        # it's at least OK enough to check broadast add etc.
                        net_OK[i] = True
                        net_addr[i] = data['submitted_answers'][ans]
        
                        # network address is correct
                        if data['submitted_answers'][ans]==iap.netaddr_dotdec(data['submitted_answers'][ans], prefix[i]):
                            data["partial_scores"][ans]['score']  = 1
                        
                        else: # not a network address for given subnet mask
                            data["partial_scores"][ans]['score']  = 0
                            data["feedback"][ans] =  "%s is not a valid network address, given the specified subnet mask (%s). A network address should have a 0 bit at each position where the subnet mask is also 0." % (data["submitted_answers"][ans], sub_mask[i])


                    # check smallest addresses 
                    if "small" in ans and sub_OK[i] and net_OK[i]:
                        if iap.ip_dotdec_to_int( data['submitted_answers'][ans] ) == (iap.ip_dotdec_to_int(net_addr[i]) + 1):
                            data["partial_scores"][ans]['score']  = 1

                        else: # not a smallest address for given subnet mask and network address
                            data["partial_scores"][ans]['score']  = 0
                            data["feedback"][ans] =  "%s is not the smallest address for the given network address (%s) and subnet mask (%s)." % (data["submitted_answers"][ans], net_addr[i], sub_mask[i])
                            
                    # check largest addresses 
                    if "large" in ans and sub_OK[i] and net_OK[i]:
                        if iap.ip_dotdec_to_int( data['submitted_answers'][ans] ) == (iap.ip_dotdec_to_int(net_addr[i]) + 2**(32-prefix[i]) -2 ):
                            data["partial_scores"][ans]['score']  = 1

                        else: # not a largest address for given subnet mask and network address
                            data["partial_scores"][ans]['score']  = 0
                            data["feedback"][ans] =  "%s is not the largest address for the given network address (%s) and subnet mask (%s)." % (data["submitted_answers"][ans], net_addr[i], sub_mask[i])
                            
                    # check if bcast addresses are all bcast addresses
                    if "broadcast" in ans and sub_OK[i] and net_OK[i]:
                        if data['submitted_answers'][ans]==iap.bcaddr_dotdec( net_addr[i], prefix[i] ):
                            data["partial_scores"][ans]['score']  = 1
                            bcast_addr[i] = data['submitted_answers'][ans]

                            # check that LANs do not overlap TODO
                            # if currently on LAN B, and LAN A and LAN B both specified completely, 
                            # check that LAN A and LAN B do not overlap
                            if i == 1 and all(net_OK[0:2]) and all(bcast_addr[0:2]): 
                                x =  range(iap.ip_dotdec_to_int(net_addr[i]), iap.ip_dotdec_to_int(bcast_addr[i])  + 1) 
                                y =  range(iap.ip_dotdec_to_int(net_addr[i-1]), iap.ip_dotdec_to_int(bcast_addr[i-1])  + 1) 
                                if not set(x).isdisjoint(y):
                                    for a in ip_ans_tags[i]:
                                        data["partial_scores"][a]['score']  = 0
                                        data["feedback"][a] = "LAN B overlaps with LAN A. Each LAN must use a disjoint address space."
                                    data["partial_scores"][sub_ans_tags[i]]['score']  = 0
                                    data["feedback"][sub_ans_tags[i]] = "LAN B overlaps with LAN A. Each LAN must use a disjoint address space."


                            # on last iteration only
                            if i == 2:
                                if all(net_OK[1:3]) and all(bcast_addr[1:3]): 
                                    # check that LAN C and LAN B do not overlap
                                    x =  range(iap.ip_dotdec_to_int(net_addr[i]), iap.ip_dotdec_to_int(bcast_addr[i])  + 1) 
                                    y =  range(iap.ip_dotdec_to_int(net_addr[i-1]), iap.ip_dotdec_to_int(bcast_addr[i-1])  + 1) 
                                    if not set(x).isdisjoint(y):
                                        for a in ip_ans_tags[i]:
                                            data["partial_scores"][a]['score']  = 0
                                            data["feedback"][a] = "LAN C overlaps with LAN B. Each LAN must use a disjoint address space."
                                        data["partial_scores"][sub_ans_tags[i]]['score']  = 0
                                        data["feedback"][sub_ans_tags[i]] = "LAN C overlaps with LAN B. Each LAN must use a disjoint address space."
                                        
                                if all([net_OK[0], net_OK[2]]) and all([bcast_addr[0], bcast_addr[2]]):
                                    # check that LAN C and LAN A do not overlap
                                    x =  range(iap.ip_dotdec_to_int(net_addr[i]), iap.ip_dotdec_to_int(bcast_addr[i])  + 1) 
                                    y =  range(iap.ip_dotdec_to_int(net_addr[i-2]), iap.ip_dotdec_to_int(bcast_addr[i-2])  + 1) 
                                    if not set(x).isdisjoint(y):
                                        for a in ip_ans_tags[i]:
                                            data["partial_scores"][a]['score']  = 0
                                            data["feedback"][a] = "LAN C overlaps with LAN A. Each LAN must use a disjoint address space."
                                        data["partial_scores"][sub_ans_tags[i]]['score']  = 0
                                        data["feedback"][sub_ans_tags[i]] = "LAN C overlaps with LAN A. Each LAN must use a disjoint address space."


                        else: # not a broadcast address for given subnet mask and network address
                            data["partial_scores"][ans]['score']  = 0
                            data["feedback"][ans] =  "%s is not the broadcast address for the given network address (%s) and subnet mask (%s)." % (data["submitted_answers"][ans], net_addr[i], sub_mask[i])



                    
                else: # not in IP address range
                
                    data["partial_scores"][ans]['score']  = 0
                    data["feedback"][ans] =  "%s is not within the address range %s-%s" % (data["submitted_answers"][ans], data['params']['rangemin'], data['params']['rangemax'])
                    
            else: # not a dotted decimal value          
                data["partial_scores"][ans]['score']  = 0
                if len(data['submitted_answers'][ans]):
                    data["feedback"][ans] =  "%s is not a valid address in dotted decimal notation." % (data["submitted_answers"][ans])
            
    # update overall score
    data['score'] = sum([data["partial_scores"][ans]['weight']*data["partial_scores"][ans]['score'] for ans in data["partial_scores"].keys()])/len(data["partial_scores"])