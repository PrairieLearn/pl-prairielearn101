from logicExpression import *
from collections import namedtuple

Argument = namedtuple("Argument", "key premises conclusion contradiction hardship")
argument_list = []

exp1 = Expression(None, None, None, None)
exp2 = Expression(None, None, None, None)
exp3 = Expression(None, None, None, None)
exp4 = Expression(None, None, None, None)
exp5 = Expression(None, None, None, None)
exp6 = Expression(None, None, None, None)
exp7 = Expression(None, None, None, None)
conc = Expression(None, None, None, None)


e1 = ["~", "(", "(", "e", "v", "~", "b", ")", "v", "d", ")"]
e2 = ["(", "~", "c", "->", "(", "~", "d", "v", "a", ")", ")"]
e3 = ["(", "f", "->", "(", "b", "v", "c", ")", ")"]
e4 = ["(", "a", "->", "e", ")"]
e5 = ["(", "b", "v", "c", ")"]
e6 = ["(", "(", "~", "c", "->", "(", "~", "d", "v", "a", ")", ")", "^", "(", "(", "~", "d", "v", "a", ")", "->", "~", "c", ")", ")"]
c = ["(", "~", "a", "^", "b", ")"]
premises = []
exp1 = exp1.createExpression(e1, False)
premises.append(exp1)
exp2 = exp2.createExpression(e2, False)
premises.append(exp2)
exp3 = exp3.createExpression(e3, False)
premises.append(exp3)
exp4 = exp4.createExpression(e4, False)
premises.append(exp4)
exp5 = exp5.createExpression(e5, False)
premises.append(exp5)
exp6 = exp6.createExpression(e6, False)
premises.append(exp6)
conc = conc.createExpression(c, False)
argument_list.append(Argument(1, premises, conc, False, "M")) #8steps


e1 = ["(", "c", "v", "d", ")"]
e2 = ["(", "~", "d", "->", "~", "e", ")"]
e3 = ["(", "(", "~", "f", "^", "c", ")", "->", "a", ")"]
e4 = ["~", "d"]
e5 = ["(", "~", "b", "v", "d", ")"]
e6 = ["(", "g", "v", "d", ")"]
e7 = ["(", "f", "->", "b", ")"]
c = ["(", "a", "^", "g", ")"]
premises = []
exp1 = exp1.createExpression(e1, False)
premises.append(exp1)
exp2 = exp2.createExpression(e2, False)
premises.append(exp2)
exp3 = exp3.createExpression(e3, False)
premises.append(exp3)
exp4 = exp4.createExpression(e4, False)
premises.append(exp4)
exp5 = exp5.createExpression(e5, False)
premises.append(exp5)
exp6 = exp6.createExpression(e6, False)
premises.append(exp6)
exp7 = exp7.createExpression(e7, False)
premises.append(exp7)
conc = conc.createExpression(c, False)
argument_list.append(Argument(2, premises, conc, False, "M")) #7steps


e1 = ["(", "(", "~", "d", "v", "e", ")", "v", "c", ")"]
e2 = ["(", "c", "->", "(", "~", "b", "^", "~", "g", ")", ")"]
e3 = ["(", "f", "^", "d", ")"]
e4 = ["(", "a", "->", "~", "e", ")"]
e5 = ["~", "(", "~", "a", "^", "f", ")"]
c = ["~", "b"]
premises = []
exp1 = exp1.createExpression(e1, False)
premises.append(exp1)
exp2 = exp2.createExpression(e2, False)
premises.append(exp2)
exp3 = exp3.createExpression(e3, False)
premises.append(exp3)
exp4 = exp4.createExpression(e4, False)
premises.append(exp4)
exp5 = exp5.createExpression(e5, False)
premises.append(exp5)
conc = conc.createExpression(c, False)
argument_list.append(Argument(3, premises, conc, False, "M")) #8steps


e1 = ["(", "e", "(+)", "b", ")"]
e2 = ["(", "d", "->", "(", "c", "^", "e", ")", ")"]
e3 = ["(", "a", "<->", "b", ")"]
e4 = ["e"]
c = ["~", "a"]
premises = []
exp1 = exp1.createExpression(e1, False)
premises.append(exp1)
exp2 = exp2.createExpression(e2, False)
premises.append(exp2)
exp3 = exp3.createExpression(e3, False)
premises.append(exp3)
exp4 = exp4.createExpression(e4, False)
premises.append(exp4)
conc = conc.createExpression(c, False)
argument_list.append(Argument(4, premises, conc, False, "M")) #7steps


e1 = ["(", "a", "v", "b", ")"]
e2 = ["(", "b", "->", "d", ")"]
e3 = ["(", "(", "a", "^", "c", ")", "->", "e", ")"]
e4 = ["~", "d"]
e5 = ["(", "~", "b", "->", "(", "d", "^", "c", ")", ")"]
c = ["e"]
premises = []
exp1 = exp1.createExpression(e1, False)
premises.append(exp1)
exp2 = exp2.createExpression(e2, False)
premises.append(exp2)
exp3 = exp3.createExpression(e3, False)
premises.append(exp3)
exp4 = exp4.createExpression(e4, False)
premises.append(exp4)
exp5 = exp5.createExpression(e5, False)
premises.append(exp5)
conc = conc.createExpression(c, False)
argument_list.append(Argument(5, premises, conc, True, "M")) #6steps


