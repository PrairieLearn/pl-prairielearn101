#!/usr/bin/python3
import random, string
import lib.schemdraw as schemdraw
from lib.schemdraw import logic
from lib.schemdraw.parsing import logicparse

op_list = ["or", "and", "xor", "imp", "bic"]
simple_op_list = ["or", "and"]
var_list = [["a", "b", "c", "d", "e", "f", "g"], ["p", "q", "r", "o", "n", "m", "k"], ["x", "y", "z", "w", "u", "t", "s"], ["x1", "x2", "x3", "x4", "x5", "x6", "x7"]]
const_list = ["T", "F"]

# Parse operations to op_list
def parse_op(op):
    if op == "\\vee" or op == "v":
        return "or"
    elif op == "\wedge" or op == "^":
        return "and"
    elif op == "\oplus" or op == "(+)":
        return "xor"
    elif op == "\\rightarrow" or op == "->":
        return "imp"
    elif op == "\leftrightarrow" or op == "<->":
        return "bic"


# A class which represents a logic expression, with an operation name, zero, one or more negation signs, and 2 variables
class Expression:
    def __init__(self, name, num_neg, var1, var2):
        self.name = name
        self.num_neg = num_neg
        self.var1 = var1
        self.var2 = var2


    # Create a random simple (only AND/OR) expression with n operations and variables in list var_names
    # used by createRandomSimpleExpression
    def randomSimpleExpression(self, n, var_names):
        if n == 0:
            var_name = random.choice(var_names)
            not_ops = random.randint(0,1)
            return Expression(var_name, not_ops, None, None)
        else:
            op = random.choice(simple_op_list)
            num_op = random.randint(0,n-1)
            var1 = self.randomSimpleExpression(num_op, var_names)
            var2 = self.randomSimpleExpression(n-1-num_op, var_names)
            not_ops = random.randint(0,1)
            return Expression(op, not_ops, var1, var2)


    # Create a random simple expression with n operations and m variables 
    #      n in [0, ...)
    #      m in [1, 5]
    def createRandomSimpleExpression(self, n, m):
        var_names = random.choice(var_list)
        return self.randomSimpleExpression(n, var_names[:m])

    # Create a random expression with n operations and variables in list var_names
    # used by createRandomExpression
    def randomExpression(self, n, var_names):
        if n == 0:
            var_name = random.choice(var_names)
            not_ops = random.randint(0,1)
            return Expression(var_name, not_ops, None, None)
        else:
            op = random.choice(op_list)
            num_op = random.randint(0,n-1)
            var1 = self.randomExpression(num_op, var_names)
            var2 = self.randomExpression(n-1-num_op, var_names)
            not_ops = random.randint(0,1)
            return Expression(op, not_ops, var1, var2)


    # Create a random expression with n operations and m variables 
    #      n in [0, ...)
    #      m in [1, 5]
    def createRandomExpression(self, n, m):
        var_names = random.choice(var_list)
        return self.randomExpression(n, var_names[:m])


    # Parse expression from Latex or regular string (called inorder)
    #      inorder is a list of strings with operators, variables and brackets
    #      all operations must have only 2 variables and be around brackets, i.e. (a^b)
    def createExpression(self, inorder, is_latex):
        if is_latex:
            not_op = "\sim"
            op_list = ["\wedge", "\\vee", "\oplus", "\\rightarrow", "\leftrightarrow"]
        else:
            not_op = "~"
            op_list = ["^", "v", "(+)", "->", "<->"]            
        stack = []
        for i in inorder:
            if i == "(" or i == not_op:
                stack.append(i)
            elif i in op_list:
                stack.append(i)
            elif i == ")":
                if not len(stack):
                    return None
                r = stack.pop()
                if not len(stack) or r in ["(", ")", not_op] + op_list:
                    return None
                op = stack.pop()
                if not len(stack) or not op in op_list:
                    return None
                l = stack.pop()
                if not len(stack) or l in ["(", ")", not_op] + op_list:
                    return None
                stack.pop()
                if stack and stack[-1] == not_op:
                    num_neg = 0
                    while stack and stack[-1] == not_op:
                        stack.pop()
                        num_neg += 1
                    node = Expression(parse_op(op), num_neg, l, r)
                    stack.append(node)
                else:
                    node = Expression(parse_op(op), 0, l, r)
                    stack.append(node)
            else:
                if stack and stack[-1] == not_op:
                    num_neg = 0
                    while stack and stack[-1] == not_op:
                        stack.pop()
                        num_neg += 1
                    node = Expression(i, num_neg, None, None)
                    stack.append(node)
                else:
                    node = Expression(i, 0, None, None)
                    stack.append(node)
        if len(stack) == 1 and not type(stack[0]) is str:
            return stack.pop()
        else:
            return None


    # Change variable names
    def changeVarNames(self, new_names):
        # variable
        if self.var1 == None and self.var2 == None:
            if self.name == var_list[0][0] or self.name == var_list[1][0] or self.name == var_list[2][0] or self.name == var_list[3][0]:
                self.name = new_names[0]
            if self.name == var_list[0][1] or self.name == var_list[1][1] or self.name == var_list[2][1] or self.name == var_list[3][1]:
                self.name = new_names[1]
            if self.name == var_list[0][2] or self.name == var_list[1][2] or self.name == var_list[2][2] or self.name == var_list[3][2]:
                self.name = new_names[2]
            if self.name == var_list[0][3] or self.name == var_list[1][3] or self.name == var_list[2][3] or self.name == var_list[3][3]:
                self.name = new_names[3]
            if self.name == var_list[0][4] or self.name == var_list[1][4] or self.name == var_list[2][4] or self.name == var_list[3][4]:
                self.name = new_names[4]
            if self.name == var_list[0][5] or self.name == var_list[1][5] or self.name == var_list[2][5] or self.name == var_list[3][5]:
                self.name = new_names[5]
            if self.name == var_list[0][6] or self.name == var_list[1][6] or self.name == var_list[2][6] or self.name == var_list[3][6]:
                self.name = new_names[6]
            return
        # operation
        else:
            self.var1.changeVarNames(new_names)
            self.var2.changeVarNames(new_names)
        

    # Change the expression looks by using randomly commutative steps
    def shuffleExpression(self):
        # variable
        if self.var1 == None and self.var2 == None:
            return
        # operation
        else:
            use_com = random.choice([True, False])
            if use_com and self.name != "imp":
                self.var1, self.var2 = self.var2, self.var1
            self.var1.shuffleExpression()
            self.var2.shuffleExpression()
        

    # Copy a part of the expression (to be used in the def of xor)
    def copySubExpression(self):
        copy = Expression(self.name, self.num_neg, None, None)
        if self.var1 is not None:
            copy.var1 = self.var1.copySubExpression()
        if self.var2 is not None:
            copy.var2 = self.var2.copySubExpression()
        return copy


    # Returns a expression that only has AND and OR as operations (uses def of imp, bic, xor) if remove_xor is true
    # Returns a expression that only has XOR, AND and OR as operations (uses def of imp, and bic = not xor) if remove_xor is false
    def simplifyExpression(self, remove_xor):
        # variable
        if self.var1 == None and self.var2 == None:
            return
        # operation
        else:
            if self.name == "imp":
                self.name = "or"
                self.var1.num_neg += 1
            elif self.name == "bic":
                if remove_xor:
                    self.name = "or"
                    left1 = self.var1
                    left2 = self.var1.copySubExpression()
                    right1 = self.var2
                    right2 = self.var2.copySubExpression()
                    self.var1 = Expression("or", 1, left1, right1)
                    self.var2 = Expression("and", 0, left2, right2)
                else:
                    self.name = "xor"
                    self.num_neg += 1
            elif remove_xor and self.name == "xor":
                self.name = "and"
                left1 = self.var1
                left2 = self.var1.copySubExpression()
                right1 = self.var2
                right2 = self.var2.copySubExpression()
                self.var1 = Expression("or", 0, left1, right1)
                self.var2 = Expression("and", 1, left2, right2)
            self.var1.simplifyExpression(remove_xor)
            self.var2.simplifyExpression(remove_xor)
            return


    # Bring all negation to within the variables in a simple expression (it has only AND and OR)
    # uses double negation and de morgan
    def removeNegationFromSimpleExpression(self):
        # it is a variable
        if self.var1 == None and self.var2 == None:
            return
        # it is an operation (either AND, OR)
        else:
            if self.num_neg % 2 == 0:
                self.num_neg = 0
            else:
                self.num_neg = 0 
                if self.name == "or":
                    # using de Morgan
                    self.name = "and"
                    self.var1.num_neg = (self.var1.num_neg+1) % 2 
                    self.var2.num_neg = (self.var2.num_neg+1) % 2 
                elif self.name == "and":
                    # using de Morgan
                    self.name = "or"
                    self.var1.num_neg = (self.var1.num_neg+1) % 2 
                    self.var2.num_neg = (self.var2.num_neg+1) % 2
            self.var1.removeNegationFromSimpleExpression()
            self.var2.removeNegationFromSimpleExpression()
            return


    # Negates expression
    def negatesExpression(self):
        # negate the variable
        self.num_neg += 1
        return


    # Uses double negation
    def removeDoubleNegation(self):
        # it is a variable
        if self.var1 == None and self.var2 == None:
            self.num_neg = self.num_neg % 2
            return
        # it is an operation
        else:
            self.num_neg = self.num_neg % 2
            self.var1.removeDoubleNegation()
            self.var2.removeDoubleNegation()
            return


    # Return true or false base on the variables values
    def calculateTruthValue(self, var1, var2, var3, var4, var5, var6, var7):
        # variable
        if self.var1 == None and self.var2 == None:
            if self.name == var_list[0][0] or self.name == var_list[1][0] or self.name == var_list[2][0] or self.name == var_list[3][0]:
                value = var1
            elif self.name == var_list[0][1] or self.name == var_list[1][1] or self.name == var_list[2][1] or self.name == var_list[3][1]:
                value = var2
            elif self.name == var_list[0][2] or self.name == var_list[1][2] or self.name == var_list[2][2] or self.name == var_list[3][2]:
                value = var3
            elif self.name == var_list[0][3] or self.name == var_list[1][3] or self.name == var_list[2][3] or self.name == var_list[3][3]:
                value = var4
            elif self.name == var_list[0][4] or self.name == var_list[1][4] or self.name == var_list[2][4] or self.name == var_list[3][4]:
                value = var5
            elif self.name == var_list[0][5] or self.name == var_list[1][5] or self.name == var_list[2][5] or self.name == var_list[3][5]:
                value = var6
            elif self.name == var_list[0][6] or self.name == var_list[1][6] or self.name == var_list[2][6] or self.name == var_list[3][6]:
                value = var7
            elif self.name == "T":
                value = True
            elif self.name == "F":
                value = False
        # operation
        else:
            left = self.var1.calculateTruthValue(var1, var2, var3, var4, var5, var6, var7)
            right = self.var2.calculateTruthValue(var1, var2, var3, var4, var5, var6, var7)
            if self.name == "or":
                value = (left or right)
            elif self.name == "and":
                value = (left and right)
            elif self.name == "xor":
                value = (left != right)
            elif self.name == "imp":
                value = (not left or right)
            elif self.name == "bic":
                value = (left == right)
        # check negations
        if self.num_neg % 2 == 1:
            return not value
        else:
            return value


    # Check if two expressions are equal (have the same operations, variables, in the same order)
    def isEqual(self, exp):
        if not isinstance(exp, Expression):
            return False
        if self.name != exp.name or self.num_neg != exp.num_neg:
            return False
        else:
            if self.var1 == None and self.var2 == None and exp.var1 == None and exp.var2 == None:
                return True
            elif self.var1 != None and self.var2 != None and exp.var1 != None and exp.var2 != None:
                left = self.var1.isEqual(exp.var1)
                right = self.var2.isEqual(exp.var2)
                return left and right
            else:
                return False


    # Check if two expressions are equivalent
    def isEquivalent(self, exp):
        if not isinstance(exp, Expression):
            return False
        for var1 in [True, False]:
            for var2 in [True, False]:
                for var3 in [True, False]:
                    for var4 in [True, False]:
                        for var5 in [True, False]:
                            for var6 in [True, False]:
                                for var7 in [True, False]:
                                    if self.calculateTruthValue(var1,var2,var3,var4,var5,var6,var7) != exp.calculateTruthValue(var1,var2,var3,var4,var5,var6,var7):
                                        return False
        return True


    # Check if the expression is a Tautology (always true)
    def isTautology(self):
        for var1 in [True, False]:
            for var2 in [True, False]:
                for var3 in [True, False]:
                    for var4 in [True, False]:
                        for var5 in [True, False]:
                            for var6 in [True, False]:
                                for var7 in [True, False]:
                                    if self.calculateTruthValue(var1,var2,var3,var4,var5,var6,var7) == False:
                                        return False
        return True


    # Check if the expression is a Contradiction (always false)
    def isContradiction(self):
        for var1 in [True, False]:
            for var2 in [True, False]:
                for var3 in [True, False]:
                    for var4 in [True, False]:
                        for var5 in [True, False]:
                            for var6 in [True, False]:
                                for var7 in [True, False]:
                                    if self.calculateTruthValue(var1,var2,var3,var4,var5,var6,var7) == True:
                                        return False
        return True


    # Print expression using regular char string (returns a **list** of strings with operators being ^v (+) -> and <->, variables and brackets)
    def printToSymbols(self):
        value = []
        # variable
        if self.var1 == None and self.var2 == None:
            for i in range(self.num_neg):
                value.append("~")
            value.append(self.name)
        # operation
        else:
            for i in range(self.num_neg):
                value.append("~")
            value.append("(")
            value = value + self.var1.printToSymbols()
            if self.name == "or":
                value.append("v") 
            elif self.name == "and":
                value.append("^") 
            elif self.name == "xor":
                value.append("(+)") 
            elif self.name == "imp":
                value.append("->") 
            elif self.name == "bic":
                value.append("<->") 
            value = value + self.var2.printToSymbols()
            value.append(")")
        return value


    # Print expression using Latex (returns a **list** of strings with operators, variables and brackets)
    def printToLatex(self):
        value = []
        # variable
        if self.var1 == None and self.var2 == None:
            for i in range(self.num_neg):
                value.append("\\sim")
            value.append(self.name)
        # operation
        else:
            for i in range(self.num_neg):
                value.append("\\sim")
            value.append("(")
            value = value + self.var1.printToLatex()
            if self.name == "or":
                value.append("\\vee") 
            elif self.name == "and":
                value.append("\wedge") 
            elif self.name == "xor":
                value.append("\oplus") 
            elif self.name == "imp":
                value.append("\\rightarrow") 
            elif self.name == "bic":
                value.append("\leftrightarrow") 
            value = value + self.var2.printToLatex()
            value.append(")")
        return value


    # Print expression using regular char string (returns a string with operators being english words, variables and brackets)
    def printToString(self):
        string = ""
        # variable
        if self.var1 == None and self.var2 == None:
            for i in range(self.num_neg):
                string = string + "not "
            string = string + self.name
        # operation
        else:
            for i in range(self.num_neg):
                string = string + "not "
            string = string + "("
            string = string + self.var1.printToString()
            string = string + " " + self.name + " "
            string = string + self.var2.printToString()
            string = string + ")"
        return string


    # Create a svg image of the circuit that represents the expression, must be a simple expression
    def getCircuit(self, output_name):
        d = schemdraw.Drawing()
        # note: it does not work if it has two or more not gates together, so it uses DNEG first
        self.removeDoubleNegation()
        d = logicparse(self.printToString(), outlabel=output_name)
        d.draw()
        return d.get_imagedata('svg')


    # Counts the number of operations in expr (not counting NOT)
    def countNumOp(self):
        # variable
        if self.var1 == None and self.var2 == None:
            return 0
        # operation
        else:
            left = self.var1.countNumOp()
            right = self.var2.countNumOp()
        return left+right+1


    # Return the number of OR operators in the expression
    def countOr(self):        
        # variable
        if self.var1 == None and self.var2 == None:
            return 0
        # operation
        else:
            left = self.var1.countOr()
            right = self.var2.countOr()
            if self.name == "or":
                num_or = 1
            else:
                num_or = 0
        return left+right+num_or


    # Return the number of AND operators in the expression
    def countAnd(self):        
        # variable
        if self.var1 == None and self.var2 == None:
            return 0
        # operation
        else:
            left = self.var1.countAnd()
            right = self.var2.countAnd()
            if self.name == "and":
                num_and = 1
            else:
                num_and = 0
        return left+right+num_and


    # Return the number of XOR operators in the expression
    def countXor(self):        
        # variable
        if self.var1 == None and self.var2 == None:
            return 0
        # operation
        else:
            left = self.var1.countXor()
            right = self.var2.countXor()
            if self.name == "xor":
                num_xor = 1
            else:
                num_xor = 0
        return left+right+num_xor


    # Return the number of IMP operators in the expression
    def countImp(self):        
        # variable
        if self.var1 == None and self.var2 == None:
            return 0
        # operation
        else:
            left = self.var1.countImp()
            right = self.var2.countImp()
            if self.name == "imp":
                num_imp = 1
            else:
                num_imp = 0
        return left+right+num_imp


    # Return the number of BIC operators in the expression
    def countBic(self):        
        # variable
        if self.var1 == None and self.var2 == None:
            return 0
        # operation
        else:
            left = self.var1.countBic()
            right = self.var2.countBic()
            if self.name == "bic":
                num_bic = 1
            else:
                num_bic = 0
        return left+right+num_bic


