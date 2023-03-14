import random, copy
import numpy as np

def generate(data):
    
    length = 50
    startx = 150 
    starty = 150

    angleChoices = [30, 25, 55, 60, 70, 85, 100, 105, 115, 120, 155, 160]
    angle = random.choice(angleChoices)
    data['params']['angle'] = angle    
    data['params']['endx'] = startx + length*np.cos(np.deg2rad(angle))
    data['params']['endy'] = starty - length*np.sin(np.deg2rad(angle))


    pin = 13
    onTime = (1 + 0.5*(angle/90.0))
    period = 20.0
    duty = onTime/period
    data['params']['duty'] = duty
    onUnits = int(duty*1e6)
    
    data['correct_answers']['period'] = period
    data['correct_answers']['pulse'] = onTime
    
    