e1 = ["(", "(", "~", "a", "v", "b", ")", "->", "c", ")"]
e2 = ["(", "c", "->", "(", "d", "v", "e", ")", ")"]
e3 = ["(", "~", "d", "^", "~", "a", ")"]
e4 = ["(", "~", "a", "->", "~", "e", ")"]
c = ["a"]
premises = []
exp1 = exp1.createExpression(e1, False)
premises.append(exp1)
exp2 = exp2.createExpression(e2, False)
premises.append(exp2)
exp3 = exp3.createExpression(e3, False)
premises.append(exp3)
exp4 = exp4.createExpression(e4, False)
premises.append(exp4)
conc = conc.createExpression(c, False)
argument_list.append(Argument(6, premises, conc, True, "H")) #9steps


e1 = ["(", "b", "^", "a", ")"]
e2 = ["(", "~", "c", "v", "~", "(", "a", "^", "~", "e", ")", ")"]
e3 = ["(", "b", "->", "(", "c", "^", "d", ")", ")"]
c = ["e"]
premises = []
exp1 = exp1.createExpression(e1, False)
premises.append(exp1)
exp2 = exp2.createExpression(e2, False)
premises.append(exp2)
exp3 = exp3.createExpression(e3, False)
premises.append(exp3)
conc = conc.createExpression(c, False)
argument_list.append(Argument(7, premises, conc, False, "M")) #8steps


e1 = ["(", "a", "v", "b", ")"]
e2 = ["(", "b", "->", "c", ")"]
e3 = ["(", "(", "a", "^", "d", ")", "->", "e", ")"]
e4 = ["(", "~", "b", "->", "(", "d", "^", "f", ")", ")"]
e5 = ["~", "c"]
c = ["e"]
premises = []
exp1 = exp1.createExpression(e1, False)
premises.append(exp1)
exp2 = exp2.createExpression(e2, False)
premises.append(exp2)
exp3 = exp3.createExpression(e3, False)
premises.append(exp3)
exp4 = exp4.createExpression(e4, False)
premises.append(exp4)
exp5 = exp5.createExpression(e5, False)
premises.append(exp5)
conc = conc.createExpression(c, False)
argument_list.append(Argument(8, premises, conc, False, "M")) #6steps


e1 = ["(", "b", "->", "d", ")"]
e2 = ["(", "e", "->", "f", ")"]
e3 = ["(", "~", "c", "v", "a", ")"]
e4 = ["(", "(", "f", "^", "a", ")", "->", "~", "d", ")"]
e5 = ["(", "e", "^", "c", ")"]
c = ["~", "b"]
premises = []
exp1 = exp1.createExpression(e1, False)
premises.append(exp1)
exp2 = exp2.createExpression(e2, False)
premises.append(exp2)
exp3 = exp3.createExpression(e3, False)
premises.append(exp3)
exp4 = exp4.createExpression(e4, False)
premises.append(exp4)
exp5 = exp5.createExpression(e5, False)
premises.append(exp5)
conc = conc.createExpression(c, False)
argument_list.append(Argument(9, premises, conc, False, "M")) #7steps


e1 = ["(", "a", "(+)", "b", ")"]
e2 = ["(", "(", "d", "->", "c", ")", "->", "e", ")"]
e3 = ["(", "(", "e", "->", "f", ")", "v", "g", ")"]
e4 = ["(", "c", "v", "~", "b", ")"]
e5 = ["(", "~", "g", "^", "~", "f", ")"]
c = ["(", "a", "^", "d", ")"]
premises = []
exp1 = exp1.createExpression(e1, False)
premises.append(exp1)
exp2 = exp2.createExpression(e2, False)
premises.append(exp2)
exp3 = exp3.createExpression(e3, False)
premises.append(exp3)
exp4 = exp4.createExpression(e4, False)
premises.append(exp4)
exp5 = exp5.createExpression(e5, False)
premises.append(exp5)
conc = conc.createExpression(c, False)
argument_list.append(Argument(10, premises, conc, False, "H")) #15steps


e1 = ["(", "d", "(+)", "e", ")"]
e2 = ["(", "d", "v", "a", ")"]
e3 = ["~", "(", "b", "v", "a", ")"]
e4 = ["(", "(", "c", "^", "~", "b", ")", "->", "e", ")"]
c = ["~", "c"]
premises = []
exp1 = exp1.createExpression(e1, False)
premises.append(exp1)
exp2 = exp2.createExpression(e2, False)
premises.append(exp2)
exp3 = exp3.createExpression(e3, False)
premises.append(exp3)
exp4 = exp4.createExpression(e4, False)
premises.append(exp4)
conc = conc.createExpression(c, False)
argument_list.append(Argument(11, premises, conc, False, "H")) #10steps


e1 = ["(", "b", "v", "e", ")"]
e2 = ["(", "c", "->", "~", "a", ")"]
e3 = ["(", "d", "(+)", "e", ")"]
e4 = ["(", "e", "->", "(", "c", "v", "d", ")", ")"]
e5 = ["~", "(", "a", "->", "b", ")"]
c = ["~", "a"]
premises = []
exp1 = exp1.createExpression(e1, False)
premises.append(exp1)
exp2 = exp2.createExpression(e2, False)
premises.append(exp2)
exp3 = exp3.createExpression(e3, False)
premises.append(exp3)
exp4 = exp4.createExpression(e4, False)
premises.append(exp4)
exp5 = exp5.createExpression(e5, False)
premises.append(exp5)
conc = conc.createExpression(c, False)
argument_list.append(Argument(12, premises, conc, True, "H")) #12steps


