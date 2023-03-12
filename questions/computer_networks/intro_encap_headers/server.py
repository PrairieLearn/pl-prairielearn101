import random, copy

def generate(data):
    # as it is sent down from the transport layer
    # as it is sent down from the network layer
    # as it is sent down from the link layer
    data['params']['desc'] = random.choice([
        {"name": "the TCP segment", 'ans': ["false", "false", "true", "true", "false", "false"], 'isTCP': True, 'isIP': False, 'isEthernet': False}, 
        {"name": "the IP datagram", 'ans': ["false", "true", "true", "true", "false", "false"],  'isTCP': False, 'isIP': True, 'isEthernet': False}, 
        {"name": "the Ethernet frame", 'ans': ["true", "true", "true", "true", "true", "false"], 'isTCP': False, 'isIP': False, 'isEthernet': True}
        ]
        )

