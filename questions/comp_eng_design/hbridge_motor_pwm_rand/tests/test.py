from pl_helpers import name, points, not_repeated
from pl_unit_test import PLTestCase
from code_feedback import Feedback
from functools import wraps
import random


MOTOR_A_IDX = 0
MOTOR_A_EN = 12
MOTOR_A_POS = 5
MOTOR_A_NEG = 6

MOTOR_B_IDX = 1
MOTOR_B_EN = 13
MOTOR_B_POS = 23
MOTOR_B_NEG = 24

class Test(PLTestCase):
    @points(2)
    @name("setup")
    def test_setup(self):


        # setup code is executed, student code is executed, and it goes into st
        # setup code is executed, answer code is executed, and it goes into ref
        correct = 1
        Feedback.call_user(self.st.setup)       
        studAns = self.ref.GPIO.pinDict
        # Check that GPIO pins are in output mode
        for p in [MOTOR_A_POS, MOTOR_A_NEG, MOTOR_B_POS, MOTOR_B_NEG]:
            if studAns[p]['mode'] != 0:
               correct = 0
               Feedback.add_feedback("Setup does not put pin %d in the expected mode (input, output, alt)" % p)
        #for p in [MOTOR_A_EN, MOTOR_B_EN]:
        #    if studAns[p]['mode'] == 0:
        #       correct -= 0.1
        #       Feedback.add_feedback("setup should not put pin %d in output mode, since it will be used for hardware PWM" % p )
        #if not ( (studAns[MOTOR_A_POS]['value'] == studAns[MOTOR_A_NEG]['value']) ):
        #       correct -= 0.1
        #       Feedback.add_feedback("setup does not leave motor A off" )
        #if not ( (studAns[MOTOR_B_POS]['value'] == studAns[MOTOR_B_NEG]['value']) ):
        #       correct -= 0.1
        #       Feedback.add_feedback("setup does not leave motor B off" )
        Feedback.set_score(correct)


    @points(4)
    @name("motor_forward_full")
    def test_fwd_full(self):

        # setup code is executed, student code is executed, and it goes into st
        # setup code is executed, answer code is executed, and it goes into ref
        correct = 0
        
         # check Motor A case
        speed = 0
        Feedback.call_user(self.st.setup)
        Feedback.call_user(self.st.motor_forward_full, 0)       
        studAns = self.ref.GPIO.pinDict
        studPwm   = self.ref.pi.pwmDict
        
        # option 1: turn on EN as output and also make POS HIGH and NEG LOW
        if studAns[MOTOR_A_POS]['mode']==0 and studAns[MOTOR_A_POS]['value']==1 and studAns[MOTOR_A_NEG]['mode']==0 and studAns[MOTOR_A_NEG]['value']==0 and studAns[MOTOR_A_EN]['mode']==0 and studAns[MOTOR_A_EN]['value']==1:
            correct += 0.5
        # option 2: turn on EN as PWM with 100% duty cycle and also make POS HIGH and NEG LOW
        elif studAns[MOTOR_A_POS]['mode']==0 and studAns[MOTOR_A_POS]['value']==1 and studAns[MOTOR_A_NEG]['mode']==0 and studAns[MOTOR_A_NEG]['value']==0 and studPwm[MOTOR_A_EN]['freq'] is not None and studPwm[MOTOR_A_EN]['duty'] is not None and studPwm[MOTOR_A_EN]['freq'] > 5 and int(studPwm[MOTOR_A_EN]['duty'])==1000000:
            correct += 0.5
        else:
            Feedback.add_feedback("motor_forward_full failed for motor A" )

         # check Motor B case
        speed = 0
        Feedback.call_user(self.st.setup)
        Feedback.call_user(self.st.motor_forward_full, 1)       
        studAns = self.ref.GPIO.pinDict
        studPwm   = self.ref.pi.pwmDict
        
        # option 1: turn on EN as output and also make POS HIGH and NEG LOW
        if studAns[MOTOR_B_POS]['mode']==0 and studAns[MOTOR_B_POS]['value']==1 and studAns[MOTOR_B_NEG]['mode']==0 and studAns[MOTOR_B_NEG]['value']==0 and studAns[MOTOR_B_EN]['mode']==0 and studAns[MOTOR_B_EN]['value']==1:
            correct += 0.5
        # option 2: turn on EN as PWM with 100% duty cycle and also make POS HIGH and NEG LOW
        elif studAns[MOTOR_B_POS]['mode']==0 and studAns[MOTOR_B_POS]['value']==1 and studAns[MOTOR_B_NEG]['mode']==0 and studAns[MOTOR_B_NEG]['value']==0 and studPwm[MOTOR_B_EN]['freq'] is not None and studPwm[MOTOR_B_EN]['duty'] is not None and studPwm[MOTOR_B_EN]['freq'] > 5 and int(studPwm[MOTOR_B_EN]['duty'])==1000000:
            correct += 0.5
        else:
            Feedback.add_feedback("motor_forward_full failed for motor B" )

        Feedback.set_score(correct)



    @points(4)
    @name("motor_reverse_full")
    def test_rev_full(self):

        # setup code is executed, student code is executed, and it goes into st
        # setup code is executed, answer code is executed, and it goes into ref
        correct = 0
        
         # check Motor A case
        Feedback.call_user(self.st.setup)
        Feedback.call_user(self.st.motor_reverse_full, 0)       
        studAns = self.ref.GPIO.pinDict
        studPwm   = self.ref.pi.pwmDict
        
        # option 1: turn on EN as output and also make POS LOW and NEG HIGH
        if studAns[MOTOR_A_POS]['mode']==0 and studAns[MOTOR_A_POS]['value']==0 and studAns[MOTOR_A_NEG]['mode']==0 and studAns[MOTOR_A_NEG]['value']==1 and studAns[MOTOR_A_EN]['mode']==0 and studAns[MOTOR_A_EN]['value']==1:
            correct += 0.5
        # option 2: turn on EN as PWM with 100% duty cycle and also make POS LOW and NEG HIGH
        elif studAns[MOTOR_A_POS]['mode']==0 and studAns[MOTOR_A_POS]['value']==0 and studAns[MOTOR_A_NEG]['mode']==0 and studAns[MOTOR_A_NEG]['value']==1 and studPwm[MOTOR_A_EN]['freq'] is not None and studPwm[MOTOR_A_EN]['duty'] is not None and studPwm[MOTOR_A_EN]['freq'] > 5 and int(studPwm[MOTOR_A_EN]['duty'])==1000000:
            correct += 0.5
        else:
            Feedback.add_feedback("motor_reverse_full failed for motor A" )

         # check Motor B case
        Feedback.call_user(self.st.setup)
        Feedback.call_user(self.st.motor_reverse_full, 1)       
        studAns = self.ref.GPIO.pinDict
        studPwm   = self.ref.pi.pwmDict
        
        # option 1: turn on EN as output and also make POS LOW and NEG HIGH
        if studAns[MOTOR_B_POS]['mode']==0 and studAns[MOTOR_B_POS]['value']==0 and studAns[MOTOR_B_NEG]['mode']==0 and studAns[MOTOR_B_NEG]['value']==1 and studAns[MOTOR_B_EN]['mode']==0 and studAns[MOTOR_B_EN]['value']==1:
            correct += 0.5
        # option 2: turn on EN as PWM with 100% duty cycle and also make POS LOW and NEG HIGH
        elif studAns[MOTOR_B_POS]['mode']==0 and studAns[MOTOR_B_POS]['value']==0 and studAns[MOTOR_B_NEG]['mode']==0 and studAns[MOTOR_B_NEG]['value']==1 and studPwm[MOTOR_B_EN]['freq'] is not None and studPwm[MOTOR_B_EN]['duty'] is not None and studPwm[MOTOR_B_EN]['freq'] > 5 and int(studPwm[MOTOR_B_EN]['duty'])==1000000:
            correct += 0.5
        else:
            Feedback.add_feedback("motor_reverse_full failed for motor B" )

        Feedback.set_score(correct)


    @points(4)
    @name("motor_reverse_slow")
    def test_rev_slow(self):

        # setup code is executed, student code is executed, and it goes into st
        # setup code is executed, answer code is executed, and it goes into ref
        correct = 0
        
         # check Motor A case
        Feedback.call_user(self.st.setup)
        Feedback.call_user(self.st.motor_reverse_slow, 0)       
        studAns = self.ref.GPIO.pinDict
        studPwm   = self.ref.pi.pwmDict
        
        # option 1: turn on EN as PWM with 10% duty cycle and also make POS LOW and NEG HIGH
        if studAns[MOTOR_A_POS]['mode']==0 and studAns[MOTOR_A_POS]['value']==0 and studAns[MOTOR_A_NEG]['mode']==0 and studAns[MOTOR_A_NEG]['value']==1 and studPwm[MOTOR_A_EN]['freq'] is not None and studPwm[MOTOR_A_EN]['duty'] is not None and studPwm[MOTOR_A_EN]['freq'] > 5 and int(studPwm[MOTOR_A_EN]['duty'])==studPwm[0]['units']:
            correct += 0.5
        else:
            Feedback.add_feedback("motor_reverse_slow failed for motor A" )

         # check Motor B case
        Feedback.call_user(self.st.setup)
        Feedback.call_user(self.st.motor_reverse_slow, 1)       
        studAns = self.ref.GPIO.pinDict
        studPwm   = self.ref.pi.pwmDict
        
        # option 1: turn on EN as PWM with 10% duty cycle and also make POS LOW and NEG HIGH
        if studAns[MOTOR_B_POS]['mode']==0 and studAns[MOTOR_B_POS]['value']==0 and studAns[MOTOR_B_NEG]['mode']==0 and studAns[MOTOR_B_NEG]['value']==1 and studPwm[MOTOR_B_EN]['freq'] is not None and studPwm[MOTOR_B_EN]['duty'] is not None and studPwm[MOTOR_B_EN]['freq'] > 5 and int(studPwm[MOTOR_B_EN]['duty'])==studPwm[0]['units']:
            correct += 0.5
        else:
            Feedback.add_feedback("motor_reverse_slow failed for motor B" )

        Feedback.set_score(correct)


    @points(4)
    @name("motor_forward_slow")
    def test_fwd_slow(self):

        # setup code is executed, student code is executed, and it goes into st
        # setup code is executed, answer code is executed, and it goes into ref
        correct = 0
        
         # check Motor A case
        speed = 0
        Feedback.call_user(self.st.setup)
        Feedback.call_user(self.st.motor_forward_slow, 0)       
        studAns = self.ref.GPIO.pinDict
        studPwm   = self.ref.pi.pwmDict
        
        # option 1: turn on EN as PWM with 10% duty cycle and also make POS HIGH and NEG LOW
        if studAns[MOTOR_A_POS]['mode']==0 and studAns[MOTOR_A_POS]['value']==1 and studAns[MOTOR_A_NEG]['mode']==0 and studAns[MOTOR_A_NEG]['value']==0 and studPwm[MOTOR_A_EN]['freq'] is not None and studPwm[MOTOR_A_EN]['duty'] is not None and studPwm[MOTOR_A_EN]['freq'] > 5 and int(studPwm[MOTOR_A_EN]['duty'])==studPwm[0]['units']:
            correct += 0.5
        else:
            Feedback.add_feedback("motor_forward_slow failed for motor A" )

         # check Motor B case
        speed = 0
        Feedback.call_user(self.st.setup)
        Feedback.call_user(self.st.motor_forward_slow, 1)       
        studAns = self.ref.GPIO.pinDict
        studPwm   = self.ref.pi.pwmDict
        
        # option 1: turn on EN as PWM with 10% duty cycle and also make POS HIGH and NEG LOW
        if studAns[MOTOR_B_POS]['mode']==0 and studAns[MOTOR_B_POS]['value']==1 and studAns[MOTOR_B_NEG]['mode']==0 and studAns[MOTOR_B_NEG]['value']==0 and studPwm[MOTOR_B_EN]['freq'] is not None and studPwm[MOTOR_B_EN]['duty'] is not None and studPwm[MOTOR_B_EN]['freq'] > 5 and int(studPwm[MOTOR_B_EN]['duty'])==studPwm[0]['units']:
            correct += 0.5
        else:
            Feedback.add_feedback("motor_forward_slow failed for motor B" )

        Feedback.set_score(correct)




    @points(2)
    @name("motor_stop")
    def test_stop(self):

        # setup code is executed, student code is executed, and it goes into st
        # setup code is executed, answer code is executed, and it goes into ref
        correct = 0

         # check motor A case
        Feedback.call_user(self.st.setup)
        Feedback.call_user(self.st.motor_stop, 0)       
        studAns = self.ref.GPIO.pinDict
        studPwm   = self.ref.pi.pwmDict
        
        # option 1: turn off by setting duty cycle to 0:
        if studPwm[MOTOR_A_EN]['freq'] is not None and studPwm[MOTOR_A_EN]['duty'] is not None and int(studPwm[MOTOR_A_EN]['duty'])==int(0):
            correct += 0.5
        # option 2: turn off by setting two pins equal
        elif studAns[MOTOR_A_POS]['value']==0 and studAns[MOTOR_A_NEG]['value']==0:
            correct += 0.5
        elif studAns[MOTOR_A_POS]['value']==1 and studAns[MOTOR_A_NEG]['value']==1:
            correct += 0.5
        # option 3: turn off by setting enable to output LOW
        elif studAns[MOTOR_A_EN]['mode']==0 and studAns[MOTOR_A_EN]['value']==0:
            correct += 0.5
        else:
            Feedback.add_feedback("stop failed for motor A" )

        
         # check motor B case
        Feedback.call_user(self.st.setup)
        Feedback.call_user(self.st.motor_stop, 1)       
        studAns = self.ref.GPIO.pinDict
        studPwm   = self.ref.pi.pwmDict
        
        # option 1: turn off by setting duty cycle to 0:
        if studPwm[MOTOR_B_EN]['freq'] is not None and studPwm[MOTOR_B_EN]['duty'] is not None and studAns[MOTOR_B_EN]['mode']!=0 and int(studPwm[MOTOR_B_EN]['duty'])==int(0):
            correct += 0.5
        # option 2: turn of by setting two pins equal
        elif studAns[MOTOR_B_POS]['value']==0 and studAns[MOTOR_B_NEG]['value']==0:
            correct += 0.5
        elif studAns[MOTOR_B_POS]['value']==1 and studAns[MOTOR_B_NEG]['value']==1:
            correct += 0.5
        # option 3: turn off by setting enable to output LOW
        elif studAns[MOTOR_A_EN]['mode']==0 and studAns[MOTOR_A_EN]['value']==0:
            correct += 0.5
        else:
            Feedback.add_feedback("stop failed for motor B" )
            
        Feedback.set_score(correct)
