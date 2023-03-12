import random, copy
import sympy
import prairielearn as pl

def generate(data):

  x, y = sympy.symbols('x y')


  # Answer to fill in the blank input stored as JSON.
  data['correct_answers']['symbolic_ex'] = pl.to_json(x**2)
