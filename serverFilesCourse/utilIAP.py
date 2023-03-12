import random
import numpy as np

IAP_NAMES = ['floyd', 'dijkstra', 'perlman', 'knuth', 'cerf', 'hopper', 'lovelace', 'baran', 'shannon', 'roberts', 'kleinrock', 'kahn']

def netmask_from_prefix(prefix):
    # convert a prefix length to netmask 
    # e.g. 24 to "255.255.255.0"
    mask_bin = '1'*prefix + '0'*(32-prefix)
    mask_dotdec = "%d.%d.%d.%d" % (int(mask_bin[0:8], base=2), 
                                    int(mask_bin[8:16], base=2), 
                                    int(mask_bin[16:24], base=2), 
                                    int(mask_bin[24:32], base=2))
    return mask_dotdec

def ip_dotdec_to_binstr(ip):
    # convert IP address from dotted decimal string to binary string
    # e.g. "192.168.10.120" to "11000000101010000000101001111000"
    return ''.join([str(format(int(x, base=10), '08b')) for x in ip.split('.')])

def ip_dotdec_to_binstr_sp(ip):
    # convert IP address from dotted decimal string to binary string with spaces
    # e.g. "192.168.10.120" to "11000000 10101000 00001010 01111000"
    return ' '.join([str(format(int(x, base=10), '08b')) for x in ip.split('.')])


def ip_dotdec_to_hex_sp(ip):
    # convert IP address from dotted decimal string to hex string with spaces
    return ' '.join([str(format(int(x, base=10), '02x')) for x in ip.split('.')])

def ip_binstr_to_dotdec(ip):
    # convert IP address from binary string to dotted decimal string
    # e.g. "11000000101010000000101001111000" to "192.168.0.120"
    return "%d.%d.%d.%d" % (int(ip[0:8], base=2), 
                            int(ip[8:16], base=2), 
                            int(ip[16:24], base=2), 
                            int(ip[24:32], base=2))

def ip_binstr_to_int(ip):
    # convert IP address from 32-length binary string to integer
    # e.g. "11000000101010000000101001111000" to 3232238200
    return int(ip, base=2)

def ip_int_to_binstr(ip):
    # convert IP address from integer to 32-length binary string
    # e.g. 3232238200 to "11000000101010000000101001111000"
    return format(ip, '032b')

def ip_int_to_dotdec(ip):
    # convert IP address from integer to dotted decimal
    # e.g. 3232238200 to "192.168.0.120"
    return ip_binstr_to_dotdec(ip_int_to_binstr(ip))

def ip_dotdec_to_int(ip):
    # convert IP address from dotted decimal to integer
    # e.g. "192.168.0.120" to 3232238200
    return ip_binstr_to_int(ip_dotdec_to_binstr(ip))

def netaddr_dotdec(ip, prefix):
    # given IP address (dotted decimal) and prefix length (integer),
    # returns network address. e.g. from "192.168.10.24" and 24,
    # returns "192.168.10.0"
    net_add_int = int( ip_dotdec_to_binstr(ip)[0:prefix] + '0'*(32-prefix), base=2)
    net_add_bin = format(net_add_int, '032b')
    net_add_dotdec = "%d.%d.%d.%d" % (int(net_add_bin[0:8], base=2), 
                                        int(net_add_bin[8:16], base=2), 
                                        int(net_add_bin[16:24], base=2),
                                        int(net_add_bin[24:32], base=2))
    return net_add_dotdec

def bcaddr_dotdec(ip, prefix):
    # given IP address (dotted decimal) and prefix length (integer),
    # returns broadcast address. e.g. from "192.168.0.24" and 24,
    # returns "192.168.10.255"
    bcast_bin = ip_dotdec_to_binstr(ip)[0:prefix] + '1'*(32-prefix)
    bcast_dotdec = ip_binstr_to_dotdec(bcast_bin)
    return bcast_dotdec

def ips_in_subnet(ip, prefix, n):
    # given an IP address and prefix, returns n IP addresses in that subnet
    netaddr = ip_dotdec_to_int( netaddr_dotdec(ip, prefix) )
    bcaddr  = ip_dotdec_to_int(  bcaddr_dotdec(ip, prefix) )
    hosts = random.sample(range(netaddr+2, bcaddr-2), n)
    return [ip_int_to_dotdec(h) for h in hosts]

def min_ip_in_subnet(ip, prefix):
    # given an IP address and prefix, return smallest host address in that subnet
    netaddr = ip_dotdec_to_int( netaddr_dotdec(ip, prefix) )
    return ip_int_to_dotdec(netaddr + 1)

