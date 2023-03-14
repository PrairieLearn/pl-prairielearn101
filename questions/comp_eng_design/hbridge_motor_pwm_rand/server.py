import random, copy, numpy, base64

def generate(data):
    
    data['params']['speed'] = random.choice([15, 20, 25, 30, 35, 40, 45, 50])

    data["params"]["names_for_user"] = [
        {"name": "GPIO", "description": "RPi GPIO library", "type": "object"},
        {"name": "pi", "description": "Instance of a pigpio", "type": "object"},
        {"name": "speed", "description": "Speed at which to move in partial speed", "type": "integer"},
    ]
    
    data["params"]["names_from_user"] = [
        {"name": "setup", "description": "Set up GPIO pins. Motors should be off/stopped at the end of this function.", "type": "function"},
        {"name": "motor_forward_full", "description": "Go at full speed in forward direction. Accepts an integer argument that is a motor index: 0 for Motor A and 1 for Motor B.", "type": "function"},
        {"name": "motor_forward_slow", "description": "Go at " +  str(data['params']['speed']) + "% speed in forward direction (using hardware PWM). Accepts an integer argument that is a motor index: 0 for Motor A and 1 for Motor B.", "type": "function"},
        {"name": "motor_reverse_full", "description": "Go at full speed in reverse direction. Accepts an integer argument that is a motor index: 0 for Motor A and 1 for Motor B.", "type": "function"},
        {"name": "motor_reverse_slow", "description": "Go at " +  str(data['params']['speed']) + "% speed in reverse direction (using hardware PWM). Accepts an integer argument that is a motor index: 0 for Motor A and 1 for Motor B.", "type": "function"},
        {"name": "motor_stop", "description": "Stop motor. Accepts an integer argument that is a motor index: 0 for Motor A and 1 for Motor B.", "type": "function"}
    ]

    #def grade(data):
    #print(data['score'])
    #fileAnswer = data['submitted_answers']['_files'][0]['contents']
    #fileDecoded = base64.b64decode(fileAnswer)
    #print(dir(fileDecoded))
    #lines = base64.b64decode(bytes(fileAnswer, encoding='utf8')).split('\n')
    #print(lines[-2])
    #print(fileLines[-1])
