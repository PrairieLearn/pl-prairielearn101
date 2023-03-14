import copy

speed = data['params']['speed']

class pigpio_class: 
    


    # pi.hardware_PWM(13, 50, 500000) 
    pwmDict = {
            12: {'freq': None, 'duty': None},
            13: {'freq': None, 'duty': None},
            0: {'units': speed*10000}
    }
    

    def hardware_PWM(self, pin, freq, duty):
        self.pwmDict[pin]['freq'] = freq
        self.pwmDict[pin]['duty'] = duty


class GPIO_class:

    HIGH = 1
    LOW = 0
    HIGHZ = -1

    IN  = -1
    OUT = 0
    ALT    = 1

    BCM = 1

    mode = 0


    
    pinDict = {
            1:  {'mode': -1, 'value': -1},
            2:  {'mode': -1, 'value': -1},
            3:  {'mode': -1, 'value': -1},
            4:  {'mode': -1, 'value': -1},
            5:  {'mode': -1, 'value': -1},
            6:  {'mode': -1, 'value': -1},
            7:  {'mode': -1, 'value': -1},
            8:  {'mode': -1, 'value': -1},
            9:  {'mode': -1, 'value': -1},
            10: {'mode': -1, 'value': -1},
            11: {'mode': -1, 'value': -1},
            12: {'mode': -1, 'value': -1},
            13: {'mode': -1, 'value': -1},
            14: {'mode': -1, 'value': -1},
            15: {'mode': -1, 'value': -1},
            16: {'mode': -1, 'value': -1},
            17: {'mode': -1, 'value': -1},
            18: {'mode': -1, 'value': -1},
            19: {'mode': -1, 'value': -1},
            20: {'mode': -1, 'value': -1},
            21: {'mode': -1, 'value': -1},
            22: {'mode': -1, 'value': -1},
            23: {'mode': -1, 'value': -1},
            24: {'mode': -1, 'value': -1},
            25: {'mode': -1, 'value': -1},
            26: {'mode': -1, 'value': -1},
            27: {'mode': -1, 'value': -1}
        }


    def setmode(self, m):
        if m==self.BCM:
            mode = self.BCM

    def setup(self, pin, mode, initial=0):
        self.pinDict[pin]['mode']=mode
        if mode==self.OUT:
            self.pinDict[pin]['value'] = initial

    def output(self, pin, val):
        if self.pinDict[pin]['mode']==self.OUT:
            self.pinDict[pin]['value'] = val

# These are available to students (via names_for_user)
GPIO = GPIO_class()
pi   = pigpio_class()

# This is to be used by the answer code
ansDict = copy.deepcopy(GPIO.pinDict)
ansDictPwm = copy.deepcopy(pi.pwmDict)


