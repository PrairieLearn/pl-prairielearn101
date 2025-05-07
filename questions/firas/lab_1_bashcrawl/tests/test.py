import numpy as np
from code_feedback import Feedback
from pl_helpers import name, points
from pl_unit_test import PLTestCase


class Test(PLTestCase):
    student_code_file = "example.py"

    @points(10)
    @name("Check the Magic Number!")
    def test_1(self):
        user_val = Feedback.call_user(self.st.magic_number, 1)
        if Feedback.check_scalar("magic_number()", self.ref.magic_number(10101010), user_val):
            Feedback.set_score(1)
        else:
            Feedback.set_score(0)