e1 = ["(", "a", "(+)", "e", ")"]
e2 = ["(", "c", "->", "(", "e", "v", "b", ")", ")"]
e3 = ["(", "d", "->", "c", ")"]
e4 = ["(", "b", "->", "~", "a", ")"]
e5 = ["~", "e"]
c = ["~", "d"]
premises = []
exp1 = exp1.createExpression(e1, False)
premises.append(exp1)
exp2 = exp2.createExpression(e2, False)
premises.append(exp2)
exp3 = exp3.createExpression(e3, False)
premises.append(exp3)
exp4 = exp4.createExpression(e4, False)
premises.append(exp4)
exp5 = exp5.createExpression(e5, False)
premises.append(exp5)
conc = conc.createExpression(c, False)
argument_list.append(Argument(13, premises, conc, False, "M")) #8steps


e1 = ["~", "(", "a", "^", "b", ")"]
e2 = ["(", "c", "->", "(", "a", "v", "~", "d", ")", ")"]
e3 = ["b"]
e4 = ["(", "(", "e", "^", "~", "a", ")",  "->", "c", ")"]
e5 = ["~", "(", "a", "->", "~", "d", ")"]
c = ["~", "e"]
premises = []
exp1 = exp1.createExpression(e1, False)
premises.append(exp1)
exp2 = exp2.createExpression(e2, False)
premises.append(exp2)
exp3 = exp3.createExpression(e3, False)
premises.append(exp3)
exp4 = exp4.createExpression(e4, False)
premises.append(exp4)
exp5 = exp5.createExpression(e5, False)
premises.append(exp5)
conc = conc.createExpression(c, False)
argument_list.append(Argument(14, premises, conc, True, "H")) #12steps


e1 = ["(", "~", "(", "a", "v", "b", ")", "->", "a", ")"]
e2 = ["~", "(", "c", "->", "~", "a", ")"]
e3 = ["~", "(", "c", "^", "~", "f", ")"]
e4 = ["(", "~", "f", "v", "g", ")"]
e5 = ["(", "~", "(", "b", "v", "d", ")", "->", "e", ")"]
c = ["g"]
premises = []
exp1 = exp1.createExpression(e1, False)
premises.append(exp1)
exp2 = exp2.createExpression(e2, False)
premises.append(exp2)
exp3 = exp3.createExpression(e3, False)
premises.append(exp3)
exp4 = exp4.createExpression(e4, False)
premises.append(exp4)
exp5 = exp5.createExpression(e5, False)
premises.append(exp5)
conc = conc.createExpression(c, False)
argument_list.append(Argument(15, premises, conc, False, "H")) #9steps


e1 = ["a"]
e2 = ["(", "~", "c", "->", "b", ")"]
e3 = ["(", "(", "a", "v", "d", ")", "->", "~", "b", ")"]
e4 = ["(", "~", "b", "->", "~", "d", ")"]
c = ["~", "(", "c", "->", "d", ")"]
premises = []
exp1 = exp1.createExpression(e1, False)
premises.append(exp1)
exp2 = exp2.createExpression(e2, False)
premises.append(exp2)
exp3 = exp3.createExpression(e3, False)
premises.append(exp3)
exp4 = exp4.createExpression(e4, False)
premises.append(exp4)
conc = conc.createExpression(c, False)
argument_list.append(Argument(16, premises, conc, False, "M")) #7steps


e1 = ["(", "c", "v", "~", "a", ")"]
e2 = ["(", "~", "d", "->", "~", "b", ")"]
e3 = ["(", "c", "->", "b", ")"]
e4 = ["(", "a", "^", "~", "d", ")"]
c = ["~", "a"]
premises = []
exp1 = exp1.createExpression(e1, False)
premises.append(exp1)
exp2 = exp2.createExpression(e2, False)
premises.append(exp2)
exp3 = exp3.createExpression(e3, False)
premises.append(exp3)
exp4 = exp4.createExpression(e4, False)
premises.append(exp4)
conc = conc.createExpression(c, False)
argument_list.append(Argument(17, premises, conc, True, "E")) #4steps


e1 = ["(", "(", "b", "^", "a", ")", "->", "~", "d", ")"]
e2 = ["~", "(", "~", "c", "v", "~", "a", ")"]
e3 = ["(", "~", "d", "->", "~", "c", ")"]
c = ["~", "b"]
premises = []
exp1 = exp1.createExpression(e1, False)
premises.append(exp1)
exp2 = exp2.createExpression(e2, False)
premises.append(exp2)
exp3 = exp3.createExpression(e3, False)
premises.append(exp3)
conc = conc.createExpression(c, False)
argument_list.append(Argument(18, premises, conc, False, "H")) #9steps


e1 = ["(", "(", "~", "a", "^", "b", ")", "->", "~", "c", ")"]
e2 = ["c"]
e3 = ["b"]
c = ["(", "a", "^", "c", ")"]
premises = []
exp1 = exp1.createExpression(e1, False)
premises.append(exp1)
exp2 = exp2.createExpression(e2, False)
premises.append(exp2)
exp3 = exp3.createExpression(e3, False)
premises.append(exp3)
conc = conc.createExpression(c, False)
argument_list.append(Argument(19, premises, conc, False, "E")) #5steps


