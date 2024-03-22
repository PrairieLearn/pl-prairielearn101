#!/usr/bin/python3
import random, string
from logicExpression import *



# Check if exp1 and exp2 match I
# p^T = p
# pvF = p
# T^p = p
# Fvp = p
def checkI(exp1, exp2):
	e1 = exp1.copySubExpression()
	e2 = exp2.copySubExpression()
	if e2.num_neg >= e1.num_neg:
		e2.num_neg -= e1.num_neg
	if e1.name == "and":
		if e1.var1 == None or e1.var2 == None:
			return False
		elif e1.var1.isEqual(e2) and e1.var2.name == "T":
			return True
		elif e1.var2.isEqual(e2) and e1.var1.name == "T":
			return True
		else:
			return False
	elif e1.name == "or":
		if e1.var1 == None or e1.var2 == None:
			return False
		elif e1.var1.isEqual(e2) and e1.var2.name == "F":
			return True
		elif e1.var2.isEqual(e2) and e1.var1.name == "F":
			return True
		else:
			return False
	else:
		return False


# Check if exp1 and exp2 match UB
# p^F = F
# pvT = T
# F^p = F
# Tvp = T
def checkUB(exp1, exp2):
	if exp1.name == "and" and exp1.num_neg == exp2.num_neg:
		if exp1.var1 == None or exp1.var2 == None:
			return False
		elif exp1.var1.name == "F" and exp2.name == "F":
			return True
		elif exp1.var2.name == "F" and exp2.name == "F":
			return True
		else:
			return False
	elif exp1.name == "or" and exp1.num_neg == exp2.num_neg:
		if exp1.var1 == None or exp1.var2 == None:
			return False
		elif exp1.var1.name == "T" and exp2.name == "T":
			return True
		elif exp1.var2.name == "T" and exp2.name == "T":
			return True
		else:
			return False
	else:
		return False


# Check if exp1 and exp2 match ID
# p^p = p
# pvp = p
def checkID(exp1, exp2):
	e1 = exp1.copySubExpression()
	e2 = exp2.copySubExpression()
	if e2.num_neg >= e1.num_neg:
		e2.num_neg -= e1.num_neg
	if e1.name == "and" or e1.name == "or":
		if e1.var1 == None or e1.var2 == None:
			return False
		elif e1.var1.isEqual(e2) and e1.var2.isEqual(e2):
			return True
		else:
			return False
	else:
		return False


# Check if exp1 and exp2 match COM
# p^q = q^p
# pvq = qvp
def checkCOM(exp1, exp2):
	if ((exp1.name == "and" and exp2.name == "and") or (exp1.name == "or" and exp2.name == "or")) and exp1.num_neg == exp2.num_neg:
		if exp1.var1 == None or exp1.var2 == None or exp2.var1 == None or exp2.var2 == None:
			return False
		elif exp1.var1.isEqual(exp2.var2) and exp1.var2.isEqual(exp2.var1):
			return True
		else:
			return False
	else:
		return False


# Check if exp1 and exp2 match ASS
# p^(q^r) = (p^q)^r
# pv(qvr) = (pvq)vr
def checkASS(exp1, exp2):
	if exp1.name == "and" and exp2.name == "and" and exp1.num_neg == exp2.num_neg:
		if exp1.var1 == None or exp1.var2 == None or exp2.var1 == None or exp2.var2 == None:
			return False
		if exp1.var2.name == "and" and exp2.var1.name == "and" and exp1.var2.num_neg == 0 and exp2.var1.num_neg == 0:
			if exp1.var2.var1 == None or exp1.var2.var2 == None or exp2.var1.var1 == None or exp2.var1.var2 == None:
				return False
			if exp1.var1.isEqual(exp2.var1.var1) and exp1.var2.var1.isEqual(exp2.var1.var2) and exp1.var2.var2.isEqual(exp2.var2):
				return True
			else:
				return False
		else:
			return False
	elif exp1.name == "or" and exp2.name == "or" and exp1.num_neg == exp2.num_neg:
		if exp1.var1 == None or exp1.var2 == None or exp2.var1 == None or exp2.var2 == None:
			return False
		if exp1.var2.name == "or" and exp2.var1.name == "or" and exp1.var2.num_neg == 0 and exp2.var1.num_neg == 0:
			if exp1.var2.var1 == None or exp1.var2.var2 == None or exp2.var1.var1 == None or exp2.var1.var2 == None:
				return False
			if exp1.var1.isEqual(exp2.var1.var1) and exp1.var2.var1.isEqual(exp2.var1.var2) and exp1.var2.var2.isEqual(exp2.var2):
				return True
			else:
				return False
		else:
			return False
	else:
		return False


