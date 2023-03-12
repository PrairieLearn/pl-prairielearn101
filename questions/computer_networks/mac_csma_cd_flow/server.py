import random, copy

def generate(data):

    opts = [
        {"situation": "the host has sent a frame and then detects a collision", 'answer': 'jam'},   # send a jamming signal and cease transmission
        {"situation": "the host has sent a frame, detected a collision, and sent a jamming signal", 'answer': 'backoff'},   # start the exponential backoff process
        {"situation": "the host has data to send", 'answer': 'sense'},  # sense to be sure the medium is idle before transmitting
        {"situation": "the host has found the medium to be idle, and transmitted a frame", 'answer': 'detect-collision'},   # sense to be sure there is no collision
        {"situation": "the host has data to send, is in the exponential backoff process, and has had 16 collisions as part of this process", 'answer': 'abort'},   # give up
        {"situation": "the host has sent a frame, sensed the medium afterward, and detected no collision", 'answer': 'complete'},   # nothing else to do
        {"situation": "the host has data to send, has sensed the medium, and found it idle", 'answer': 'tx'},  # transmit the data
        {"situation": "the host has data to send, has sensed the medium, and found it busy", 'answer': 'wait-idle'}  # wait for the medium to be idle
        ]

    data['params']['desc'] = random.choice(opts)
    
    data['params']['ans'] = {s['answer']: s['answer']==data['params']['desc']['answer'] for s in opts}
    