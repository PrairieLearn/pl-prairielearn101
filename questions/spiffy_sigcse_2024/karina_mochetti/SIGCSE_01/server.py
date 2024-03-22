import random
import os
from logicExpression import *
from equivalence import *
from inference import *
from arguments import *


def wrongChar(ans_str):
    # remove operations
    ans_str = ans_str.replace("v","").replace("^","").replace("(+)","").replace("->","").replace("<->","").replace("~","")
    # remove brackets
    ans_str = ans_str.replace("(","").replace(")","")
    # remove var names
    ans_str = ans_str.replace("x1","").replace("x2","").replace("x3","").replace("x4","").replace("x5","").replace("x6","").replace("x7","")
    ans_str = ans_str.replace("a","").replace("b","").replace("c","").replace("d","").replace("e","").replace("f","").replace("g","")
    ans_str = ans_str.replace("p","").replace("q","").replace("r","").replace("o","").replace("n","").replace("m","").replace("k","")
    ans_str = ans_str.replace("x","").replace("y","").replace("z","").replace("w","").replace("u","").replace("t","").replace("s","")
    # remove const names
    ans_str = ans_str.replace("T","").replace("F","")
    # remove spaces
    ans_str = ans_str.replace(" ","")
    
    if len(ans_str) > 0:
        return True
    else:
        return False


def generate(data):

    # Choose var names
    var_names = random.choice([["a", "b", "c", "d"], ["p", "q", "r", "s"], ["x", "y", "z", "w"], ["x1", "x2", "x3", "x4"]])
    data["params"]["var1"] = var_names[0]
    data["params"]["var2"] = var_names[1]
    data["params"]["var3"] = var_names[2]

    # Generate a contradiction argument with 4 variables and 4 premises
    argument = createArgument(4, var_names)
    while not isContradiction(argument[:-1], argument[-1]):
        argument = createArgument(4, var_names)

    # Print the expression(s)
    data["params"]["prem"] = []
    num = 1
    for exp in argument[:-1]:
        latex_list = exp.printToLatex()
        str_exp = ""
        for i in latex_list:
            str_exp = str_exp + " " + i
        data["params"]["prem"].append({"num": str(num), "exp": str_exp[1:]})
        num += 1
    data["params"]["num"] = num

    # Print conclusion
    expr = argument[-1]
    latex_list = expr.printToLatex()
    expr_str = ""
    for symbol in latex_list:
        expr_str = expr_str + " " + symbol
    data["params"]["conc"] = expr_str

    # Add numbers to each line
    data["params"]["answer_panel"] = []
    for i in range (num, 26):
        data["params"]["Numbers"] = [
            {"tag": "true", "ans": "---"}
        ]
        for j in range(1, i):
            data["params"]["Numbers"].append({"tag": "false", "ans": str(j)})
        data["params"]["answer_panel"].append({"num": str(i), "ans": "ans"+str(i), "rule": "rule"+str(i), "FirstNum": "FirstNum"+str(i), "SecondNum": "SecondNum"+str(i), "Numbers": data["params"]["Numbers"]})