# Check if exp1 and exp2 match DIST
# pv(q^r) = (pvq)^(pvr)
# p^(qvr) = (p^q)v(p^r)
# (r^q)vp = (rvp)^(qvp)
# (rvq)^p = (r^p)v(q^p)
def checkDIST(exp1, exp2):
	if exp1.name == "or" and exp2.name == "and" and exp1.num_neg == exp2.num_neg:
		if exp1.var1 == None or exp1.var2 == None or exp2.var1 == None or exp2.var2 == None:
			return False
		if exp1.var2.name == "and" and exp2.var1.name == "or" and exp2.var2.name == "or":
			if exp1.var1.isEqual(exp2.var1.var1) and exp1.var1.isEqual(exp2.var2.var1) and exp1.var2.var1.isEqual(exp2.var1.var2) and exp1.var2.var2.isEqual(exp2.var2.var2):
				return True
		if exp1.var1.name == "and" and exp2.var1.name == "or" and exp2.var2.name == "or":
			if exp1.var2.isEqual(exp2.var1.var2) and exp1.var2.isEqual(exp2.var2.var2) and exp1.var1.var1.isEqual(exp2.var1.var1) and exp1.var1.var2.isEqual(exp2.var2.var1):
				return True
		else:
			return False
	elif exp1.name == "and" and exp2.name == "or" and exp1.num_neg == exp2.num_neg:
		if exp1.var1 == None or exp1.var2 == None or exp2.var1 == None or exp2.var2 == None:
			return False
		if exp1.var2.name == "or" and exp2.var1.name == "and" and exp2.var2.name == "and":
			if exp1.var1.isEqual(exp2.var1.var1) and exp1.var1.isEqual(exp2.var2.var1) and exp1.var2.var1.isEqual(exp2.var1.var2) and exp1.var2.var2.isEqual(exp2.var2.var2):
				return True
		if exp1.var1.name == "or" and exp2.var1.name == "and" and exp2.var2.name == "and":
			if exp1.var2.isEqual(exp2.var1.var2) and exp1.var2.isEqual(exp2.var2.var2) and exp1.var1.var1.isEqual(exp2.var1.var1) and exp1.var1.var2.isEqual(exp2.var2.var1):
				return True
		else:
			return False
	else:
		return False


# Check if exp1 and exp2 match ABS
# pv(p^q) = p
# p^(pvq) = p
# (q^p)vp = p
# (qvp)^p = p
def checkABS(exp1, exp2):
	e1 = exp1.copySubExpression()
	e2 = exp2.copySubExpression()
	if e1.num_neg == e2.num_neg:
		e1.num_neg = 0
		e2.num_neg = 0
	elif e1.num_neg > e2.num_neg:
		e1.num_neg -= e2.num_neg
	elif e1.num_neg < e2.num_neg:
		e2.num_neg -= e1.num_neg

	if e1.name == "or":
		if e1.var1 == None or e1.var2 == None:
			return False
		if e1.var2.name == "and" and e1.var2.num_neg == 0:
			if e1.var2.var1 == None or e1.var2.var2 == None:
				return False
			if e2.isEqual(exp1.var1) and e2.isEqual(e1.var2.var1):
				return True
		if e1.var1.name == "and" and e1.var1.num_neg == 0:
			if e1.var1.var1 == None or e1.var1.var2 == None:
				return False
			if e2.isEqual(e1.var2) and e2.isEqual(e1.var1.var2):
				return True
			else:
				return False
		else:
			return False
	elif e1.name == "and":
		if e1.var1 == None or e1.var2 == None:
			return False
		if e1.var2.name == "or" and e1.var2.num_neg == 0:
			if e1.var2.var1 == None or e1.var2.var2 == None:
				return False
			if e2.isEqual(e1.var1) and e2.isEqual(e1.var2.var1):
				return True
		if e1.var1.name == "or" and e1.var1.num_neg == 0:
			if e1.var1.var1 == None or e1.var1.var2 == None:
				return False
			if e2.isEqual(e1.var2) and e2.isEqual(e1.var1.var2):
				return True
			else:
				return False
		else:
			return False
	else:
		return False
		

