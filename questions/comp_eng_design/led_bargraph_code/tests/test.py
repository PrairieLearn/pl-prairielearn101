from pl_helpers import name, points, not_repeated
from pl_unit_test import PLTestCase
from code_feedback import Feedback
from functools import wraps
import random
import json


class Test(PLTestCase):
    @points(2)
    @name("8bars")
    def test_0(self):
        # setup code is executed, student code is executed, and it goes into st
        # setup code is executed, answer code is executed, and it goes into ref
        correct = 1
        Feedback.call_user(self.ref.write_bar, self.ref.PINS, 8)        
        Feedback.call_user(self.st.write_bar,  self.ref.PINS, 8)       
        studAns = self.ref.GPIO.pinDict
        myAns   = self.ref.ansDict
        for p in self.ref.PINS:
           if studAns[p] != myAns[p]:
               Feedback.add_feedback('When calling write_bar(PINS,8), the result was incorrect.')
               Feedback.add_feedback("Expected result was: %s" % json.dumps(myAns))
               Feedback.add_feedback("Your result was    : %s" % json.dumps(studAns))
               correct = 0
               break
        Feedback.set_score(correct)

    @points(4)
    @name("4bars")
    def test_1(self):
        # setup code is executed, student code is executed, and it goes into st
        # setup code is executed, answer code is executed, and it goes into ref
        correct = 1
        Feedback.call_user(self.ref.write_bar, self.ref.PINS, 8)        
        Feedback.call_user(self.st.write_bar,  self.ref.PINS, 8)       
        Feedback.call_user(self.ref.write_bar, self.ref.PINS, 4)        
        Feedback.call_user(self.st.write_bar,  self.ref.PINS, 4)       
        studAns = self.ref.GPIO.pinDict
        myAns   = self.ref.ansDict
        for p in self.ref.PINS:
           if studAns[p] != myAns[p]:
               Feedback.add_feedback('When calling write_bar(PINS,8) followed by write_bar(PINS,4), the result was incorrect.')
               Feedback.add_feedback("Expected result was: %s" % json.dumps(myAns))
               Feedback.add_feedback("Your result was    : %s" % json.dumps(studAns))
               correct = 0
               break
        Feedback.set_score(correct)


    @points(4)
    @name("sequence")
    def test_2(self):
        # setup code is executed, student code is executed, and it goes into st
        # setup code is executed, answer code is executed, and it goes into ref
        correct = 1
        Feedback.call_user(self.ref.write_bar, self.ref.PINS, 10)        
        Feedback.call_user(self.st.write_bar,  self.ref.PINS, 10)       
        Feedback.call_user(self.ref.write_bar, self.ref.PINS, 0)        
        Feedback.call_user(self.st.write_bar,  self.ref.PINS, 0)       
        i = random.randint(0,10)
        Feedback.call_user(self.ref.write_bar, self.ref.PINS, i)        
        Feedback.call_user(self.st.write_bar,  self.ref.PINS, i)   

        studAns = self.ref.GPIO.pinDict
        myAns   = self.ref.ansDict
        for p in self.ref.PINS:
           if studAns[p] != myAns[p]:
               Feedback.add_feedback("When calling this sequence, the result was incorrect: ")
               Feedback.add_feedback("write_bar(PINS, 10), write_bar(PINS, 0), write_bar(PINS, %d)" % i)
               Feedback.add_feedback("Expected result was: %s" % json.dumps(myAns))
               Feedback.add_feedback("Your result was    : %s" % json.dumps(studAns))
               correct = 0
               break
        Feedback.set_score(correct)