e1 = ["(", "(", "a", "v", "b", ")", "->", "c", ")"]
e2 = ["a"]
c = ["~", "(", "a", "->", "~", "c", ")"]
premises = []
exp1 = exp1.createExpression(e1, False)
premises.append(exp1)
exp2 = exp2.createExpression(e2, False)
premises.append(exp2)
conc = conc.createExpression(c, False)
argument_list.append(Argument(20, premises, conc, False, "E")) #5steps


e1 = ["b"]
e2 = ["(", "(", "a", "->", "c", ")", "->", "(", "d", "^", "e", ")", ")"]
e3 = ["(", "b", "->", "c", ")"]
c = ["e"]
premises = []
exp1 = exp1.createExpression(e1, False)
premises.append(exp1)
exp2 = exp2.createExpression(e2, False)
premises.append(exp2)
exp3 = exp3.createExpression(e3, False)
premises.append(exp3)
conc = conc.createExpression(c, False)
argument_list.append(Argument(21, premises, conc, False, "E")) #5steps


e1 = ["(", "a", "^", "~", "(", "a", "^", "b", ")", ")"]
e2 = ["(", "(", "a", "->", "~", "b", ")", "->", "(", "c", "v", "d", ")", ")"]
e3 = ["~", "d"]
c = ["c"]
premises = []
exp1 = exp1.createExpression(e1, False)
premises.append(exp1)
exp2 = exp2.createExpression(e2, False)
premises.append(exp2)
exp3 = exp3.createExpression(e3, False)
premises.append(exp3)
conc = conc.createExpression(c, False)
argument_list.append(Argument(22, premises, conc, False, "E")) #5steps


e1 = ["(", "(", "~", "d", "v", "b", ")", "v", "f", ")"]
e2 = ["(", "c", "^", "d", ")"]
e3 = ["(", "c", "->", "(", "a", "v", "(", "a", "^", "e", ")", ")", ")"]
e4 = ["(", "b", "->", "~", "a", ")"]
c = ["f"]
premises = []
exp1 = exp1.createExpression(e1, False)
premises.append(exp1)
exp2 = exp2.createExpression(e2, False)
premises.append(exp2)
exp3 = exp3.createExpression(e3, False)
premises.append(exp3)
exp4 = exp4.createExpression(e4, False)
premises.append(exp4)
conc = conc.createExpression(c, False)
argument_list.append(Argument(23, premises, conc, False, "H")) #10steps


e1 = ["(", "(", "a", "v", "b", ")", "->", "c", ")"]
e2 = ["(", "d", "v", "(", "d", "^", "a", ")", ")"]
e3 = ["(", "~", "b", "->", "e", ")"]
e4 = ["~", "(", "c", "^", "d", ")"]
c = ["e"]
premises = []
exp1 = exp1.createExpression(e1, False)
premises.append(exp1)
exp2 = exp2.createExpression(e2, False)
premises.append(exp2)
exp3 = exp3.createExpression(e3, False)
premises.append(exp3)
exp4 = exp4.createExpression(e4, False)
premises.append(exp4)
conc = conc.createExpression(c, False)
argument_list.append(Argument(24, premises, conc, False, "H")) #9steps

e1 = ["(", "a", "->", "b", ")"]
e2 = ["(", "b", "<->", "c", ")"]
c = ["(", "a", "->", "c", ")"]
premises = []
exp1 = exp1.createExpression(e1, False)
premises.append(exp1)
exp2 = exp2.createExpression(e2, False)
premises.append(exp2)
conc = conc.createExpression(c, False)
argument_list.append(Argument(25, premises, conc, False, "E")) #3steps


e1 = ["(", "a", "->", "(", "b", "^", "c", ")", ")"]
e2 = ["~", "c"]
e3 = ["(", "a", "^", "~", "d", ")"]
c = ["(", "b", "v", "d", ")"]
premises = []
exp1 = exp1.createExpression(e1, False)
premises.append(exp1)
exp2 = exp2.createExpression(e2, False)
premises.append(exp2)
exp3 = exp3.createExpression(e3, False)
premises.append(exp3)
conc = conc.createExpression(c, False)
argument_list.append(Argument(26, premises, conc, True, "E")) #4steps


e1 = ["(", "a", "->", "b", ")"]
e2 = ["(", "c", "->", "d", ")"]
e3 = ["(", "~", "c", "v", "~", "d", ")"]
c = ["(", "~", "a", "v", "~", "c", ")"]
premises = []
exp1 = exp1.createExpression(e1, False)
premises.append(exp1)
exp2 = exp2.createExpression(e2, False)
premises.append(exp2)
exp3 = exp3.createExpression(e3, False)
premises.append(exp3)
conc = conc.createExpression(c, False)
argument_list.append(Argument(27, premises, conc, True, "E")) #4steps


e1 = ["(", "a", "v", "b", ")"]
e2 = ["(", "~", "a", "^", "~", "c", ")"]
c = ["(", "b", "v", "c", ")"]
premises = []
exp1 = exp1.createExpression(e1, False)
premises.append(exp1)
exp2 = exp2.createExpression(e2, False)
premises.append(exp2)
conc = conc.createExpression(c, False)
argument_list.append(Argument(28, premises, conc, False, "E")) #3steps


