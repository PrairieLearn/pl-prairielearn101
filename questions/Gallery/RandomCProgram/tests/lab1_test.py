#! /usr/bin/python3

import sys, math, sympy

import cgrader

class Lab1Grader(cgrader.CGrader):

    def tests(self):
        t = sympy.symbols('t')
        formula = sympy.sympify(self.data['params']['xstr'])

        self.test_compile_file('position.c', 'position')

        for tval in [1, 0, 2, 0.5, 1.5, math.pi]:
            x = formula.subs(t, tval)
            self.test_run('./position', '%s\n' % tval, '%0.3f' % x)

g = Lab1Grader()
g.start()