def max_ip_in_subnet(ip, prefix):
    # given an IP address and prefix, return largest host address in that subnet
    bcaddr  = ip_dotdec_to_int(  bcaddr_dotdec(ip, prefix) )
    return ip_int_to_dotdec(bcaddr - 1)

def is_in_subnet(test_ip, ip, prefix):
    # given an IP address (in dot dec), and another address and prefix,
    # returns True if the first address is in the subnet described by the other two parameters
    netaddr = ip_dotdec_to_int( netaddr_dotdec(ip, prefix) )
    bcaddr  = ip_dotdec_to_int(  bcaddr_dotdec(ip, prefix) )
    testaddr = ip_dotdec_to_int(test_ip)
    return (netaddr < testaddr < bcaddr)

def range_subnet(ip, prefix):
    # given an IP address (in dot dec) and prefix,
    # returns a range() of the integer values of addresses in its subnet
    # including the network and broadcast addresses
    # this is useful for checking if subnets are disjoint
    netaddr = ip_dotdec_to_int( netaddr_dotdec(ip, prefix) )
    bcaddr  = ip_dotdec_to_int(  bcaddr_dotdec(ip, prefix) )
    return range(netaddr, bcaddr)

def is_dotdec(ip):
    # return True if it is valid dotted decimal notation
    # should be four integers between 0 and 255, separated by a .
    return isinstance(ip, str) and len(ip.split("."))==4 and all([i.isdigit() for i in ip.split(".")]) and all([0 <= int(i) <= 255 for i in ip.split(".")])

def hostnames(n):
    # return an array of n hostnames
    return random.sample(IAP_NAMES, n)   

def macs(n):
    # return an array of n unicast MAC addresses
    marr = []
    for i in range(n):
        m = "%s:%02x:%02x:%02x" % (
            random.choice(['52:54:00', '00:50:56', '00:16:3e', '00:ca:fe', '00:15:5d', '3c:52:82']),
                              random.randint(0, 255),
                             random.randint(0, 255),
                             random.randint(0, 255))
        marr.append(m)
    return marr

def hosts_in_subnet(ip, prefix, n):
    # return an array of n dictionaries, where each dictionary has a hostname, 
    # a MAC address, and an IP address in it (for a given subnet)
    iparr = ips_in_subnet(ip, prefix, n)
    marr = macs(n)
    narr = hostnames(n)
    return [{"name": i, "mac": j, "ip": k} for i,j,k in zip(narr, marr, iparr)]


def prefix_length_to_subnet(n):
    # given a prefix length, returns subnet mask in 
    # dotted decimal notation
    mask = '1'*n + '0'*(32-n)
    return "%d.%d.%d.%d" % (int(mask[0:8], base=2),
            int(mask[8:16], base=2),
            int(mask[16:24], base=2),
            int(mask[24:32], base=2))

def is_subnet_mask(ip):
    # return true if dotted decimal IP is a valid subnet mask
    masks = [prefix_length_to_subnet(i) for i in range(8,32)]
    return ip in masks

def subnet_to_prefix_length(ip):
    # return prefix length from subnet
    if is_subnet_mask(ip):
        return ip_dotdec_to_binstr(ip).count('1')
    else:
        return 0

def nhosts_to_prefix_length(n):
    # given some number of hosts, what is the largest prefix length
    # that supports that number of hosts? returns integer
    return int(32-np.ceil(np.log2(n)))

def multicast_ip_to_mac(ip):
    # given an IP address in dotted decimal notation, returns the 
    # MAC address assuming it is a multicast address
    bs = '00000001' + '00000000' + '01011110' + '0' + ip_dotdec_to_binstr(ip)[32-23:]
    mac = ':'.join(["%02x" % int(bs[i:i+8], base=2) for i in range(0, len(bs), 8)])
    return mac

def multicast_ip(type='any'):
    # returns a random multicast IP in dotted decimal
    # if type is 'any', can be anything in 224.0.0.0/4
    # if type is 'admin', will be within admin scope block 239.0.0./8
    # if type is 'local', will be within local scope block 224.0.0.0/24
    # if type is 'org', will be within organization scope block 239.255.0.0/16
    if type=="any":
        return hosts_in_subnet("224.0.0.0", 4, 1)[0]['ip']
    elif type=="local":
        return hosts_in_subnet("224.0.0.0", 24, 1)[0]['ip']
    elif type=="admin":
        return hosts_in_subnet("239.0.0.0", 8, 1)[0]['ip']
    elif type=='org':
        return hosts_in_subnet("239.255.0.0", 16, 1)[0]['ip']
