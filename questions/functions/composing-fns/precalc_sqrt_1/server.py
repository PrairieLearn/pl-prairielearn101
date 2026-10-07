import prairielearn as pl
import sympy as sp
import random
from sympy.parsing.sympy_parser import (
    parse_expr,
    standard_transformations,
    implicit_multiplication_application,
    convert_xor,
    rationalize,
    function_exponentiation,
    implicit_application,
    implicit_multiplication
)

# Utility function
def remove_leading_one_mul(expr):
    if isinstance(expr, sp.Mul):
        args = [a for a in expr.args if a != 1]
        return sp.Mul(*[remove_leading_one_mul(a) for a in args], evaluate=False)
    elif isinstance(expr, sp.Add):
        return sp.Add(*[remove_leading_one_mul(a) for a in expr.args], evaluate=False)
    elif isinstance(expr, sp.Pow):
        return sp.Pow(remove_leading_one_mul(expr.base), remove_leading_one_mul(expr.exp), evaluate=False)
    return expr

# Utility function
def parse_st_expr(data, var_name):
    transformations = standard_transformations + (
        rationalize,
        implicit_multiplication_application,
        convert_xor,
        
        function_exponentiation,
        implicit_application,
        implicit_multiplication
    )
    if var_name not in data["format_errors"]:
        st_expr = parse_expr(data["raw_submitted_answers"][var_name], transformations=transformations, evaluate=False)
        return remove_leading_one_mul(st_expr)
    
def generate(data):
    A = random.choice([5,7,9])
    B = random.choice([2,3,4,5])
    
    x = sp.symbols("x", commutative=True)
    
    expression = (x + B*x**(sp.Rational(A,2)))/(sp.root(x,2))
    data["params"]["expression"] = sp.latex(expression)
    data["correct_answers"]["expr"] = pl.to_json(x**(sp.Rational(1,2)) + B*x**(sp.Rational(A-1,2)))
    
def grade(data):
    if data["partial_scores"]["expr"]["score"] == 1:
        st_answer = parse_st_expr(data, "expr")
        terms = st_answer.as_ordered_terms()
        if len(terms) != 2:
            data["partial_scores"]["expr"]["score"] = 0
            data["feedback"]["expr"] = "You have not simplified the expression correctly."
            pl.set_weighted_score_data(data)
            return
        
        
        for term in terms:
            if str(term) == "x**(1/2)":
                pass
            if str(term) != str(sp.cancel(term)):
                data["partial_scores"]["expr"]["score"] = 0
                data["feedback"]["expr"] = "You have not simplified the expression correctly."
                pl.set_weighted_score_data(data)
                return 
            # power simp
            if str(term) != str(sp.powsimp(term)):

                data["partial_scores"]["expr"]["score"] = 0
                data["feedback"]["expr"] = "You have not simplified the expression correctly."
                pl.set_weighted_score_data(data)
                return
        
        data["feedback"]["expr"] = "You have simplified the expression correctly."
        
        return