import random, copy

def generate(data):

    data['params'] = random.choice([
        {'protocol': 'Ethernet', 'next': 'protocol', 'correctField': 'Frame Type', 'wrongField': ["Destination Address", "Source Address", "Data", "CRC"], 'nextProtocol': 'network', 'wrongProtocol': ["application", "transport", "link"]},
        {'protocol': 'IPv4', 'next': 'protocol', 'correctField': 'Protocol', 'wrongField': ["Identification", "Destination IP Address", "Flags"], 'nextProtocol': 'transport', 'wrongProtocol': ["network", "application", "link"]},
        {'protocol': 'UDP', 'next': 'application or service', 'correctField': 'Destination Port', 'wrongField': ["Source Port", "Message Length", "Checksum"], 'nextProtocol': 'application', 'wrongProtocol': ["network", "transport", "link"]},
        ])
        
        
