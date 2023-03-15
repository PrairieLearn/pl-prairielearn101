class GPIO_class:

    pinDict = {
            16: 0,
            12: 0,
            7:  0,
            8:  0,
            25: 0,
            24: 0,
            23: 0,
            18: 0,
            15: 0,
            14: 0
        }

    HIGH = 1
    LOW = 0

    def output(self, pin, val):
        self.pinDict[pin] = val

# These are available to students (via names_for_user)
GPIO = GPIO_class()
PINS = list(GPIO.pinDict.keys())

# This is to be used by the answer code
ansDict = GPIO.pinDict.copy()