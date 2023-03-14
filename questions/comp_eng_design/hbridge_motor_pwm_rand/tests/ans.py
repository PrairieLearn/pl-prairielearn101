MOTOR_A_EN = 12
MOTOR_A_POS = 5
MOTOR_A_NEG = 6
MOTOR_B_EN = 13
MOTOR_B_POS = 23
MOTOR_B_NEG = 24



def setup():
    for p in [MOTOR_A_POS, MOTOR_A_NEG, MOTOR_B_POS, MOTOR_B_NEG]:
        ansDict[p]['mode'] = GPIO.OUT

def motor_A_speed(speed):
    ansDictPwm[MOTOR_A_EN]['freq'] = 50
    ansDictPwm[MOTOR_A_EN]['duty'] = speed*10000
    if speed >= 0:
        ansDict[MOTOR_A_POS]['value'] = GPIO.HIGH 
        ansDict[MOTOR_A_NEG]['value'] = GPIO.LOW 
    else:
        ansDict[MOTOR_A_POS]['value'] = GPIO.LOW 
        ansDict[MOTOR_A_NEG]['value'] = GPIO.HIGH 
        

def motor_B_speed(speed):
    ansDictPwm[MOTOR_B_EN]['freq'] = 50
    ansDictPwm[MOTOR_B_EN]['duty'] = speed*10000
    if speed >= 0:
        ansDict[MOTOR_B_POS]['value'] = GPIO.HIGH 
        ansDict[MOTOR_B_NEG]['value'] = GPIO.LOW 
    else:
        ansDict[MOTOR_B_POS]['value'] = GPIO.LOW 
        ansDict[MOTOR_B_NEG]['value'] = GPIO.HIGH 
