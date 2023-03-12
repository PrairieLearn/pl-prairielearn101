import random, copy
import utilIAP as iap

def generate(data):

    data['params']['web'] = "http://example.org/"
    data['params']['webip'] = "93.184.216.34"
    data['params']['hostname'] = "example.org"
    sub = random.sample(range(11,99), k=2)
    data['params']['bcast'] = "10.%d.%d.255" % (sub[0], sub[1])
    hosts = iap.hosts_in_subnet("10.%d.%d.0" % (sub[0], sub[1]), 24, 5)
    data['params']['host'] = hosts[0]
    data['params']['dns'] = hosts[1]
    data['params']['dhcp'] = hosts[2]
    data['params']['gw'] = hosts[3]
    data['params']['gw']['ip'] = "10.%d.%d.1" % (sub[0], sub[1])
    
    data['params']['dnsport'] = random.randint(49152,65535)
    data['params']['dnstrans'] = random.randint(10e3, 60e3)
    
    data['params']['ids']    = random.sample(range(10000,65535), k=5) 
    data['params']['id-dnsack']  = data['params']['ids'][2] + 1
    data['params']['id-httpget'] = data['params']['ids'][0] + 1
    data['params']['xid'] = f"0x{random.randint(0, 0xFFFFFFFF):08x}"

    data['params']['isn1'] = random.randint(1e9, 4294967295)
    data['params']['ack1'] = data['params']['isn1'] + 1
    data['params']['isn2'] = random.randint(1e9, 4294967295)
    data['params']['ack2'] = data['params']['isn2'] + 1
    data['params']['seq3'] = data['params']['ack1']
    data['params']['ack3'] = data['params']['seq3'] + 138
    data['params']['seq4'] = data['params']['isn2']
    data['params']['ack4'] = data['params']['seq4'] + 1391
    data['params']['seq5'] = data['params']['ack3']
    data['params']['ack5'] = data['params']['seq5'] + 1
    data['params']['seq6'] = data['params']['ack4']
    data['params']['ack6'] = data['params']['seq6'] + 1
    data['params']['tcpport'] = random.randint(49152,65535)