# Parse string of operators to expression
def parseStringToExp(str_exp):

    # remove spaces
    str_exp = str_exp.replace(" ", "")

    # parse answer
    str_list = []
    n = len(str_exp)
    i = 0
    while i < n:
        # if char means variable
        if str_exp[i] in var_list[0] or str_exp[i] in var_list[1] or str_exp[i] in var_list[2] or str_exp[i] in var_list[3]:
            if str_exp[i] == 'x':
                if i < n-1 and str_exp[i+1] in ["1", "2", "3", "4", "5", "6", "7"]:
                    str_list.append(str_exp[i:i+2])
                    i = i+1
                else:
                    str_list.append(str_exp[i:i+1])
            else:
                str_list.append(str_exp[i:i+1])
        # if char means True/False
        elif str_exp[i] == 'T' or str_exp[i] == 'F':
            str_list.append(str_exp[i:i+1])
        # if char means op
        elif str_exp[i] == '^' or str_exp[i] == 'v' or str_exp[i] == ')' or str_exp[i] == '~':
            str_list.append(str_exp[i:i+1])
        # if char means bracket
        elif str_exp[i] == '(':
            if i < n-1 and str_exp[i+1] == "+":
                str_list.append("(+)")
                i = i+2
            else:
                str_list.append("(")
        # if char means implications
        elif str_exp[i] == '-':
            if i < n-1 and str_exp[i+1] == '>':
                str_list.append("->")
                i = i+1
        # if char means biconditional
        elif str_exp[i] == '<':
            if i < n-2 and str_exp[i+1] == '-' and str_exp[i+2] == '>':
                str_list.append("<->")
                i = i+2
        else:
            return None
        i += 1

    # check if there is an answer
    if len(str_list):
        exp = Expression(None, None, None, None)
        exp = exp.createExpression(str_list, False)
        return exp
    else:
        return None