e1 = ["(", "a", "->", "b", ")"]
e2 = ["(", "b", "->", "c", ")"]
e3 = ["~", "c"]
c = ["(", "a", "<->", "c", ")"]
premises = []
exp1 = exp1.createExpression(e1, False)
premises.append(exp1)
exp2 = exp2.createExpression(e2, False)
premises.append(exp2)
exp3 = exp3.createExpression(e3, False)
premises.append(exp3)
conc = conc.createExpression(c, False)
argument_list.append(Argument(29, premises, conc, False, "E")) #5steps


e1 = ["(", "(", "a", "->", "b", ")", "^", "(", "c", "->", "a", ")", ")"]
e2 = ["c"]
c = ["(", "~", "(", "a", "^", "c", ")", "->", "~", "(", "b", "^", "d", ")", ")"]
premises = []
exp1 = exp1.createExpression(e1, False)
premises.append(exp1)
exp2 = exp2.createExpression(e2, False)
premises.append(exp2)
conc = conc.createExpression(c, False)
argument_list.append(Argument(30, premises, conc, False, "M")) #6steps


e1 = ["(", "a", "->", "b", ")"]
c = ["(", "a", "->", "(", "b", "^", "b", ")", ")"]
premises = []
exp1 = exp1.createExpression(e1, False)
premises.append(exp1)
conc = conc.createExpression(c, False)
argument_list.append(Argument(31, premises, conc, False, "M")) #4steps


e1 = ["(", "a", "v", "b", ")"]
e2 = ["(", "a", "->", "c", ")"]
e3 = ["(", "b", "->", "d", ")"]
c = ["(", "c", "v", "d", ")"]
premises = []
exp1 = exp1.createExpression(e1, False)
premises.append(exp1)
exp2 = exp2.createExpression(e2, False)
premises.append(exp2)
exp3 = exp3.createExpression(e3, False)
premises.append(exp3)
conc = conc.createExpression(c, False)
argument_list.append(Argument(32, premises, conc, False, "E")) #4steps


e1 = ["(", "a", "->", "b", ")"]
e2 = ["(", "b", "->", "c", ")"]
c = ["(", "(", "a", "^", "~", "c", ")", "->", "~", "b", ")"]
premises = []
exp1 = exp1.createExpression(e1, False)
premises.append(exp1)
exp2 = exp2.createExpression(e2, False)
premises.append(exp2)
conc = conc.createExpression(c, False)
argument_list.append(Argument(33, premises, conc, False, "M")) #5steps


e1 = ["(", "a", "->", "b", ")"]
e2 = ["(", "(", "b", "->", "c", ")", "^", "(", "d", "->", "e", ")", ")"]
e3 = ["(", "a", "v", "d", ")"]
c = ["(", "c", "v", "e", ")"]
premises = []
exp1 = exp1.createExpression(e1, False)
premises.append(exp1)
exp2 = exp2.createExpression(e2, False)
premises.append(exp2)
exp3 = exp3.createExpression(e3, False)
premises.append(exp3)
conc = conc.createExpression(c, False)
argument_list.append(Argument(34, premises, conc, False, "H")) #8steps


e1 = ["(", "(", "a", "->", "b", ")", "v", "(", "c", "->", "d", ")", ")"]
e2 = ["(", "a", "^", "c", ")"]
c = ["(", "b", "v", "d", ")"]
premises = []
exp1 = exp1.createExpression(e1, False)
premises.append(exp1)
exp2 = exp2.createExpression(e2, False)
premises.append(exp2)
conc = conc.createExpression(c, False)
argument_list.append(Argument(35, premises, conc, False, "H")) #9steps


e1 = ["(", "(", "a", "^", "b", ")", "->", "c", ")"]
e2 = ["(", "(", "d", "v", "e", ")", "->", "b", ")"]
e3 = ["(", "a", "^", "d", ")"]
c = ["(", "c", "v", "e", ")"]
premises = []
exp1 = exp1.createExpression(e1, False)
premises.append(exp1)
exp2 = exp2.createExpression(e2, False)
premises.append(exp2)
exp3 = exp3.createExpression(e3, False)
premises.append(exp3)
conc = conc.createExpression(c, False)
argument_list.append(Argument(36, premises, conc, False, "M")) #7steps


e1 = ["(", "(", "a", "^", "b", ")", "->", "c", ")"]
e2 = ["(", "(", "d", "v", "e", ")", "->", "b", ")"]
e3 = ["(", "(", "c", "v", "f", ")", "->", "g", ")"]
e4 = ["(", "a", "^", "d", ")"]
c = ["g"]
premises = []
exp1 = exp1.createExpression(e1, False)
premises.append(exp1)
exp2 = exp2.createExpression(e2, False)
premises.append(exp2)
exp3 = exp3.createExpression(e3, False)
premises.append(exp3)
exp4 = exp4.createExpression(e4, False)
premises.append(exp4)
conc = conc.createExpression(c, False)
argument_list.append(Argument(37, premises, conc, False, "M")) #8steps


e1 = ["(", "(", "e", "^", "f", ")", "->", "c", ")"]
e2 = ["(", "d", "->", "(", "a", "v", "e", ")", ")"]
e3 = ["(", "(", "c", "^", "f", ")", "->", "g", ")"]
e4 = ["(", "e", "->", "f", ")"]
e5 = ["(", "d", "^", "~", "a", ")"]
c = ["(", "g", "^", "e", ")"]
premises = []
exp1 = exp1.createExpression(e1, False)
premises.append(exp1)
exp2 = exp2.createExpression(e2, False)
premises.append(exp2)
exp3 = exp3.createExpression(e3, False)
premises.append(exp3)
exp4 = exp4.createExpression(e4, False)
premises.append(exp4)
exp5 = exp5.createExpression(e5, False)
premises.append(exp5)
conc = conc.createExpression(c, False)
argument_list.append(Argument(38, premises, conc, False, "H")) #10steps


