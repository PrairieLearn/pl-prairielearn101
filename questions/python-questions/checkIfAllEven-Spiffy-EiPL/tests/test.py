import unittest, math, random, json, pltest
from pltest import name, points
from bin.student_code import foo

class Test(unittest.TestCase):
    @points(1)
    @name("Checking foo([1, 1, 1, 1])")
    def test_one(self):
        self.assertEqual(foo([1, 1, 1, 1]), False)

    @points(1)
    @name("Checking foo([2, 2, 2, 2])")
    def test_two(self):
        self.assertEqual(foo([2, 2, 2, 2]), True)

    @points(1)
    @name("Checking foo([1, 2, 3, 4, 5])")
    def test_three(self):
        self.assertEqual(foo([1, 2, 3, 4, 5]), False)

    @points(1)
    @name("Checking foo([2, 4, 6, 8])")
    def test_four(self):
        self.assertEqual(foo([2, 4, 6, 8]), True)
