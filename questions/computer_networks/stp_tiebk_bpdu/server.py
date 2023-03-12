import random, copy
import utilIAP as iap

def generate(data):

    macs = iap.macs(4)
    macs.sort()
    brports = ['8001', '8002', '8003', '8004']
    rpcost = ['100', '200', '300', '400']
    rpcostSame = random.choice(rpcost)
    
    opts = [
        {'root1': macs[0], 'root2': macs[1], 'id1': macs[3], 'id2': macs[2], 'rpc1': random.choice(rpcost), 'rpc2': random.choice(rpcost), 
          'port1': random.choice(brports), 'port2': random.choice(brports), 'wins': ["true", "false"], 'tags': ["true", "false", "false", "false"]}, # tiebreaker is on lowest root bridge ID, first BPDU wins
          
        {'root1': macs[1], 'root2': macs[0], 'id1': macs[3], 'id2':  macs[2], 'rpc1': random.choice(rpcost), 'rpc2': random.choice(rpcost), 
          'port1': random.choice(brports), 'port2': random.choice(brports), 'wins': ["false", "true"], 'tags': ["true", "false", "false", "false"]}, # tiebreaker is on lowest root bridge ID, second BPDU wins
          
        {'root1': macs[0], 'root2': macs[1], 'id1': macs[0], 'id2':  macs[2], 'rpc1': '0', 'rpc2': random.choice(rpcost), 
          'port1': random.choice(brports), 'port2': random.choice(brports), 'wins': ["true", "false"], 'tags': ["true", "false", "false", "false"]}, # tiebreaker is on lowest root bridge ID, first BPDU wins, sent by root bridge

        {'root1': macs[1], 'root2': macs[0], 'id1': macs[2], 'id2':  macs[0], 'rpc1': random.choice(rpcost), 'rpc2': '0', 
          'port1': random.choice(brports), 'port2': random.choice(brports), 'wins': ["false", "true"], 'tags': ["true", "false", "false", "false"]}, # tiebreaker is on lowest root bridge ID, second BPDU wins, sent by root bridge
          
        {'root1': macs[1], 'root2': macs[0], 'id1': macs[1], 'id2':  macs[0], 'rpc1': '0', 'rpc2': '0', 
          'port1': random.choice(brports), 'port2': random.choice(brports), 'wins': ["false", "true"], 'tags': ["true", "false", "false", "false"]}, # tiebreaker is on lowest root bridge ID, second BPDU wins, both sent by self
          
        {'root1': macs[0], 'root2': macs[0], 'id1': macs[3], 'id2': macs[2], 'rpc1': '100', 'rpc2': '200', 
          'port1': random.choice(brports), 'port2': random.choice(brports), 'wins': ["true", "false"], 'tags': ["false", "true", "false", "false"]}, # tiebreaker is on lowest root path cost, first BPDU wins

        {'root1': macs[0], 'root2': macs[0], 'id1': macs[3], 'id2': macs[2], 'rpc1': '400', 'rpc2': '300', 
          'port1': random.choice(brports), 'port2': random.choice(brports), 'wins': ["false", "true"], 'tags': ["false", "true", "false", "false"]}, # tiebreaker is on lowest root path cost, second BPDU wins

        {'root1': macs[0], 'root2': macs[0], 'id1': macs[3], 'id2': macs[2], 'rpc1': '200', 'rpc2': '300', 
          'port1': random.choice(brports), 'port2': random.choice(brports), 'wins': ["true", "false"], 'tags': ["false", "true", "false", "false"]}, # tiebreaker is on lowest root path cost, first BPDU wins

        {'root1': macs[0], 'root2': macs[0], 'id1': macs[3], 'id2': macs[2], 'rpc1': '200', 'rpc2': '100', 
          'port1': random.choice(brports), 'port2': random.choice(brports), 'wins': ["false", "true"], 'tags': ["false", "true", "false", "false"]}, # tiebreaker is on lowest root path cost, second BPDU wins


        {'root1': macs[0], 'root2': macs[0], 'id1': macs[2], 'id2': macs[3], 'rpc1': rpcostSame, 'rpc2': rpcostSame,
          'port1': random.choice(brports), 'port2': random.choice(brports), 'wins': ["true", "false"], 'tags': ["false", "false", "true", "false"]}, # tiebreaker is on lowest sender bridge ID, first BPDU wins

        {'root1': macs[0], 'root2': macs[0], 'id1': macs[3], 'id2': macs[1], 'rpc1': rpcostSame, 'rpc2': rpcostSame,
          'port1': random.choice(brports), 'port2': random.choice(brports), 'wins': ["false", "true"], 'tags': ["false", "false", "true", "false"]}, # tiebreaker is on lowest sender bridge ID, second BPDU wins


        {'root1': macs[0], 'root2': macs[0], 'id1': macs[1], 'id2': macs[1], 'rpc1': rpcostSame, 'rpc2': rpcostSame,
          'port1': brports[0], 'port2': brports[1], 'wins': ["true", "false"], 'tags': ["false", "false", "false", "true"]} # tiebreaker is on lowest sender port, first BPDU wins


        ]

    data['params'] = random.choice(opts)
    data['correct_answers']['root'] = '8000.' + macs[0]
    data['params']['designated'] = ["Bridge 8000." + data['params']['id1'] + ", port " + data['params']['port1'], "Bridge 8000." + data['params']['id2'] + ", port " + data['params']['port2']]