e1 = ["(", "(", "a", "v", "b", ")", "->", "c", ")"]
e2 = ["(", "d", "->", "(", "a", "^", "f", ")", ")"]
e3 = ["(", "(", "c", "^", "f", ")", "->", "g", ")"]
e4 = ["(", "b", "^", "d", ")"]
c = ["(", "g", "v", "e", ")"]
premises = []
exp1 = exp1.createExpression(e1, False)
premises.append(exp1)
exp2 = exp2.createExpression(e2, False)
premises.append(exp2)
exp3 = exp3.createExpression(e3, False)
premises.append(exp3)
exp4 = exp4.createExpression(e4, False)
premises.append(exp4)
conc = conc.createExpression(c, False)
argument_list.append(Argument(39, premises, conc, False, "H")) #9steps


e1 = ["(", "a", "->", "(", "b", "^", "c", ")", ")"]
e2 = ["(", "(", "d", "v", "e", ")", "->", "b", ")"]
e3 = ["(", "(", "f", "^", "g", ")", "->", "d", ")"]
e4 = ["(", "a", "^", "f", ")"]
e5 = ["(", "c", "->", "g", ")"]
c = ["(", "e", "->", "(", "b", "v", "d", ")", ")"]
premises = []
exp1 = exp1.createExpression(e1, False)
premises.append(exp1)
exp2 = exp2.createExpression(e2, False)
premises.append(exp2)
exp3 = exp3.createExpression(e3, False)
premises.append(exp3)
exp4 = exp4.createExpression(e4, False)
premises.append(exp4)
exp5 = exp5.createExpression(e5, False)
premises.append(exp5)
conc = conc.createExpression(c, False)
argument_list.append(Argument(40, premises, conc, False, "M")) #6steps


e1 = ["(", "a", "->", "(", "b", "^", "c", ")", ")"]
e2 = ["(", "b", "->", "(", "d", "v", "e", ")", ")"]
e3 = ["(", "c", "->", "(", "f", "^", "g", ")", ")"]
e4 = ["~", "f"]
e5 = ["(", "a", "v", "c", ")"]
c = ["(", "~", "g", "->", "~", "d", ")"]
premises = []
exp1 = exp1.createExpression(e1, False)
premises.append(exp1)
exp2 = exp2.createExpression(e2, False)
premises.append(exp2)
exp3 = exp3.createExpression(e3, False)
premises.append(exp3)
exp4 = exp4.createExpression(e4, False)
premises.append(exp4)
exp5 = exp5.createExpression(e5, False)
premises.append(exp5)
conc = conc.createExpression(c, False)
argument_list.append(Argument(41, premises, conc, True, "H")) #9steps


e1 = ["(", "(", "a", "^", "b", ")", "->", "c", ")"]
e2 = ["(", "(", "d", "v", "e", ")", "->", "a", ")"]
e3 = ["(", "f", "->", "(", "g", "^", "b", ")", ")"]
e4 = ["(", "d", "^", "f", ")"]
e5 = ["(", "e", "v", "g", ")"]
c = ["(", "c", "->", "(", "a", "v", "g", ")", ")"]
premises = []
exp1 = exp1.createExpression(e1, False)
premises.append(exp1)
exp2 = exp2.createExpression(e2, False)
premises.append(exp2)
exp3 = exp3.createExpression(e3, False)
premises.append(exp3)
exp4 = exp4.createExpression(e4, False)
premises.append(exp4)
exp5 = exp5.createExpression(e5, False)
premises.append(exp5)
conc = conc.createExpression(c, False)
argument_list.append(Argument(42, premises, conc, False, "H")) #7steps


e1 = ["(", "a", "->", "(", "b", "^", "c", ")", ")"]
e2 = ["(", "c", "->", "(", "d", "v", "a", ")", ")"]
e3 = ["(", "(", "b", "^", "c", ")", "->", "~", "a", ")"]
e4 = ["(", "c", "^", "~", "d", ")"]
c = ["(", "~", "a", "^", "b", ")"]
premises = []
exp1 = exp1.createExpression(e1, False)
premises.append(exp1)
exp2 = exp2.createExpression(e2, False)
premises.append(exp2)
exp3 = exp3.createExpression(e3, False)
premises.append(exp3)
exp4 = exp4.createExpression(e4, False)
premises.append(exp4)
conc = conc.createExpression(c, False)
argument_list.append(Argument(43, premises, conc, True, "M")) #8steps


e1 = ["(", "(", "a", "^", "b", ")", "->", "e", ")"]
e2 = ["(", "(", "c", "v", "d", ")", "->", "a", ")"]
e3 = ["(", "~", "b", "->", "d", ")"]
e4 = ["(", "c", "^", "~", "d", ")"]
c = ["e"]
premises = []
exp1 = exp1.createExpression(e1, False)
premises.append(exp1)
exp2 = exp2.createExpression(e2, False)
premises.append(exp2)
exp3 = exp3.createExpression(e3, False)
premises.append(exp3)
exp4 = exp4.createExpression(e4, False)
premises.append(exp4)
conc = conc.createExpression(c, False)
argument_list.append(Argument(44, premises, conc, False, "H")) #8steps


