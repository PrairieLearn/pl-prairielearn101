#!/usr/bin/python3
import random, string
from logicExpression import *


# returns True if the argument given by premises (a list of Expressions) 
# and the conclusion (one Expression) is valid
def isValid(premises, conclusion):
	# check validity (when all premises True, the conclusion is True)
	for v1 in [False, True]:
		for v2 in [False, True]:
			for v3 in [False, True]:
				for v4 in [False, True]:
					for v5 in [False, True]:
					    for v6 in [False, True]:
					        for v7 in [False, True]:
					            # and all premises values
					            value = True
					            for p in premises:
					                value = value and p.calculateTruthValue(v1, v2, v3, v4, v5, v6, v7)
					            # if all premises are True, and conclusion is False, it is not valid
					            if value and not conclusion.calculateTruthValue(v1, v2, v3, v4, v5, v6, v7):
					                return False
	return True


# returns True if the argument given by premises (a list of Expressions) 
# and the conclusion (one Expression) is a contradiction
# conclusion not used
def isContradiction(premises, conclusion):
	# check validity (when all premises True, the conclusion is True)
	for v1 in [False, True]:
		for v2 in [False, True]:
			for v3 in [False, True]:
				for v4 in [False, True]:
					for v5 in [False, True]:
					    for v6 in [False, True]:
					        for v7 in [False, True]:
					            # and all premises values
					            value = True
					            for p in premises:
					                value = value and p.calculateTruthValue(v1, v2, v3, v4, v5, v6, v7)
					            # if all premises are True, it is not a contradiction
					            if value:
					                return False
	return True


# create an argument with num premises and a conclusion
# return a list with num+1 Expressions (conclusion is the last one) 
# using var_names, a list of variables names, as variables
# the argument can randomly be valid or invalid 
def createArgument(num, var_names):
	argument = []
	exp = Expression(None, None, None, None)
	for i in range(num):
		n = random.randint(1,2)
		exp = exp.randomExpression(n, var_names)
		argument.append(exp)
	exp = exp.randomExpression(1, var_names)
	argument.append(exp)
	return argument


# check if conc is the conclusion of using SPEC in exp
def isSpecialization(exp, conc):
	if exp.name == "and" and exp.num_neg == 0:
		if exp.var1.isEqual(conc) or exp.var2.isEqual(conc):
			return True
	return False

# check if conc is the conclusion of using GEN in exp
def isGeneralization(exp, conc):
	if conc.name == "or":
		if conc.var1.isEqual(exp) or conc.var2.isEqual(exp):
			return True
	return False

# check if conc is the conclusion of using CONTD in exp
def isContradictionRule(exp, conc):
	if exp.name == "imp" and exp.num_neg == 0:
		not_exp = exp.var1.copySubExpression()
		not_exp.negatesExpression()
		if not_exp.isEqual(conc) and exp.var2.name == "F":
			return True
	return False

# check if conc is the conclusion of using CONJ in exp1 and exp2
def isConjunction(exp1, exp2, conc):
	if conc.name == "and" and conc.num_neg == 0:
		if conc.var1.isEqual(exp1) and conc.var2.isEqual(exp2):
			return True
		elif conc.var1.isEqual(exp2) and conc.var2.isEqual(exp1):
			return True
	return False

# check if conc is the conclusion of using ELIM in exp1 and exp2
def isElimination(exp1, exp2, conc):
	if exp1.name == "or":
		not_exp = exp1.var1.copySubExpression()
		not_exp.negatesExpression()
		not_exp.removeDoubleNegation()
		no_dneg_exp2 = exp2.copySubExpression()
		no_dneg_exp2.removeDoubleNegation()
		if exp1.var2.isEqual(conc) and not_exp.isEqual(no_dneg_exp2):
			return True
		not_exp = exp1.var2.copySubExpression()
		not_exp.negatesExpression()
		not_exp.removeDoubleNegation()
		no_dneg_exp2 = exp2.copySubExpression()
		no_dneg_exp2.removeDoubleNegation()
		if exp1.var1.isEqual(conc) and not_exp.isEqual(no_dneg_exp2):
			return True
	if exp2.name == "or":
		not_exp = exp2.var1.copySubExpression()
		not_exp.negatesExpression()
		not_exp.removeDoubleNegation()
		no_dneg_exp1 = exp1.copySubExpression()
		no_dneg_exp1.removeDoubleNegation()
		if exp2.var2.isEqual(conc) and not_exp.isEqual(no_dneg_exp1):
			return True
		not_exp = exp2.var2.copySubExpression()
		not_exp.negatesExpression()
		not_exp.removeDoubleNegation()
		no_dneg_exp1 = exp1.copySubExpression()
		no_dneg_exp1.removeDoubleNegation()
		if exp2.var1.isEqual(conc) and not_exp.isEqual(no_dneg_exp1):
			return True
	return False

