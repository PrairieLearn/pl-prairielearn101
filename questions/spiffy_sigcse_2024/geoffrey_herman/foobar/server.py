import random
import os

OPTIONS = ["q01", "q02", "q03", "q04", "q05", 
           "q06", "q07", "q08", "q09", "q10",
           "q11", "q12", "q13", "q14", "q15"]

def read_question(data, option):
    with open(f'specs/{option}.txt', 'r') as file:
        data["params"]["code"] = file.read()

def bar(x):
    y = 181

    a = x ^ y
    b = x | y 
    c = x & y 
    d = x + y 
    e = y - x

    return max([a, b, c, d, e])

# Yes, this is repetitive code, but it simulates recursion to ensure correct behavior
# a - array to process
# length - length of the array
def q01_section6(A, x, y):
    temp = bar(A[x])
    baz = bar(y)
    A[x] += temp * baz

def q02_section6(A, x, y):
    temp = bar(A[x]) + 4
    baz = bar(y) - 10
    A[x] += temp * baz

def q03_section6(A, x, y):
    temp = bar(A[x])
    baz = bar(y)
    A[x+1] += temp * baz

def q04_section6(A, x, y):
    temp = bar(A[x])
    baz = bar(y)
    A[x] += (temp * baz) - (x + y)

def q05_section6(A, x, y):
    temp = 10 + bar(A[x])
    baz = 3 - bar(y)
    A[x-1] += temp * baz

def q06_section6(A, x, y):
    temp = bar(A[x+1])
    baz = bar(y)
    A[x] += temp * baz

def q07_section6(A, x, y):
    temp = bar(A[x])
    baz = bar(y)
    A[x] += 3 * (temp + baz)

def q08_section6(A, x, y):
    temp = bar(A[x])
    baz = bar(y)
    A[x-1] -= temp * baz

def q09_section6(A, x, y):
    temp = bar(A[x]) - 6
    baz = 4 * bar(y)
    A[x] += temp * baz

def q10_section6(A, x, y):
    temp = bar(A[x])
    baz = y + bar(y)
    A[x] += temp * baz

def q11_section6(A, x, y):
    temp = A[x] + bar(A[x])
    baz = bar(y)
    A[x] += temp * baz

def q12_section6(A, x, y):
    temp = bar(A[x])
    baz = bar(y)
    A[x] = temp * baz

def q13_section6(A, x, y):
    temp = bar(A[x])
    baz = bar(y)
    A[x] += temp * baz + A[x] + y

def q14_section6(A, x, y):
    temp = 10 + bar(A[x])
    baz = 25 - bar(y)
    A[x] += temp * baz

def q15_section6(A, x, y):
    temp = bar(A[x])
    baz = bar(y)
    A[x] = temp * baz

FUNCTIONS = [
    q01_section6, q02_section6, q03_section6, q04_section6,
    q05_section6, q06_section6, q07_section6, q08_section6,
    q09_section6, q10_section6, q11_section6, q12_section6,
    q13_section6, q14_section6, q15_section6
]

function_library = {}

for i in range(len(FUNCTIONS)):
    function_library[OPTIONS[i]] = FUNCTIONS[i]

def generate(data):
    # metadata for the autograder
    NUM_TESTS = 4

    data['params']['problem'] = 'foo'  # name of function being run
    data['params']['numTests'] = NUM_TESTS          # number of tests to run
    data['params']['evilTests'] = True     # True: check for callee save (need main_evil_[].s ) False, do not check for callee save. 
    data['params']['regular_weight'] = 60  # percent weighting to give non-evil tests, if evilTests is false, make this 100
    correct = []                            # list of test case strings

    question_choice = random.choice(OPTIONS) # Pick a random question

    read_question(data, question_choice)

    arrays = [
        [0, 13, 3, -4], 
        [1, 2, 3, 4, 5, 6, 7, 8, 9], 
        [10, 20, 40, 30], 
        [0, 0, 0, 0]
    ]
    
    xVals = [2, 4, 1, 2]
    yVals = [3, 5, 12, 8]

    # Desired correct string to be produced by first test case
    # The main MIPS function should print something similar
    for ii in range(NUM_TESTS):
        out_str = ''

        function_library[question_choice](arrays[ii], xVals[ii], yVals[ii])

        for arrOut in arrays[ii]:
            out_str += f'{arrOut} '

        correct.append(out_str)

    # correct is a list of test cases for the autograder, one test case per row
    data['params']['correct'] = correct
    data['params']['test0'] = correct[0]
    data['params']['test1'] = correct[1]

    return data

def file(data):
    correct = data['params']['correct']
    temp_string = 'Expected \n'
    temp_string += str(correct[0]) + '\n' + str(correct[1])
    #correct = data['params']['correct']
    if data['filename']=='output.txt':
        return temp_string