e1 = ["(", "a", "->", "(", "b", "v", "c", ")", ")"]
e2 = ["(", "b", "->", "~", "(", "d", "v", "~", "e", ")", ")"]
e3 = ["(", "c", "->", "~", "(", "f", "^", "~", "d", ")", ")"]
e4 = ["(", "~", "f", "->", "~", "(", "a", "v", "~", "e", ")", ")"]
e5 = ["~", "(", "d", "v", "e", ")"]
e6 = ["~", "c"]
c = ["~", "(", "a", "v", "~", "f", ")"]
premises = []
exp1 = exp1.createExpression(e1, False)
premises.append(exp1)
exp2 = exp2.createExpression(e2, False)
premises.append(exp2)
exp3 = exp3.createExpression(e3, False)
premises.append(exp3)
exp4 = exp4.createExpression(e4, False)
premises.append(exp4)
exp5 = exp5.createExpression(e5, False)
premises.append(exp5)
exp6 = exp6.createExpression(e6, False)
premises.append(exp6)
conc = conc.createExpression(c, False)
argument_list.append(Argument(45, premises, conc, False, "H")) #12steps


e1 = ["(", "a", "->", "(", "b", "^", "c", ")", ")"]
e2 = ["(", "b", "->", "~", "(", "d", "v", "e", ")", ")"]
e3 = ["(", "c", "->", "(", "~", "d", "^", "f", ")", ")"]
e4 = ["(", "e", "v", "f", ")"]
e5 = ["(", "~", "a", "^", "b", ")"]
e6 = ["(", "~", "c", "^", "d", ")"]
c = ["f"]
premises = []
exp1 = exp1.createExpression(e1, False)
premises.append(exp1)
exp2 = exp2.createExpression(e2, False)
premises.append(exp2)
exp3 = exp3.createExpression(e3, False)
premises.append(exp3)
exp4 = exp4.createExpression(e4, False)
premises.append(exp4)
exp5 = exp5.createExpression(e5, False)
premises.append(exp5)
exp6 = exp6.createExpression(e6, False)
premises.append(exp6)
conc = conc.createExpression(c, False)
argument_list.append(Argument(46, premises, conc, False, "M")) #5steps


e1 = ["(", "(", "a", "^", "b", ")", "->", "c", ")"]
e2 = ["(", "b", "->", "(", "d", "v", "f", ")", ")"]
e3 = ["(", "(", "f", "^", "b", ")", "->", "a", ")"]
c = ["(", "(", "b", "^", "~", "d", ")", "->", "c", ")"]
premises = []
exp1 = exp1.createExpression(e1, False)
premises.append(exp1)
exp2 = exp2.createExpression(e2, False)
premises.append(exp2)
exp3 = exp3.createExpression(e3, False)
premises.append(exp3)
conc = conc.createExpression(c, False)
argument_list.append(Argument(47, premises, conc, False, "XH")) #25steps


e1 = ["(", "(", "a", "^", "b", ")", "->", "c", ")"]
e2 = ["(", "c", "v", "d", ")"]
e3 = ["(", "b", "->", "d", ")"]
c = ["d"]
premises = []
exp1 = exp1.createExpression(e1, False)
premises.append(exp1)
exp2 = exp2.createExpression(e2, False)
premises.append(exp2)
exp3 = exp3.createExpression(e3, False)
premises.append(exp3)
conc = conc.createExpression(c, False)
e1 = ["(", "a", "->", "b", ")"]
e2 = ["(", "b", "<->", "c", ")"]
c = ["(", "a", "->", "c", ")"]
premises = []
exp1 = exp1.createExpression(e1, False)
premises.append(exp1)
exp2 = exp2.createExpression(e2, False)
premises.append(exp2)
conc = conc.createExpression(c, False)
argument_list.append(Argument(48, premises, conc, False, "E")) #3steps


e1 = ["(", "a", "->", "(", "b", "^", "c", ")", ")"]
e2 = ["~", "c"]
e3 = ["(", "a", "v", "d", ")"]
c = ["d"]
premises = []
exp1 = exp1.createExpression(e1, False)
premises.append(exp1)
exp2 = exp2.createExpression(e2, False)
premises.append(exp2)
exp3 = exp3.createExpression(e3, False)
premises.append(exp3)
conc = conc.createExpression(c, False)
argument_list.append(Argument(49, premises, conc, False, "E")) #5steps


e1 = ["(", "a", "->", "b", ")"]
e2 = ["(", "c", "->", "d", ")"]
e3 = ["(", "~", "c", "v", "~", "d", ")"]
c = ["(", "~", "a", "v", "~", "c", ")"]
premises = []
exp1 = exp1.createExpression(e1, False)
premises.append(exp1)
exp2 = exp2.createExpression(e2, False)
premises.append(exp2)
exp3 = exp3.createExpression(e3, False)
premises.append(exp3)
conc = conc.createExpression(c, False)
argument_list.append(Argument(50, premises, conc, False, "M")) #7steps