# Create a circuit missing a gate
def getMissGateCircuit(n, vars, output_name):
    exp = Expression(None, None, None, None)
    found_exp = False

    # find a expression
    while not found_exp:
        exp = exp.createRandomExpression(n, vars)
        exp.simplifyExpression(False)
        exp_list = exp.printToSymbols()

        # randomly choose a operation
        op_list_index = []
        for index, symbol in enumerate(exp_list):
            if symbol in ["^", "v", "(+)"]:
                op_list_index.append(index)
        op_index = random.choice(op_list_index)

        # find negation position
        neg_index = 0
        num_brackets = 0
        i = op_index
        while i >= 0 and neg_index == 0:
            if exp_list[i] == ")":
                num_brackets += 1
            elif exp_list[i] == "(":
                if num_brackets == 0:
                    neg_index = i
                else:
                    num_brackets -= 1
            i -= 1

        # make sure that changing the operation by and, or and xor does not make it equivalent
        exp1 = Expression(None, None, None, None)
        exp1_list = exp_list.copy()
        exp1_list[op_index] = "^"
        exp1 = exp1.createExpression(exp1_list, False)
        exp2 = Expression(None, None, None, None)
        exp2_list = exp_list.copy()
        exp2_list[op_index] = "v"
        exp2 = exp2.createExpression(exp2_list, False)
        exp3 = Expression(None, None, None, None)
        exp3_list = exp_list.copy()
        exp3_list[op_index] = "(+)"
        exp3 = exp3.createExpression(exp3_list, False)
    
        # make sure that changing the operation by nand, nor and xnor does not make it equivalent
        exp4 = Expression(None, None, None, None)
        exp4_list = exp_list.copy()
        exp4_list[op_index] = "^"
        exp4_list.insert(neg_index, "~")
        exp4 = exp4.createExpression(exp4_list, False)
        exp5 = Expression(None, None, None, None)
        exp5_list = exp_list.copy()
        exp5_list[op_index] = "v"
        exp5_list.insert(neg_index, "~")
        exp5 = exp5.createExpression(exp5_list, False)
        exp6 = Expression(None, None, None, None)
        exp6_list = exp_list.copy()
        exp6_list[op_index] = "(+)"
        exp6_list.insert(neg_index, "~")
        exp6 = exp6.createExpression(exp6_list, False)
    
        if not exp1.isEquivalent(exp2) and not exp2.isEquivalent(exp3) and not exp3.isEquivalent(exp4) and not exp4.isEquivalent(exp5) and not exp5.isEquivalent(exp6) and not exp6.isEquivalent(exp1):
            found_exp = True
            
    # replace the chosen gate by ?
    correct_gate = exp_list[op_index]
    exp_list[op_index] = "?"

    # create a expression with only or gates, and ? as an and gate to get its position
    tmp_list = exp_list.copy()
    for i in range(len(tmp_list)):
        if tmp_list[i] == '?':
            tmp_list[i] = '^'
        elif tmp_list[i] in ['^', '(+)']:
            tmp_list[i] = 'v'

    # check to see if the gate is negated
    tmp = Expression(None, None, None, None)
    tmp = tmp.createExpression(tmp_list, False)
    neg = False
    ops = []
    ops.append(tmp)
    while len(ops) > 0:
        op = ops.pop(-1)
        if op.name == "and":
            if op.num_neg%2 == 1:
                neg = True
            ops = []
        else:
            if op.var1 != None and op.var2 != None:
                ops.append(op.var1)
                ops.append(op.var2)

    # return the removed gate
    if correct_gate == "v":
        if neg:
            correct_gate = "nor"
        else:
            correct_gate = "or"
    elif correct_gate == "^":
        if neg:
            correct_gate = "nand"
        else:
            correct_gate = "and"
    elif correct_gate == "(+)":
        if neg:
            correct_gate = "xnor"
        else:
            correct_gate = "xor"

    # create svg file and get and gate position
    svg = tmp.getCircuit(output_name)

    # find the and gate path on the svg (path with 54 coordinates)
    start = svg.find(b"<path")
    while start != -1:
        end = svg.find(b"clip-path", start)
        path_str = str(svg[start+9:end-2])[2:-1]
        path_str = path_str.replace("\n", "");
        path_str = path_str.replace("\\n", "");
        path_list = path_str.split(" ")
        path = []
        for i in range(len(path_list)):
            if path_list[i] == 'L':
                path.append({'x': float(path_list[i+1]), 'y': float(path_list[i+2])})
        if len(path) == 54:
            start = -1
        else:
            start = svg.find(b"<path", end)

    # get min x and min y from path coordenates
    min_x = 9999
    min_y = 9999
    for p in path:
        if p['x'] < min_x:
            min_x = p['x']
        if p['y'] < min_y:
            min_y = p['y']

    # create original exp with all gates, ? as an and
    new_list = exp_list.copy()
    new_list[op_index] = "^"
    for i in range(len(new_list)):
        if new_list[i] == '?':
            new_list[i] = '^'
    new_exp = Expression(None, None, None, None)
    new_exp = new_exp.createExpression(new_list, False)
    svg = new_exp.getCircuit(output_name)

    # add a white square on top of the chosen gate
    index = svg.find(b'</svg>')
    svg = svg[:index] + b'<rect x="' + bytes(str(min_x-1), 'utf-8') + b'" y="' + bytes(str(min_y-1), 'utf-8') + b'" width="53" height="38" style="fill:white;stroke:black" /></svg>'
    
    return exp, correct_gate, svg
