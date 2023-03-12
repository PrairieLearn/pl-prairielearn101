import random, copy, sympy
import prairielearn as pl

def generate(data):

    a = random.randint(1, 9)
    b = random.randint(2, 7)
    c = random.randint(1, 7)
    d = random.randint(1, 3)
    e = random.randint(1, 3)
    f = random.randint(2, 7)
    g = random.randint(1, 7)
    h = random.randint(1, 3)
    i = random.randint(1, 3)
    j = random.randint(5, 9)    
    
    t = sympy.symbols('t')
    x = a * sympy.sqrt(t) / b * sympy.sin(c * t) ** d + \
        sympy.Rational(e, f) * sympy.cos(g * t) ** h + \
        sympy.Rational(i, j) ** t

    data['params']['x'] = sympy.latex(x)
    data['params']['xstr'] = str(x)