# Check if exp1 and exp2 match NEG
# p^~p = F
# ~p^p = F
# pv~p = T
# p^~p = T
def checkNEG(exp1, exp2):
	if exp1.name == "and" and exp2.name == "F" and exp1.num_neg == exp2.num_neg:
		if exp1.var1 == None or exp1.var2 == None:
			return False
		not_exp1_var1 = exp1.var1.copySubExpression()
		not_exp1_var1.negatesExpression()
		not_exp1_var2 = exp1.var2.copySubExpression()
		not_exp1_var2.negatesExpression()
		if not_exp1_var1.isEqual(exp1.var2) or not_exp1_var2.isEqual(exp1.var1):
			return True
		else:
			return False
	elif exp1.name == "or" and exp2.name == "T" and exp1.num_neg == exp2.num_neg:
		if exp1.var1 == None or exp1.var2 == None:
			return False
		not_exp1_var1 = exp1.var1.copySubExpression()
		not_exp1_var1.negatesExpression()			
		not_exp1_var2 = exp1.var2.copySubExpression()
		not_exp1_var2.negatesExpression()
		if not_exp1_var1.isEqual(exp1.var2) or not_exp1_var2.isEqual(exp1.var1):
			return True
		else:
			return False
	else:
		return False


# Check if exp1 and exp2 match DNEG:
# ~~p = p
def checkDNEG(exp1, exp2):
	not_exp2 = exp2.copySubExpression()
	not_exp2.negatesExpression()
	not_not_exp2 = not_exp2.copySubExpression()
	not_not_exp2.negatesExpression()
	if not_not_exp2.isEqual(exp1):
		return True
	else:
		return False


# Check if exp1 and exp2 match DM
# ~(p^q) = ~pv~q
# ~(pvq) = ~p^~q
def checkDM(exp1, exp2):
	if ((exp1.name == "and" and exp2.name == "or") or (exp1.name == "or" and exp2.name == "and")) and exp1.num_neg%2 == exp2.num_neg%2+1:
		if exp1.var1 == None or exp1.var2 == None or exp2.var1 == None or exp2.var2 == None:
			return False
		not_exp1_var1 = exp1.var1.copySubExpression()
		not_exp1_var1.negatesExpression()
		not_exp1_var1.removeDoubleNegation()
		not_exp1_var2 = exp1.var2.copySubExpression()
		not_exp1_var2.negatesExpression()
		not_exp1_var2.removeDoubleNegation()
		exp2_var1 = exp2.var1.copySubExpression()
		exp2_var1.removeDoubleNegation()
		exp2_var2 = exp2.var2.copySubExpression()
		exp2_var2.removeDoubleNegation()
		if exp2_var1.isEqual(not_exp1_var1) and exp2_var2.isEqual(not_exp1_var2):
			return True
		else:
			return False
	else:
		return False


# Check if exp1 and exp2 match XOR
# p(+)q = (pvq)^~(p^q)
# p(+)q = (p^~q)v(~p^q)
def checkXOR(exp1, exp2):
	if exp1.name == "xor" and exp1.num_neg == exp2.num_neg:
		if exp1.var1 == None or exp1.var2 == None or exp2.var1 == None or exp2.var2 == None:
			return False
		if exp2.name == "and" and exp2.var1.name == "or" and exp2.var2.name == "and" and exp2.var2.num_neg == 1:
			if exp1.var1.isEqual(exp2.var1.var1) and exp1.var1.isEqual(exp2.var2.var1) and exp1.var2.isEqual(exp2.var1.var2) and exp1.var2.isEqual(exp2.var2.var2):
				return True
			else:
				return False
		elif exp2.name == "or" and exp2.var1.name == "and" and exp2.var2.name == "and":
			not_exp1_var1 = exp1.var1.copySubExpression()
			not_exp1_var1.negatesExpression()
			not_exp1_var2 = exp1.var2.copySubExpression()
			not_exp1_var2.negatesExpression()
			if exp1.var1.isEqual(exp2.var1.var1) and not_exp1_var1.isEqual(exp2.var2.var1) and not_exp1_var2.isEqual(exp2.var1.var2) and exp1.var2.isEqual(exp2.var2.var2):
				return True
			else:
				return False
		else:
			return False
	else:
		return False


