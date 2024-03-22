
from pl_helpers import name, points, not_repeated
from code_feedback import Feedback
from pl_unit_test import PLTestCaseWithPlot, PLTestCase


class Test(PLTestCaseWithPlot):

    student_code_file = 'hello_world.py'

    @points(1)
    @name('test stuff')
    def test_a_stuff(self):
        msg = f"Hi, everybody!"
        Feedback.add_feedback(msg)
        Feedback.add_feedback(data)