def grade(data):

    # Clear scores
    num = data["params"]["num"]
    for i in range(num, 26):
        del data['partial_scores']["rule"+str(i)]
        del data['partial_scores']["FirstNum"+str(i)]
        del data['partial_scores']["SecondNum"+str(i)]
    data["params"]["feedback"] = ""
    prem_exp = Expression(None, None, None, None)
    conc_exp = Expression(None, None, None, None)

    # read argument
    exp = []
    argument = []
    exp.append(None)
    for i in range(1, num):
        # Get answer
        prem_str = data["params"]["prem"][i-1]["exp"]
        prem_latex = prem_str.split()
        prem_exp = prem_exp.createExpression(prem_latex, True)
        exp.append(prem_exp)
        argument.append(prem_exp)

    # read conclusion
    conc_str = "F"
    conc_exp = conc_exp.createExpression(conc_str, True)

    # read all expressions answers
    for i in range(num, 26):
        # Get answer
        ans_str = data["submitted_answers"]["ans"+str(i)]
        if ans_str != "":
            ans_exp = parseStringToExp(ans_str)
            if ans_exp == None:
                data["params"]["feedback"] = "Expression " + str(i) + " is not a valid logic expression!"
                data["score"] = 0
                return
            exp.append(ans_exp)

    # For each expression in answer
    for i in range(num, len(exp)):

        # Check if it is a valid premise
        if not isValid(argument, exp[i]):
            data["params"]["feedback"] = "Expression " + str(i) + " is not a valid premise!"
            data["score"] = 0
            return

        else:
            # Get rule
            rule = data["submitted_answers"]["rule"+str(i)]

            # Get premise numbers
            first_number = 0
            if data["submitted_answers"]["FirstNum"+str(i)] != "---":
                first_number = int(data["submitted_answers"]["FirstNum"+str(i)])
            second_number = 0
            if data["submitted_answers"]["SecondNum"+str(i)] != "---":
                second_number = int(data["submitted_answers"]["SecondNum"+str(i)])

            # Check if the rule/law was applied
            is_correct = False
            extra_num = False
            missing_num = False
            if rule == "I":
                if second_number != 0:
                    extra_num = True
                if first_number == 0:                    
                    missing_num = True
                else:
                    is_correct = isIdentity(exp[first_number], exp[i])
            elif rule == "UB":
                if second_number != 0:
                    extra_num = True
                if first_number == 0:                    
                    missing_num = True
                else:
                    is_correct = isUniversalBound(exp[first_number], exp[i])
            elif rule == "ID":
                if second_number != 0:
                    extra_num = True
                if first_number == 0:                    
                    missing_num = True
                else:
                    is_correct = isIdempotent(exp[first_number], exp[i])
            elif rule == "COM":
                if second_number != 0:
                    extra_num = True
                if first_number == 0:                    
                    missing_num = True
                else:
                    is_correct = isCommutative(exp[first_number], exp[i])
            elif rule == "ASS":
                if second_number != 0:
                    extra_num = True
                if first_number == 0:                    
                    missing_num = True
                else:
                    is_correct = isAssociative(exp[first_number], exp[i])
            elif rule == "DIST":
                if second_number != 0:
                    extra_num = True
                if first_number == 0:                    
                    missing_num = True
                else:
                    is_correct = isDistributive(exp[first_number], exp[i])
            elif rule == "ABS":
                if second_number != 0:
                    extra_num = True
                if first_number == 0:                    
                    missing_num = True
                else:
                    is_correct = isAbsorption(exp[first_number], exp[i])
            elif rule == "NEG":
                if second_number != 0:
                    extra_num = True
                if first_number == 0:                    
                    missing_num = True
                else:
                    is_correct = isNegation(exp[first_number], exp[i])
            elif rule == "DNEG":
                if second_number != 0:
                    extra_num = True
                if first_number == 0:                    
                    missing_num = True
                else:
                    is_correct = isDoubleNegation(exp[first_number], exp[i])
            elif rule == "DM":
                if second_number != 0:
                    extra_num = True
                if first_number == 0:                    
                    missing_num = True
                else:
                    is_correct = isDeMorgan(exp[first_number], exp[i])
            elif rule == "XOR":
                if second_number != 0:
                    extra_num = True
                if first_number == 0:                    
                    missing_num = True
                else:
                    is_correct = isDefExclusiveOr(exp[first_number], exp[i])
            elif rule == "IMP":
                if second_number != 0:
                    extra_num = True
                if first_number == 0:                    
                    missing_num = True
                else:
                    is_correct = isDefImplication(exp[first_number], exp[i])
            elif rule == "CONTP":
                if second_number != 0:
                    extra_num = True
                if first_number == 0:                    
                    missing_num = True
                else:
                    is_correct = isContrapositive(exp[first_number], exp[i])
            elif rule == "BIC":
                if second_number != 0:
                    extra_num = True
                if first_number == 0:                    
                    missing_num = True
                else:
                    is_correct = isDefBiconditional(exp[first_number], exp[i])
            elif rule == "M.PON":
                if first_number == 0 or second_number == 0:                    
                    missing_num = True
                else:
                    is_correct = isModusPonens(exp[first_number], exp[second_number], exp[i])
            elif rule == "M.TOL":
                if first_number == 0 or second_number == 0:                    
                    missing_num = True
                else:
                    is_correct = isModusTollens(exp[first_number], exp[second_number], exp[i])
            elif rule == "GEN":
                if second_number != 0:
                    extra_num = True
                if first_number == 0:                    
                    missing_num = True
                else:
                    is_correct = isGeneralization(exp[first_number], exp[i])
            elif rule == "SPEC":
                if second_number != 0:
                    extra_num = True
                if first_number == 0:                    
                    missing_num = True
                else:
                    is_correct = isSpecialization(exp[first_number], exp[i])
            elif rule == "CONJ":
                if first_number == 0 or second_number == 0:                    
                    missing_num = True
                else:
                    is_correct = isConjunction(exp[first_number], exp[second_number], exp[i])
            elif rule == "ELIM":
                if first_number == 0 or second_number == 0:                    
                    missing_num = True
                else:
                    is_correct = isElimination(exp[first_number], exp[second_number], exp[i])
            elif rule == "TRANS":
                if first_number == 0 or second_number == 0:                    
                    missing_num = True
                else:
                    is_correct = isTransitivity(exp[first_number], exp[second_number], exp[i])
            elif rule == "CASE":
                if first_number == 0 or second_number == 0:                    
                    missing_num = True
                else:
                    is_correct = isProofByCases(exp[first_number], exp[second_number], exp[i])
            elif rule == "RES":
                if first_number == 0 or second_number == 0:                    
                    missing_num = True
                else:
                    is_correct = isResolution(exp[first_number], exp[second_number], exp[i])
            elif rule == "CONTD":
                if second_number != 0:
                    extra_num = True
                if first_number == 0:                    
                    missing_num = True
                else:
                    is_correct = isContradictionRule(exp[first_number], exp[i])
            else:
                data["params"]["feedback"] = "Law/rule missing in step " + str(i)
                data["score"] = 0
                return
            if missing_num:
                data["params"]["feedback"] = "Missing Law/rule number in step " + str(i)
                data["score"] = 0
                return
            if  extra_num:
                data["params"]["feedback"] = "Extra Law/rule number given in step " + str(i)
                data["score"] = 0
                return
            if  not is_correct:
                data["params"]["feedback"] = "Law/rule applied incorrectly in step " + str(i)
                data["score"] = 0
                return

    # Check if it is the last expression is the conclusion
    if exp[-1].isEqual(conc_exp):
        data["params"]["feedback"] = "Correct proof!"
        data["score"] = 1
        return
            
    # Did not reach to the conclusion
    else: 
        data["params"]["feedback"] = "Your proof is not complete (the last expression does not match the expected conclusion)!"
        data["score"] = 0
        return


def parse(data):

    # For each expression in answer...
    num = data["params"]["num"]
    ans_exp = exp1
    for i in range(num, 26):
        prev_ans_exp = ans_exp
        # Get answer
        ans_str = data["submitted_answers"]["ans"+str(i)]
        if ans_str == "":
            break;
        ans_exp = parseStringToExp(ans_str)
        if ans_exp == None:
            # strange char
            if wrongChar(ans_str):
                data["format_errors"]["ans"+str(i)] = "Invalid character found in the expression."
            # wrong number of brackets
            elif ans_str.count('(') > ans_str.count(')'):
                data["format_errors"]["ans"+str(i)] = "Invalid brackets: there are more ( than )."
            elif ans_str.count(')') > ans_str.count('('):
                data["format_errors"]["ans"+str(i)] = "Invalid brackets: there are more ) than (."
            # invalid expression
            else:
                data["format_errors"]["ans"+str(i)] = "The expression does not follow the rules given, remember each operation can only have 2 inputs and must have brackets."
    return