# Check if exp1 and exp2 match IMP:
# p->q = ~pvq
def checkIMP(exp1, exp2):
	if exp1.name == "imp" and exp2.name == "or" and exp1.num_neg == exp2.num_neg:
		if exp1.var1 == None or exp1.var2 == None or exp2.var1 == None or exp2.var2 == None:
			return False
		not_exp1_var1 = exp1.var1.copySubExpression()
		not_exp1_var1.negatesExpression()
		if not_exp1_var1.isEqual(exp2.var1) and exp1.var2.isEqual(exp2.var2):
			return True
		else:
			return False
	else:
		return False


# Check if exp1 and exp2 match CONTP
# p->q = ~q->~p
def checkCONTP(exp1, exp2):
	if exp1.name == "imp" and exp2.name == "imp" and exp1.num_neg == exp2.num_neg:
		if exp1.var1 == None or exp1.var2 == None or exp2.var1 == None or exp2.var2 == None:
			return False
		not_exp1_var1 = exp1.var1.copySubExpression()
		not_exp1_var1.negatesExpression()
		not_exp1_var2 = exp1.var2.copySubExpression()
		not_exp1_var2.negatesExpression()
		if not_exp1_var1.isEqual(exp2.var2) and not_exp1_var2.isEqual(exp2.var1):
			return True
		else:
			return False
	else:
		return False


# Check if exp1 and exp2 match BIC
# p<->q = (p->q)^(q->p)
# p<->q = ~(p(+)q)
def checkBIC(exp1, exp2):
	if exp1.name == "bic":
		if exp1.var1 == None or exp1.var2 == None or exp2.var1 == None or exp2.var2 == None:
			return False
		if exp2.name == "and" and exp1.num_neg == exp2.num_neg:
			if exp2.var1.name == "imp" and exp2.var2.name == "imp":
				if exp1.var1.isEqual(exp2.var1.var1) and exp1.var1.isEqual(exp2.var2.var2) and exp1.var2.isEqual(exp2.var1.var2) and exp1.var2.isEqual(exp2.var2.var1):
					return True
				else:
					return False
			else:
				return False
		elif exp2.name == "xor" and exp1.num_neg+1 == exp2.num_neg:
			if exp1.var1.isEqual(exp2.var1) and exp1.var2.isEqual(exp2.var2):
				return True
			else:
				return False
		else:
			return False
	else:
		return False



# Check if a rule can be matched between two expressions
def isRule(exp1, exp2, rule):
	# match I
	if rule == "I":
		if checkI(exp1, exp2) or checkI(exp2, exp1):
			return True
	# match UB
	elif rule == "UB":
		if checkUB(exp1, exp2) or checkUB(exp2, exp1):
			return True
	# match ID
	elif rule == "ID":
		if checkID(exp1, exp2) or checkID(exp2, exp1):
			return True
	# match COM
	elif rule == "COM":
		if checkCOM(exp1, exp2) or checkCOM(exp2, exp1):
			return True
	# match ASS
	elif rule == "ASS":
		if checkASS(exp1, exp2) or checkASS(exp2, exp1):
			return True
	# match DIST
	elif rule == "DIST":
		if checkDIST(exp1, exp2) or checkDIST(exp2, exp1):
			return True
	# match ABS
	elif rule == "ABS":
		if checkABS(exp1, exp2) or checkABS(exp2, exp1):
			return True
	# match NEG
	elif rule == "NEG":
		if checkNEG(exp1, exp2) or checkNEG(exp2, exp1):
			return True
	# match DNEG
	elif rule == "DNEG":
		if checkDNEG(exp1, exp2) or checkDNEG(exp2, exp1):
			return True
	# match DM
	elif rule == "DM":
		if checkDM(exp1, exp2) or checkDM(exp2, exp1):
			return True
	# match XOR
	elif rule == "XOR":
		if checkXOR(exp1, exp2) or checkXOR(exp2, exp1):
			return True
	# match IMP
	elif rule == "IMP":
		if checkIMP(exp1, exp2) or checkIMP(exp2, exp1):
			return True
	# match CONTP
	elif rule == "CONTP":
		if checkCONTP(exp1, exp2) or checkCONTP(exp2, exp1):
			return True
	# match BIC
	elif rule == "BIC":
		if checkBIC(exp1, exp2) or checkBIC(exp2, exp1):
			return True
	# no match
	else:
		return None
	# check vars
	if exp1.name == exp2.name and exp1.num_neg == exp2.num_neg:
		if exp1.var1 == None or exp1.var2 == None or exp2.var1 == None or exp2.var2 == None:
			return False
		elif exp1.var1.isEqual(exp2.var1) and isRule(exp1.var2, exp2.var2, rule):
			return True
		elif isRule(exp1.var1, exp2.var1, rule) and exp1.var2.isEqual(exp2.var2):
			return True
		else:
			return False
	# does not match the rule
	else:
		return False




