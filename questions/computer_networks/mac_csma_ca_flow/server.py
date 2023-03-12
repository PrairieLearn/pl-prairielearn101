import random, copy
def generate(data):


    opts = [
        {"situation": "the host has some data to send, and it has sensed the medium to be free for one DIFS time interval", 'answer': 'tx'},
        {"situation": "the host has some data to send, and it has sensed that the medium and observed that it is busy", 'answer': 'sense-busy'},
        {"situation": "the host has data to send, is sensing the medium in random backoff after previously finding the medium busy, and it has just detected a transmission", 'answer': 'freeze'},
        {"situation": "the host has sent a frame", 'answer': 'waitack'},
        {"situation": "the host has sent a frame and received an ACK", 'answer': 'complete'},
        {"situation": "the host has received a frame and verified that its CRC is OK", 'answer': 'ack'},
        {"situation": "the host has data to send, but it has been through multiple backoff iterations, and has not found an idle channel even after the maximum contention window", 'answer': 'abort'},
        {"situation": "the host has sent some data but has not received an ACK within the timeout interval", 'answer': 'retx'}
        ]

    data['params']['desc'] = random.choice(opts)
    
    data['params']['ans'] = {s['answer']: s['answer']==data['params']['desc']['answer'] for s in opts}
        
    #    data['params']['desc'] = random.choice([
    #    {"situation": "senses the medium to find no free slot of length >=DIFS", 'ans': ["true","false","false","false"]}, 
    #    {"situation": "senses the medium to find a free slot of length >=DIFS", 'ans': ["false","true","false","false"]}, 
    #    {"situation": "transmits a frame but receives no ACK within a timeout window", 'ans': ["false","false","true","false"]}, 
    #    {"situation": "transmits a frame and receives an ACK shortly after", 'ans': ["false","false","false","true"]}, 
    #    ]
    #   )