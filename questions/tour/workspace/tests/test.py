from pl_helpers import name, points, not_repeated, extract_ipynb_contents
from pl_unit_test import PLTestCaseWithPlot, PLTestCase
from code_feedback import Feedback
from functools import wraps
import numpy as np
import numpy.random
import os


class Test(PLTestCase):

    student_code_file = 'Workbook.ipynb'

    @points(1)
    @name('Checking x')
    def test_1(self):
        if Feedback.check_scalar('x', self.ref.x, self.st.x):
            Feedback.set_score(1)
        else:
            Feedback.set_score(0)