# check if conc is the conclusion of using M.TOL in exp1 and exp2
def isModusTollens(exp1, exp2, conc):
	if exp1.name == "imp":
		not_exp1 = exp1.var1.copySubExpression()
		not_exp1.negatesExpression()
		not_exp1.removeDoubleNegation()
		not_exp2 = exp1.var2.copySubExpression()
		not_exp2.negatesExpression()
		not_exp2.removeDoubleNegation()
		no_dneg_exp2 = exp2.copySubExpression()
		no_dneg_exp2.removeDoubleNegation()
		no_dneg_conc = conc.copySubExpression()
		no_dneg_conc.removeDoubleNegation()
		if not_exp1.isEqual(no_dneg_conc) and not_exp2.isEqual(no_dneg_exp2):
			return True
	if exp2.name == "imp":
		not_exp1 = exp2.var1.copySubExpression()
		not_exp1.negatesExpression()
		not_exp1.removeDoubleNegation()
		not_exp2 = exp2.var2.copySubExpression()
		not_exp2.negatesExpression()
		not_exp2.removeDoubleNegation()
		no_dneg_exp1 = exp1.copySubExpression()
		no_dneg_exp1.removeDoubleNegation()
		no_dneg_conc = conc.copySubExpression()
		no_dneg_conc.removeDoubleNegation()
		if not_exp1.isEqual(no_dneg_conc) and not_exp2.isEqual(no_dneg_exp1):
			return True
	return False

# check if conc is the conclusion of using M.PON in exp1 and exp2
def isModusPonens(exp1, exp2, conc):
	if exp1.name == "imp":
		if exp1.var1.isEqual(exp2) and exp1.var2.isEqual(conc):
			return True
	if exp2.name == "imp":
		if exp2.var1.isEqual(exp1) and exp2.var2.isEqual(conc):
			return True
	return False

# check if conc is the conclusion of using TRANS in exp1 and exp2
def isTransitivity(exp1, exp2, conc):
	if exp1.name == "imp" and exp2.name == "imp" and conc.name == "imp":
		if exp1.var2.isEqual(exp2.var1) and exp2.var2.isEqual(conc.var2) and exp1.var1.isEqual(conc.var1):
			return True
		if exp2.var2.isEqual(exp1.var1) and exp1.var2.isEqual(conc.var2) and exp2.var1.isEqual(conc.var1):
			return True
	return False

# check if conc is the conclusion of using CASE in exp1 and exp2
def isProofByCases(exp1, exp2, conc):
	if exp1.name == "imp" and exp2.name == "imp" and conc.name == "imp":
		if exp1.var2.isEqual(exp2.var2) and conc.var1.name == "or":
			if exp1.var1.isEqual(conc.var1.var1) and exp2.var1.isEqual(conc.var1.var2):
				return True
			elif exp2.var1.isEqual(conc.var1.var1) and exp1.var1.isEqual(conc.var1.var2):
				return True
	return False

# check if conc is the conclusion of using RES in exp1 and exp2
def isResolution(exp1, exp2, conc):
	if exp1.name == "or" and exp2.name == "or" and conc.name == "or":
		not_exp1 = exp1.var1.copySubExpression()
		not_exp1.negatesExpression()
		not_exp2 = exp2.var1.copySubExpression()
		not_exp2.negatesExpression()
		if not_exp1.isEqual(exp2.var1) or not_exp2.isEqual(exp1.var1):
			if (exp1.var2.isEqual(conc.var1) and exp2.var2.isEqual(conc.var2)) or (exp2.var2.isEqual(conc.var1) and exp1.var2.isEqual(conc.var2)):
			    return True
	return False