# Identity (I)
# p^T = p
# pvF = p
def isIdentity(exp1, exp2):
	return isRule(exp1, exp2, "I") or isRule(exp2, exp1, "I")

# Universal Bound (UB) 
# p^F = F
# pvT = T
def isUniversalBound(exp1, exp2):
	return isRule(exp1, exp2, "UB") or isRule(exp2, exp1, "UB")

# Idempotent (ID)
# p^p = p
# pvp = p
def isIdempotent(exp1, exp2):
	return isRule(exp1, exp2, "ID") or isRule(exp2, exp1, "ID")

# Commutative (COM)
# p^q = q^p
# pvq = qvp
def isCommutative(exp1, exp2):
	return isRule(exp1, exp2, "COM") or isRule(exp2, exp1, "COM")

# Associative (ASS)
# p^(q^r) = (p^q)^r
# pv(qvr) = (pvq)vr
def isAssociative(exp1, exp2):
	return isRule(exp1, exp2, "ASS") or isRule(exp2, exp1, "ASS")

# Distributive (DIST)
# pv(q^r) = (pvq)^(pvr)
# p^(qvr) = (p^q)v(p^r)
def isDistributive(exp1, exp2):
	return isRule(exp1, exp2, "DIST") or isRule(exp2, exp1, "DIST")

# Absorption (ABS)
# pv(p^q) = p
# p^(pvq) = p
def isAbsorption(exp1, exp2):
	return isRule(exp1, exp2, "ABS") or isRule(exp2, exp1, "ABS")

# Negation (NEG)
# p^~p = F
# pv~p = T
def isNegation(exp1, exp2):
	return isRule(exp1, exp2, "NEG") or isRule(exp2, exp1, "NEG")

# Double Negation (DNEG) 
# ~~p = p
def isDoubleNegation(exp1, exp2):
	return isRule(exp1, exp2, "DNEG") or isRule(exp2, exp1, "DNEG")

# DeMorgan’s (DM)
# ~(p^q) = ~pv~q
# ~(pvq) = ~p^~q
def isDeMorgan(exp1, exp2):
	return isRule(exp1, exp2, "DM") or isRule(exp2, exp1, "DM")

# Definition of Exclusive OR (XOR) 
# p(+)q = (pvq)^~(p^q)
# p(+)q = (p^~q)v(~p^q)
def isDefExclusiveOr(exp1, exp2):
	return isRule(exp1, exp2, "XOR") or isRule(exp2, exp1, "XOR")

# Definition of Implication (IMP) 
# p->q = ~pvq
def isDefImplication(exp1, exp2):
	return isRule(exp1, exp2, "IMP") or isRule(exp2, exp1, "IMP")

# Contrapositive (CONTP)
# p->q = ~q->~p
def isContrapositive(exp1, exp2):
	return isRule(exp1, exp2, "CONTP") or isRule(exp2, exp1, "CONTP")

# Definition of Biconditional (BIC)
# p<->q = (p->q)^(q->p)
# p<->q = ~(p(+)q)
def isDefBiconditional(exp1, exp2):
	return isRule(exp1, exp2, "BIC") or isRule(exp2, exp1, "BIC")


#code used to test fundtions
#law = ""
#e1 = [""]
#e2 = [""]

#exp1 = Expression(None, None, None, None)
#exp1 = exp1.createExpression(e1, False)

#exp2 = Expression(None, None, None, None)
#exp2 = exp2.createExpression(e2, False)

#isRule(exp1, exp2, law)