e1 = ["(", "a", "->", "(", "b", "^", "c", ")", ")"]
e2 = ["(", "c", "->", "(", "d", "^", "a", ")", ")"]
e3 = ["(", "(", "b", "^", "d", ")", "->", "~", "a", ")"]
e4 = ["(", "c", "^", "~", "d", ")"]
c = ["~", "a"]
premises = []
exp1 = exp1.createExpression(e1, False)
premises.append(exp1)
exp2 = exp2.createExpression(e2, False)
premises.append(exp2)
exp3 = exp3.createExpression(e3, False)
premises.append(exp3)
exp4 = exp4.createExpression(e4, False)
premises.append(exp4)
conc = conc.createExpression(c, False)
argument_list.append(Argument(51, premises, conc, True, "M")) #8steps


e1 = ["(", "a", "->", "b", ")"]
e2 = ["(", "b", "->", "c", ")"]
e3 = ["(", "c", "->", "d", ")"]
e4 = ["(", "d", "->", "~", "a", ")"]
c = ["~", "a"]
premises = []
exp1 = exp1.createExpression(e1, False)
premises.append(exp1)
exp2 = exp2.createExpression(e2, False)
premises.append(exp2)
exp3 = exp3.createExpression(e3, False)
premises.append(exp3)
exp4 = exp4.createExpression(e4, False)
premises.append(exp4)
conc = conc.createExpression(c, False)
argument_list.append(Argument(52, premises, conc, False, "E")) #5steps


e1 = ["(", "e", "->", "(", "b", "v", "c", ")", ")"]
e2 = ["(", "b", "->", "~", "(", "d", "v", "e", ")", ")"]
e3 = ["(", "c", "->", "(", "~", "d", "^", "~", "e", ")", ")"]
e4 = ["(", "(", "a", "v", "b", ")", "->", "e", ")"]
c = ["~", "a"]
premises = []
exp1 = exp1.createExpression(e1, False)
premises.append(exp1)
exp2 = exp2.createExpression(e2, False)
premises.append(exp2)
exp3 = exp3.createExpression(e3, False)
premises.append(exp3)
exp4 = exp4.createExpression(e4, False)
premises.append(exp4)
conc = conc.createExpression(c, False)
argument_list.append(Argument(53, premises, conc, False, "H")) #10steps


e1 = ["(", "(", "a", "^", "b", ")", "->", "c", ")"]
e2 = ["(", "a", "v", "~", "b", ")"]
e3 = ["(", "~", "b", "->", "d", ")"]
e4 = ["(", "a", "->", "~", "e", ")"]
e5 = ["(", "e", "^", "~", "d", ")"]
c = ["c"]
premises = []
exp1 = exp1.createExpression(e1, False)
premises.append(exp1)
exp2 = exp2.createExpression(e2, False)
premises.append(exp2)
exp3 = exp3.createExpression(e3, False)
premises.append(exp3)
exp4 = exp4.createExpression(e4, False)
premises.append(exp4)
exp5 = exp5.createExpression(e5, False)
premises.append(exp5)
conc = conc.createExpression(c, False)
argument_list.append(Argument(54, premises, conc, False, "M")) #6steps


e1 = ["(", "(", "a", "^", "b", ")", "->", "c", ")"]
e2 = ["(", "(", "c", "^", "d", ")", "->", "~", "a", ")"]
e3 = ["b"]
c = ["(", "a", "->", "~", "d", ")"]
premises = []
exp1 = exp1.createExpression(e1, False)
premises.append(exp1)
exp2 = exp2.createExpression(e2, False)
premises.append(exp2)
exp3 = exp3.createExpression(e3, False)
premises.append(exp3)
conc = conc.createExpression(c, False)
argument_list.append(Argument(55, premises, conc, False, "H")) #15steps


e1 = ["(", "a", "->", "(", "b", "^", "c", ")", ")"]
e2 = ["(", "b", "->", "~", "c", ")"]
e3 = ["(", "a", "v", "b", ")"]
c = ["~", "c"]
premises = []
exp1 = exp1.createExpression(e1, False)
premises.append(exp1)
exp2 = exp2.createExpression(e2, False)
premises.append(exp2)
exp3 = exp3.createExpression(e3, False)
premises.append(exp3)
conc = conc.createExpression(c, False)
argument_list.append(Argument(56, premises, conc, False, "M")) #5steps


e1 = ["(", "a", "v", "b", ")"]
e2 = ["~", "a"]
e3 = ["(", "c", "->", "d", ")"]
e4 = ["~", "d"]
c = ["~", "(", "b", "->", "c", ")"]
premises = []
exp1 = exp1.createExpression(e1, False)
premises.append(exp1)
exp2 = exp2.createExpression(e2, False)
premises.append(exp2)
exp3 = exp3.createExpression(e3, False)
premises.append(exp3)
exp4 = exp4.createExpression(e4, False)
premises.append(exp4)
conc = conc.createExpression(c, False)
argument_list.append(Argument(57, premises, conc, False, "M")) #5steps


e1 = ["(", "a", "v", "c", ")"]
e2 = ["(", "a", "->", "b", ")"]
e3 = ["(", "c", "->", "d", ")"]
e4 = ["~", "(", "d", "v", "e", ")"]
c = ["b"]
premises = []
exp1 = exp1.createExpression(e1, False)
premises.append(exp1)
exp2 = exp2.createExpression(e2, False)
premises.append(exp2)
exp3 = exp3.createExpression(e3, False)
premises.append(exp3)
exp4 = exp4.createExpression(e4, False)
premises.append(exp4)
conc = conc.createExpression(c, False)
argument_list.append(Argument(58, premises, conc, True, "M")) #7steps
