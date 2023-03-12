import random
import string
import copy
import numpy as np

# --------------------------------------------------------
# FUNCTIONS FOR GENERATING ANSWERS
# --------------------------------------------------------
  
def make_return_variables(return_variables,parameters,provideCorrectAnswer):

    # WAYS TO MESS THIS UP
    # using the wrong brackets/braces
    # flipping the parameters with the return variables
    # forgetting the return variables
    # mixing up the order of the return variables

    return_variables = copy.deepcopy(return_variables)
    parameters = copy.deepcopy(parameters)

    # here are all the sets of braces we can use
    braces = [
        ["[","]"],
        ["(",")"],
        ["{","}"]
        ]

    # construct the correct answer
    correctAnswer = braces[0][0]
    i = 0
    while i < len(return_variables):
        correctAnswer += return_variables[i]
        if i + 1 < len(return_variables):
            correctAnswer += ", "
        else:
            correctAnswer += braces[0][1]
            break
        i += 1


    if provideCorrectAnswer:
        return correctAnswer

    else: # lets make some wrong answers!

        # pick a set of braces (might be right, might be wrong)
        whichBraces = random.choice([0,0,0,0,1,2]) # 0 is the correct set, so weight that more heavily

        # if the wrong answer forgets the return variables, we can 
        # immediately return a wrong answer (using a random set of braces)
        randomNum = random.randrange(0,6) #increase the upper range to make this happen less often
        forget_to_return_variables = randomNum == 0
        if forget_to_return_variables:
            answer = braces[whichBraces][0] + " " + braces[whichBraces][1]
            return answer

        # otherwise, construct some other wrong answer
        else:

            # maybe flip the parameters with the return variables
            randomNum = random.randrange(0,6) #increase the upper range to make this happen less often
            flipVariables = randomNum == 0 # flip if you got a zero

            # which variables are we using, return variables or parameters?
            if flipVariables:
                variable_set = parameters
            else:
                variable_set = return_variables

            # maybe shuffle the order of the variables
            randomNum = random.randrange(0,3) #increase the upper range to make this happen less often
            mix_it_up = randomNum == 0 # mix it up if you got a zero
            if mix_it_up:
                random.shuffle(variable_set)

            # construct wrong answer
            answer = braces[whichBraces][0]
            i = 0
            while i < len(variable_set):
                answer += variable_set[i]
                if i + 1 < len(variable_set):
                    answer += ", "
                else:
                    answer += braces[whichBraces][1]
                    break
                i += 1

            
            # return the constructed wrong answer!
            return answer


def make_assigned_variables(return_variables,parameters,provideCorrectAnswer):
  
    # WAYS TO MESS THIS UP
    # using the wrong brackets/braces
    # flipping the parameters with the return variables
    # forgetting the return variables
    # mixing up the order of the return variables

    return_variables = copy.deepcopy(return_variables)
    parameters = copy.deepcopy(parameters)

    # here are all the sets of braces we can use
    braces = [
        ["[","]"],
        ["(",")"],
        ["{","}"]
        ]

    correctAnswer = ""

    # construct the correct answer
    if len(return_variables) > 1:
        correctAnswer = braces[0][0]
    i = 0
    while i < len(return_variables):
        correctAnswer += return_variables[i]
        if i + 1 < len(return_variables):
            correctAnswer += ", "
        else:
            if len(return_variables) > 1:
                correctAnswer += braces[0][1]
            break
        i += 1


    if provideCorrectAnswer:
        return correctAnswer

    else: # lets make some wrong answers!

        # pick a set of braces (might be right, might be wrong)
        whichBraces = random.choice([0,0,0,0,1,2]) # 0 is the correct set, so weight that more heavily

        # start with an empty answer
        answer = ""

        # if the wrong answer forgets the return variables, we can 
        # immediately return an empty string
        randomNum = random.randrange(0,6) #increase the upper range to make this happen less often
        forget_to_return_variables = randomNum == 0
        if forget_to_return_variables:
            return answer

        # otherwise, construct some other wrong answer
        else:

            # maybe flip the parameters with the return variables
            randomNum = random.randrange(0,6) #increase the upper range to make this happen less often
            flipVariables = randomNum == 0 # flip if you got a zero

            # which variables are we using, return variables or parameters?
            if flipVariables:
                variable_set = parameters
            else:
                variable_set = return_variables

            # maybe shuffle the order of the variables
            randomNum = random.randrange(0,3) #increase the upper range to make this happen less often
            mix_it_up = randomNum == 0 # mix it up if you got a zero
            if mix_it_up:
                random.shuffle(variable_set)

            # construct wrong answer
            if len(return_variables) > 1:
                answer += braces[whichBraces][0]
            i = 0
            while i < len(variable_set):
                answer += variable_set[i]
                if i + 1 < len(variable_set):
                    answer += ", "
                else:
                    if len(return_variables) > 1:
                        answer += braces[whichBraces][1]
                    break
                i += 1

            
            # return the constructed wrong answer!
            return answer


def make_parameters(return_variables,parameters,provideCorrectAnswer):

    return_variables = copy.deepcopy(return_variables)
    parameters = copy.deepcopy(parameters)
  
    # WAYS TO MESS THIS UP
    # using the wrong brackets/braces
    # flipping the parameters with the return variables
    # forgetting the parameters
    # mixing up the order of the parameters

    # here are all the sets of braces we can use
    braces = [
        ["[","]"],
        ["(",")"],
        ["{","}"]
        ]

    # construct the correct answer
    correctAnswer = braces[1][0]
    i = 0
    while i < len(parameters):
        correctAnswer += parameters[i]
        if i + 1 < len(parameters):
            correctAnswer += ", "
        else:
            correctAnswer += braces[1][1]
            break
        i += 1

    if provideCorrectAnswer:
        return correctAnswer

    else: # lets make some wrong answers!

        # pick a set of braces (might be right, might be wrong)
        whichBraces = random.choice([0,1,1,1,1,2]) # 1 is the correct set, so weight that more heavily

        # if the wrong answer forgets the parameters, we can 
        # immediately return a wrong answer (using a random set of braces)
        randomNum = random.randrange(0,6) #increase the upper range to make this happen less often
        forget_parameters = randomNum == 0
        if forget_parameters:
            answer = braces[whichBraces][0] + " " + braces[whichBraces][1]
            return answer

        # otherwise, construct some other wrong answer
        else:

            # maybe flip the parameters with the return variables
            randomNum = random.randrange(0,6) #increase the upper range to make this happen less often
            flipVariables = randomNum == 0 # flip if you got a zero

            # which variables are we using, return variables or parameters?
            if flipVariables:
                variable_set = return_variables
            else:
                variable_set = parameters

            # maybe shuffle the order of the variables
            randomNum = random.randrange(0,3) #increase the upper range to make this happen less often
            mix_it_up = randomNum == 0 # mix it up if you got a zero
            if mix_it_up:
                random.shuffle(variable_set)


            answer = braces[whichBraces][0]
            i = 0
            while i < len(variable_set):
                answer += variable_set[i]
                if i + 1 < len(variable_set):
                    answer += ", "
                else:
                    answer += braces[whichBraces][1]
                    break
                i += 1
            
            # return the constructed wrong answer!
            return answer


def make_arguments(arguments,parameters,provideCorrectAnswer):

    arguments = copy.deepcopy(arguments)
    parameters = copy.deepcopy(parameters)
  
    # WAYS TO MESS THIS UP
    # using the wrong brackets/braces
    # flipping the arguments with the parameters
    # forgetting the arguments
    # mixing up the order of the arguments

    # here are all the sets of braces we can use
    braces = [
        ["[","]"],
        ["(",")"],
        ["{","}"]
        ]

    # construct the correct answer
    correctAnswer = braces[1][0]
    i = 0
    while i < len(arguments):
        correctAnswer += arguments[i]
        if i + 1 < len(arguments):
            correctAnswer += ", "
        else:
            break
        i += 1
    correctAnswer += braces[1][1]

    if provideCorrectAnswer:
        return correctAnswer

    else: # lets make some wrong answers!

        # pick a set of braces (might be right, might be wrong)
        whichBraces = random.choice([0,1,1,1,1,2]) # 1 is the correct set, so weight that more heavily

        # if the wrong answer forgets the arguments, we can 
        # immediately return a wrong answer (using a random set of braces)
        randomNum = random.randrange(0,6) #increase the upper range to make this happen less often
        forget_arguments = randomNum == 0
        if forget_arguments:
            answer = braces[whichBraces][0] + braces[whichBraces][1]
            return answer

        # otherwise, construct some other wrong answer
        else:

            # maybe flip the arguments with the parameters
            randomNum = random.randrange(0,6) #increase the upper range to make this happen less often
            flipVariables = randomNum == 0 # flip if you got a zero

            # which variables are we using, parameters or arguments?
            if flipVariables:
                variable_set = parameters
            else:
                variable_set = arguments

            # maybe shuffle the order of the variables
            randomNum = random.randrange(0,3) #increase the upper range to make this happen less often
            mix_it_up = randomNum == 0 # mix it up if you got a zero
            if mix_it_up:
                random.shuffle(variable_set)


            answer = braces[whichBraces][0]
            i = 0
            while i < len(variable_set):
                answer += variable_set[i]
                if i + 1 < len(variable_set):
                    answer += ", "
                else:
                    break
                i += 1
            answer += braces[whichBraces][1]
            
            # return the constructed wrong answer!
            return answer


def func_header_answers(info,num_answers):
  

    # make empty answers list
    answers = []

    correct = "function "
    correct += make_return_variables(info["return_variables"],info["parameters"],True)
    correct += " = " + info["function_name"]
    correct += make_parameters(info["return_variables"],info["parameters"],True)

    answers.append({'tag': 'true', 'ans': correct})

    
    
    # ways to mess up a function header:
    # forgetting the word "function"
    # flipping the function name with the word "function"
    # forgetting the equal sign

    # construct wrong answers
    while len(answers) < num_answers:

        validWrongAnswer = False
        while validWrongAnswer == False:

            # pick some random wrongness
            randomNum = random.randrange(0,6) #increase the upper range to make this happen less often
            forgotFunctionWord = randomNum == 0

            randomNum = random.randrange(0,6) #increase the upper range to make this happen less often
            forgotEqualSign = randomNum == 0

            randomNum = random.randrange(0,6) #increase the upper range to make this happen less often
            flipFunctionAndName = randomNum == 0

            # start constructing the answer
            if forgotFunctionWord:
                incorrect = ""
            else:
                if flipFunctionAndName:
                    incorrect = info["function_name"] + " "
                else:
                    incorrect = "function" + " "

            incorrect += make_return_variables(info["return_variables"],info["parameters"],False)

            if forgotEqualSign:
                incorrect += " "
            else: 
                incorrect += " = " 
            if flipFunctionAndName:
                incorrect += "function"
            else:
                incorrect += info["function_name"]

            incorrect += make_parameters(info["return_variables"],info["parameters"],False)

            # if it does NOT match any existing answers, then you have a valid wrong answer
            validWrongAnswer = True
            i = 0
            while i < len(answers):
                if incorrect == answers[i]["ans"]:
                    validWrongAnswer = False
                    break
                i += 1


        answers.append({'tag': 'false', 'ans': incorrect})

    return answers


def func_call_answers(info,num_answers):

# info needs to have at least this information:
# info = {
#   "function_name": "name", 
#   "parameters": ["param","param", etc.],
#   "return_variables": ["var","var", etc.],
#   "arguments": ["var","var", etc.], 
#   "assignments": ["var","var", etc.],
#   "distractor_functions": ["name", "name", etc.],
#   "distractor_variables":[
#     "var","var", etc.
#   ]
# }  



    # make empty answers list
    answers = []

    correct = ""
    if (not len(info["assignments"]) == 0):
        correct += make_assigned_variables(info["assignments"],info["parameters"],True)
        correct += " = "
    correct += info["function_name"]
    correct += make_parameters(info["arguments"],info["arguments"],True)
    correct += ";"

    answers.append({'tag': 'true', 'ans': correct})


    # ways to mess up calling a function:
    # including the word "function"
    # forgot equal sign
    # flipping the arguments with the assignment variables
    # using the parameters instead of the arguments
    # MAYBE FOR THE FUTURE: using the return variables instead of the assignment variables (this might be harder for our students to catch than we can catch)
    # use the wrong function (for common MATLAB built-in functions like max or sum)

    # construct wrong answers
    while len(answers) < num_answers:

        validWrongAnswer = False
        while validWrongAnswer == False:

            # pick some random wrongness
            randomNum = random.randrange(0,6) #increase the upper range to make this happen less often
            includeFunctionWord = randomNum == 0

            randomNum = random.randrange(0,6) #increase the upper range to make this happen less often
            forgotEqualSign = randomNum == 0

            randomNum = random.randrange(0,6) #increase the upper range to make this happen less often
            flipArgumentsAndReturnVariables = randomNum == 0

            randomNum = random.randrange(0,4) #increase the upper range to make this happen less often
            usedWrongName = randomNum == 0

            # if there are distractor functions available, maybe use one
            if usedWrongName and ("distractor_functions" in info):
                if (len(info["distractor_functions"]) > 0):
                    thisFuncName = random.choice(info["distractor_functions"])
                else: 
                    thisFuncName = info["function_name"]
            else:
                thisFuncName = info["function_name"]


            # start constructing the answer
            incorrect = "" #start with an empty answer

            # if the function doesn't have any assigned variables, skip that step
            if (not len(info["assignments"]) == 0):

                if not(forgotEqualSign):
                    if flipArgumentsAndReturnVariables:
                        incorrect += make_assigned_variables(info["arguments"],info["arguments"],False)
                    else:
                        incorrect += make_assigned_variables(info["assignments"],info["assignments"],False)
                    if incorrect != "":
                        incorrect += " = "

            if includeFunctionWord:
                incorrect += "function "

            incorrect += thisFuncName

            if flipArgumentsAndReturnVariables: #also covers using parameters instead
                incorrect += make_arguments(info["assignments"],info["parameters"],False)
            else: 
                incorrect += make_arguments(info["arguments"],info["parameters"],False)

            incorrect += ";"

            # if it does NOT match any existing answers, then you have a valid wrong answer
            validWrongAnswer = True
            i = 0
            while i < len(answers):
                if incorrect == answers[i]["ans"]:
                    validWrongAnswer = False
                    break
                i += 1



        answers.append({'tag': 'false', 'ans': incorrect})

    return answers


def buggy_func_call_answers(info):
    
    # the info variable needs to have at least this information:
    # {
    #     "function_name": functionName,
    #     "parameters": [list of parameters],
    #     "return_variables": [list of return_variables],
    #     "arguments": [list of arguments],
    # }



    # Construct wrong answers
    wrong_answers = []

    # Ways to mess up calling a function:

    # 1. including the word "function"
    wrong_answer = ""
    wrong_answer += make_return_variables(info["return_variables"],info["return_variables"],True)
    wrong_answer += " = "
    wrong_answer += "function "
    wrong_answer += info["function_name"]
    wrong_answer += make_arguments(info["arguments"],info["arguments"],True)
    wrong_answer += ";"

    answer = {
        "ans": wrong_answer,
        "bug": "included the word \"function\" when calling the function",
        "fix": "remove the word \"function\"; you just have to use the name of the function"
    }
    wrong_answers.append(answer)


    # 2. using the wrong brackets/braces
    wrong_answer = ""
    return_vars = make_return_variables(info["return_variables"],info["return_variables"],True)
    return_vars = return_vars.replace("[","(")
    return_vars = return_vars.replace("]",")")
    wrong_answer += return_vars
    wrong_answer += " = "
    wrong_answer += info["function_name"]
    args = make_arguments(info["arguments"],info["parameters"],True)
    args = args.replace("(","[")
    args = args.replace(")","]")
    wrong_answer += args
    wrong_answer += ";"

    answer = {
        "ans": wrong_answer,
        "bug": "mixed up which brackets/braces/parentheses go where",
        "fix": "use [] for the return variable(s) and () for the arguments"
    }
    wrong_answers.append(answer)


    # 3. getting the order of the arguments wrong (ONLY IF MORE THAN ONE PARAMETER!)

    # make sure only the arguments are shuffled
    shuffled_args = copy.deepcopy(info["arguments"]) #start with them in order
    argsInOrder = True
    while (argsInOrder):
        random.shuffle(shuffled_args)
        i = 0
        while i < len(info["arguments"]):
            if (shuffled_args[i] != info["arguments"][i]):
                argsInOrder = False
                break
            i += 1

    # now, make the answer
    wrong_answer = ""
    return_vars = make_return_variables(info["return_variables"],info["return_variables"],True)
    wrong_answer += return_vars
    wrong_answer += " = "
    wrong_answer += info["function_name"]
    args = make_arguments(shuffled_args,shuffled_args,True)
    wrong_answer += args
    wrong_answer += ";"

    answer = {
        "ans": wrong_answer,
        "bug": "mixed up the order of the arguments",
        "fix": "double check that they are passing the correct arguments to the correct parameters"
    }
    wrong_answers.append(answer)


    # 4. flipping the arguments with the return variables
    wrong_answer = ""
    wrong_answer += make_return_variables(info["arguments"],info["arguments"],True)
    wrong_answer += " = "
    wrong_answer += info["function_name"]
    wrong_answer += make_arguments(info["return_variables"],info["return_variables"],True)
    wrong_answer += ";"

    answer = {
        "ans": wrong_answer,
        "bug": "mixed up the arguments with the return variables",
        "fix": "switch the arguments with the return variables in their statement"
    }
    wrong_answers.append(answer)


    # 5. forgetting the equal sign
    wrong_answer = ""
    wrong_answer += make_return_variables(info["return_variables"],info["return_variables"],True)
    wrong_answer += " "
    wrong_answer += info["function_name"]
    wrong_answer += make_arguments(info["arguments"],info["arguments"],True)
    wrong_answer += ";"

    answer = {
        "ans": wrong_answer,
        "bug": "forgotten the equal sign to store the return value(s)",
        "fix": "insert an equal sign between the return variables and the function name"
    }
    wrong_answers.append(answer)



    # 6. used the function header

    wrong_answer = ""
    wrong_answer += "function "
    wrong_answer += make_return_variables(info["return_variables"],info["return_variables"],True)
    wrong_answer += " = "
    wrong_answer += info["function_name"]
    wrong_answer += make_arguments(info["parameters"],info["parameters"],True)
    wrong_answer += ";"

    answer = {
        "ans": wrong_answer,
        "bug": "used the function header instead of calling the function",
        "fix": "review how to call a function (given the function header)"
    }
    wrong_answers.append(answer)




    # 7. forgetting the return variable

    wrong_answer = ""
    wrong_answer += info["function_name"]
    wrong_answer += make_arguments(info["arguments"],info["arguments"],True)
    wrong_answer += ";"

    answer = {
        "ans": wrong_answer,
        "bug": "forgotten to capture the return variable(s), but they correctly called the function!",
        "fix": "add the return variable(s) to the left side of an equal sign (the assignment operator)"
    }
    wrong_answers.append(answer)



    # 8. forgetting the return variable AND using the word "function"
    # NB: Let's not do this one for now since it has more than one thing wrong

    # wrong_answer = ""
    # wrong_answer += "function "
    # wrong_answer += info["function_name"]
    # wrong_answer += make_arguments(info["arguments"],info["arguments"],True)
    # wrong_answer += ";"

    # answer = {
    #     "ans": wrong_answer,
    #     "bug": "forgotten to capture the return variable(s) AND they have included the word \"function\"",
    #     "fix": "add the return variable(s)s and remove the word \"function\""
    # }
    # wrong_answers.append(answer)



    # 9. using the wrong variables (just in general) 

    # make some wrong variables
    prefixes = ["new_","old_","temp_","test_","TEMP_","TEST_","NEW_","OLD_"]
    suffixes = ["_new","_old","_1","_2","_3","_v1","_v2","_v3","_temp","_test"]

    parameters = copy.deepcopy(info["parameters"])
    return_variables = copy.deepcopy(info["return_variables"])
    arguments = copy.deepcopy(info["arguments"])

    i = 0
    while i < len(return_variables):
        if (random.getrandbits(2)):
            return_variables[i] = random.choice(prefixes) + return_variables[i]
        else:
            return_variables[i] = return_variables[i] + random.choice(suffixes)
        i += 1
    i = 0
    while i < len(arguments):
        if (random.getrandbits(2)):
            arguments[i] = random.choice(prefixes) + arguments[i]
        else:
            if (random.getrandbits(2)):
                arguments[i] = arguments[i] + random.choice(suffixes)
            else:
                arguments[i] = parameters[i] + random.choice(suffixes)
        i += 1

    wrong_answer = ""
    wrong_answer += make_return_variables(return_variables,return_variables,True)
    wrong_answer += " = "
    wrong_answer += info["function_name"]
    wrong_answer += make_arguments(arguments,arguments,True)
    wrong_answer += ";"

    answer = {
        "ans": wrong_answer,
        "bug": "used variables that either do not exist or were not intended to be used in this function call",
        "fix": "double-check that the correct variables are being used in this function call"
    }
    wrong_answers.append(answer)


    return wrong_answers


def clear_workspace(provideCorrectAnswer):
  
    # WAYS TO MESS THIS UP
    # using the wrong keyword

    # construct the correct answer
    correctAnswer = "clear"

    if provideCorrectAnswer:
        return correctAnswer

    else: # lets make some wrong answers!

        # pick a wrong keyword
        answer = random.choice(["save","delete","reload","close workspace","remove","empty"]) 

        # return the wrong answer!
        return answer


def close_figures(provideCorrectAnswer):
  
    # WAYS TO MESS THIS UP
    # using the wrong keyword
    # closing only one figure and not all of them

    # construct the correct answer
    correctAnswer = "close all"

    if provideCorrectAnswer:
        return correctAnswer

    else: # lets make some wrong answers!

        # pick a wrong keyword
        answer = random.choice(["clear figure","sweep","close","unload","free","void"]) 

        # add either a number or "all"
        randomNum = random.randrange(0,2) #increase the upper range to make this happen less often
        forgot_all = randomNum == 0

        randomNum = random.randrange(0,6) #increase the upper range to make this happen less often
        added_number = randomNum == 0
        what_number = random.randrange(1,10) #increase the upper range to make this happen less often

        if forgot_all:
            answer += ""
        else:
            if added_number:
                answer += " " + str(what_number)
            else:
                answer += " all"

        # return the wrong answer!
        return answer


def clear_workspace_answers(num_answers):
  
    # make empty answers list
    answers = []

    correct = clear_workspace(True)

    answers.append({'tag': 'true', 'ans': correct})
    
    # construct wrong answers
    while len(answers) < num_answers:

        validWrongAnswer = False
        while validWrongAnswer == False:

            # start constructing the answer
            incorrect = clear_workspace(False)

            # if it does NOT match any existing answers, then you have a valid wrong answer
            validWrongAnswer = True
            i = 0
            while i < len(answers):
                if incorrect == answers[i]["ans"]:
                    validWrongAnswer = False
                    break
                i += 1

        answers.append({'tag': 'false', 'ans': incorrect})

    return answers


def close_figures_answers(num_answers):
  
    # make empty answers list
    answers = []

    correct = close_figures(True)

    answers.append({'tag': 'true', 'ans': correct})
    
    # construct wrong answers
    while len(answers) < num_answers:

        validWrongAnswer = False
        while validWrongAnswer == False:

            # start constructing the answer
            incorrect = close_figures(False)

            # if it does NOT match any existing answers, then you have a valid wrong answer
            validWrongAnswer = True
            i = 0
            while i < len(answers):
                if incorrect == answers[i]["ans"]:
                    validWrongAnswer = False
                    break
                i += 1

        answers.append({'tag': 'false', 'ans': incorrect})

    return answers


def load_image_answers(info,which_image,num_answers):

    # The form of the info variable is this:
    # [
    #     {
    #         "filename": "img1file.jpg",
    #         "variable:": "img1",
    #     },
    #     {
    #         "filename": "img2file.jpg",
    #         "variable:": "img2",
    #     },
    #     ...
    # ]
    # The which_image variable identifies which image we're trying to load

    # ways to mess up loading an image:
    # forgetting to save the information to a variable
    # using the wrong keyword
    # forgetting quotes for the filename
    # switching the filename with the variable name

    # make empty answers list
    answers = []

    # make correct answer
    filename = "'" + info[which_image]["filename"] + "'"
    arg = [filename]

    correct = info[which_image]["variable"]
    correct += " = "
    correct += "imread"
    correct += make_arguments(arg,arg,True)
    correct += ";"

    answers.append({'tag': 'true', 'ans': correct})
    

    # construct wrong answers
    while len(answers) < num_answers:

        validWrongAnswer = False
        while validWrongAnswer == False:

            # pick some random wrongness
            randomNum = random.randrange(0,6) #increase the upper range to make this happen less often
            forgotToStoreReturn = randomNum == 0

            randomNum = random.randrange(0,6) #increase the upper range to make this happen less often
            usedWrongKeyword = randomNum == 0

            randomNum = random.randrange(0,6) #increase the upper range to make this happen less often
            forgotQuotes = randomNum == 0

            randomNum = random.randrange(0,6) #increase the upper range to make this happen less often
            flippedVariables = randomNum == 0


            # start constructing the answer

            if forgotToStoreReturn:
                incorrect = ""
            else:
                if flippedVariables:
                    incorrect = info[which_image]["filename"] + " = "
                else:
                    incorrect = info[which_image]["variable"] + " = "

            if usedWrongKeyword:
                keyword = random.choice(["load","read","imshow","imload"])
                incorrect += keyword 
            else: 
                incorrect += "imread"

            if flippedVariables:
                filename = info[which_image]["variable"]
            else:
                filename = info[which_image]["filename"]

            if not(forgotQuotes):
                filename = "'" + filename + "'"

            arg = [filename]
            incorrect += make_arguments(arg,arg,False)
            # ^^ sending the same thing for arguments and parameters because we don't need to flip that again

            incorrect += ";"

            # if it does NOT match any existing answers, then you have a valid wrong answer
            validWrongAnswer = True
            i = 0
            while i < len(answers):
                if incorrect == answers[i]["ans"]:
                    validWrongAnswer = False
                    break
                i += 1

        answers.append({'tag': 'false', 'ans': incorrect})

    return answers


def save_image_answers(info,which_image,num_answers):


    # The form of the info variable is this:
    # [
    #     {
    #         "filename": "img1file.jpg",
    #         "variable:": "img1",
    #     },
    #     {
    #         "filename": "img2file.jpg",
    #         "variable:": "img2",
    #     },
    #     ...
    # ]
    # The which_image variable identifies which image we're trying to save
  
    # ways to mess up saving an image:
    # trying to save the information to a variable
    # using the wrong keyword
    # forgetting quotes for the filename
    # using the wrong image variable
    # using the wrong image filename

    numImages = len(info)

    # make empty answers list
    answers = []

    # make correct answer
    filename = "'" + info[which_image]["filename"] + "'"
    arg = [info[which_image]["variable"],filename]

    correct = ""
    correct += "imwrite"
    correct += make_arguments(arg,arg,True)
    correct += ";"

    answers.append({'tag': 'true', 'ans': correct})
    # imwrite(myHeatmap(rowLoc-zoomOffset:rowLoc+zoomOffset,colLoc-zoomOffset:colLoc+zoomOffset,:),'heatmap_local.png');

    # construct wrong answers
    while len(answers) < num_answers:

        validWrongAnswer = False
        while validWrongAnswer == False:

            # pick some random wrongness
            randomNum = random.randrange(0,4) #increase the upper range to make this happen less often
            savedAsVariable = randomNum == 0

            randomNum = random.randrange(0,2) #increase the upper range to make this happen less often
            usedWrongKeyword = randomNum == 0

            randomNum = random.randrange(0,2) #increase the upper range to make this happen less often
            forgotQuotes = randomNum == 0

            randomNum = random.randrange(0,3) #increase the upper range to make this happen less often
            usedWrongImgVariable = randomNum == 0

            randomNum = random.randrange(0,4) #increase the upper range to make this happen less often
            usedWrongImgFilename = randomNum == 0

            # start constructing the answer
            incorrect = ""

            if savedAsVariable:
                incorrect += info[which_image]["variable"] + " = "

            if usedWrongKeyword:
                keyword = random.choice(["save","write","imshow","imsave"])
                incorrect += keyword 
            else: 
                incorrect += "imwrite"

            if not(forgotQuotes):
                filename = "'" + filename + "'"

            # make a set of correct arguments and incorrect arguments (i.e. saving to the wrong file)
            filename = "'" + info[which_image]["filename"] + "'"
            correct_args = [info[which_image]["variable"],filename]

            # pick a different image to be the incorrect arguments
            i = random.randrange(0,len(info))
            while i != which_image:
                i = random.randrange(0,len(info))
            filename = "'" + info[i]["filename"] + "'"
            incorrect_args = [info[i]["variable"],filename]

            incorrect += make_arguments(correct_args,incorrect_args,False)

            incorrect += ";"

            # if it does NOT match any existing answers, then you have a valid wrong answer
            validWrongAnswer = True
            i = 0
            while i < len(answers):
                if incorrect == answers[i]["ans"]:
                    validWrongAnswer = False
                    break
                i += 1


        answers.append({'tag': 'false', 'ans': incorrect})

    return answers


def load_matfile_answers(info,which_file,num_answers):
  
    # The form of the info variable is this:
    # [
    #     {
    #         "filename": "filename1.mat",
    #         "variable": "var1",
    #     },
    #     {
    #         "filename": "filename2.mat",
    #         "variable": "var2",
    #     },
    #     ...
    # ]
    # The which_file variable identifies which file we're trying to load

    # ways to mess up loading an file:
    # saving the information to a variable (this creates a struct, which is incorrect!)
    # using the wrong keyword
    # forgetting quotes for the filename
    # switching the filename with the variables in the file

    # make empty answers list
    answers = []

    # make correct answer
    filename = "'" + info[which_file]["filename"] + "'"
    arg = [filename]

    correct = ""
    correct += "load"
    correct += make_arguments(arg,arg,True)
    correct += ";"

    answers.append({'tag': 'true', 'ans': correct})
    

    # construct wrong answers
    while len(answers) < num_answers:

        validWrongAnswer = False
        while validWrongAnswer == False:

            # pick some random wrongness
            randomNum = random.randrange(0,6) #increase the upper range to make this happen less often
            storedToAVariable = randomNum == 0

            randomNum = random.randrange(0,6) #increase the upper range to make this happen less often
            usedWrongKeyword = randomNum == 0

            randomNum = random.randrange(0,6) #increase the upper range to make this happen less often
            forgotQuotes = randomNum == 0

            randomNum = random.randrange(0,6) #increase the upper range to make this happen less often
            flippedVariables = randomNum == 0


            # start constructing the answer

            if storedToAVariable:
                if flippedVariables:
                    incorrect = info[which_file]["filename"] + " = "
                else:
                    incorrect = info[which_file]["variable"] + " = "
            else:
                incorrect = ""


            if usedWrongKeyword:
                keyword = random.choice(["imload","imread","input","read"])
                incorrect += keyword 
            else: 
                incorrect += "load"

            if flippedVariables:
                filename = info[which_file]["variable"]
            else:
                filename = info[which_file]["filename"]

            if not(forgotQuotes):
                filename = "'" + filename + "'"

            arg = [filename]
            incorrect += make_arguments(arg,arg,False)
            # ^^ sending the same thing for arguments and parameters because we don't need to flip that again

            incorrect += ";"

            # if it does NOT match any existing answers, then you have a valid wrong answer
            validWrongAnswer = True
            i = 0
            while i < len(answers):
                if incorrect == answers[i]["ans"]:
                    validWrongAnswer = False
                    break
                i += 1


        answers.append({'tag': 'false', 'ans': incorrect})

    return answers


def load_table_answers(info,which_file,num_answers):
  
    # The form of the info variable is this:
    # [
    #     {
    #         "filename": "filename",
    #         "variable:": "var1",
    #     },
    #     {
    #         "filename": "filename",
    #         "variable:": "var2",
    #     },
    #     ...
    # ]
    # The which_file variable identifies which file we're trying to load

    # ways to mess up loading an file:
    # forgetting to save the information to a variable 
    # using the wrong keyword
    # forgetting quotes for the filename
    # switching the filename with the variables in the file

    # make empty answers list
    answers = []

    # make correct answer
    filename = "'" + info[which_file]["filename"] + "'"
    arg = [filename]

    correct = ""
    correct += info[which_file]["variable"]
    correct += " = "
    correct += "readtable"
    correct += make_arguments(arg,arg,True)
    correct += ";"

    answers.append({'tag': 'true', 'ans': correct})
    

    # construct wrong answers
    while len(answers) < num_answers:

        validWrongAnswer = False
        while validWrongAnswer == False:

            # pick some random wrongness
            randomNum = random.randrange(0,6) #increase the upper range to make this happen less often
            forgotToStore = randomNum == 0

            randomNum = random.randrange(0,3) #increase the upper range to make this happen less often
            usedWrongKeyword = randomNum == 0

            randomNum = random.randrange(0,6) #increase the upper range to make this happen less often
            forgotQuotes = randomNum == 0

            randomNum = random.randrange(0,6) #increase the upper range to make this happen less often
            flippedVariables = randomNum == 0


            # start constructing the answer

            if forgotToStore:
                incorrect = ""
            else:
                if flippedVariables:
                    incorrect = info[which_file]["filename"] + " = "
                else:
                    incorrect = info[which_file]["variable"] + " = "


            if usedWrongKeyword:
                keyword = random.choice(["load","read","input","loadtable"])
                incorrect += keyword 
            else: 
                incorrect += "readtable"

            if flippedVariables:
                filename = info[which_file]["variable"]
            else:
                filename = info[which_file]["filename"]

            if not(forgotQuotes):
                filename = "'" + filename + "'"

            arg = [filename]
            incorrect += make_arguments(arg,arg,False)
            # ^^ sending the same thing for arguments and parameters because we don't need to flip that again

            incorrect += ";"

            # if it does NOT match any existing answers, then you have a valid wrong answer
            validWrongAnswer = check_duplicate_answers(incorrect,answers)
            


        answers.append({'tag': 'false', 'ans': incorrect})

    return answers


def write_table_answers(info,num_answers):
  
    # The form of the info variable is this:
    # 
    #     {
    #         "filename": "filename",
    #         "variable:": "var1",
    #     }
    # 
    # The which_file variable identifies which file we're trying to load

    # ways to mess up writing a table:
    # saving to a variable 
    # using the wrong keyword
    # forgetting quotes for the filename
    # switching the filename with the variable in the file

    # make empty answers list
    answers = []

    # make correct answer
    filename = "'" + info["filename"] + "'"
    arg = [info["variable"],filename]

    correct = ""
    correct += "writetable"
    correct += make_arguments(arg, arg,True)
    correct += ";"

    answers.append({'tag': 'true', 'ans': correct})
    

    # construct wrong answers
    while len(answers) < num_answers:

        validWrongAnswer = False
        while validWrongAnswer == False:

            # pick some random wrongness
            randomNum = random.randrange(0,6) #increase the upper range to make this happen less often
            storedVariable = randomNum == 0

            randomNum = random.randrange(0,3) #increase the upper range to make this happen less often
            usedWrongKeyword = randomNum == 0

            randomNum = random.randrange(0,6) #increase the upper range to make this happen less often
            forgotQuotes = randomNum == 0

            randomNum = random.randrange(0,6) #increase the upper range to make this happen less often
            flippedVariables = randomNum == 0


            # start constructing the answer

            if storedVariable:
                if flippedVariables:
                    incorrect = info["filename"] + " = "
                else:
                    incorrect = info["variable"] + " = "
            else:
                incorrect = ""
                


            if usedWrongKeyword:
                keyword = random.choice(["write","save","print","savetable"])
                incorrect += keyword 
            else: 
                incorrect += "writetable"

            if flippedVariables:
                filename = info["variable"]
            else:
                filename = info["filename"]

            if not(forgotQuotes):
                filename = "'" + filename + "'"

            arg = [info["variable"],filename]
            incorrect += make_arguments(arg,arg,False)
            # ^^ sending the same thing for arguments and parameters because we don't need to flip that again

            incorrect += ";"

            # if it does NOT match any existing answers, then you have a valid wrong answer
            validWrongAnswer = check_duplicate_answers(incorrect,answers)
            


        answers.append({'tag': 'false', 'ans': incorrect})

    return answers


def make_vector_with_values(values,provideCorrectAnswer):
  
    # ways to mess up making a vector:
    # mixing up the order of the values
    # using the wrong braces/brackets

    # here are all the sets of braces we can use
    braces = [
        ["[","]"],
        ["(",")"],
        ["{","}"]
        ]


    values = copy.deepcopy(values)

    # construct the correct answer
    correctAnswer = braces[0][0]
    i = 0
    while i < len(values):
        correctAnswer += values[i]
        if i + 1 < len(values):
            correctAnswer += ", "
        else:
            correctAnswer += braces[0][1]
            break
        i += 1


    if provideCorrectAnswer:
        return correctAnswer

    else: # lets make some wrong answers!

        # pick a set of braces (might be right, might be wrong)
        whichBraces = random.choice([0,0,1,2]) # 0 is the correct set, so weight that more heavily

        # maybe shuffle the order of the values
        randomNum = random.randrange(0,3) #increase the upper range to make this happen less often
        mix_it_up = randomNum == 0 # mix it up if you got a zero
        if mix_it_up:
            random.shuffle(values)

        # construct wrong answer
        answer = braces[whichBraces][0]
        i = 0
        while i < len(values):
            answer += values[i]
            if i + 1 < len(values):
                answer += ", "
            else:
                answer += braces[whichBraces][1]
                break
            i += 1

        # return the constructed wrong answer!
        return answer



def make_vector_range_notation(info,provideCorrectAnswer):
  
  # needed fields in the info variable:
    # {
    #     "start_range": "number as a string",
    #     "end_range": "number as a string",
    #     "step_size": "number as a string",
    # }


    # common ways to mess up making a vector with range notation:
    #    1. wrong order of the values
    #    2. using "" marks around the values
    #    3. messing up syntax (primarily : vs. ,)



    # construct the correct answer
    correctAnswer = info["start_range"] + " : " + info["step_size"] + " : " + info["end_range"]


    if provideCorrectAnswer:
        return correctAnswer

    else: # lets make a wrong answer!

        # maybe shuffle the order of the values
        randomNum = random.randrange(0,3) #increase the upper range to make this happen less often
        mix_it_up = randomNum == 0 # mix it up if you got a zero
        
        # maybe use quotes 
        randomNum = random.randrange(0,3) #increase the upper range to make this happen less often
        usedQuotes = randomNum == 0 # do this if you got a zero
        
        # maybe use commas instead of :
        randomNum = random.randrange(0,3) #increase the upper range to make this happen less often
        usedCommas = randomNum == 0 # do this if you got a zero

        # implement some of the randomness
        if usedQuotes:
            values = [
                copy.copy("'" + info["start_range"] + "'"),
                copy.copy("'" + info["step_size"] + "'"),
                copy.copy("'" + info["end_range"] + "'")
            ]
        else:
            values = [
                copy.copy(info["start_range"]),
                copy.copy(info["step_size"]),
                copy.copy(info["end_range"])
            ]
        if mix_it_up:
            random.shuffle(values)


        # construct wrong answer
        if usedCommas:
            answer = "[" + values[0] + " , " + values[1] + " , " + values[2] + "]"
        else:
            answer = values[0] + " : " + values[1] + " : " + values[2]



        # return the constructed wrong answer!
        return answer


def store_vector(info,type,provideCorrectAnswer):
  
    # format of the info variable is: 
    # {
    #   "name": "var",
    #   "values": ["val1","val2",...],
    #   "start_range": "start_val",
    #   "end_range": "end_val",
    #   "step_size": "step_val",
    #   "num_elements": ""
    # }
    # the fields that you don't need can be blank or missing

    # options for the type are: " 
    # "by_value"
    # "range_notation"
    # "linspace"


    # make empty answers list
    answers = []

    # make correct answer
    correct = ""
    correct += info["name"]
    correct += " = "

    if (type == "by_value"):
        correct += make_vector_with_values(info["values"],True)
    if (type == "range_notation"):
        correct += make_vector_range_notation(info,True)
    if (type == "linspace"):
        correct += make_vector_with_values(info["values"],True)

    correct += ";"




    if provideCorrectAnswer:
        return correct

    else: # lets make a wrong answer!

        # start constructing the answer
        incorrect = "" #start with an empty answer

        incorrect += info["name"]
        incorrect += " = "

        if (type == "by_value"):
            incorrect += make_vector_with_values(info["values"],False)
        if (type == "range_notation"):
            incorrect += make_vector_range_notation(info,False)
        if (type == "linspace"):
            incorrect += make_vector_with_values(info["values"],False)

        incorrect += ";"

        return incorrect


def store_vector_answers(info,type,num_answers):
  
    # format of the info variable is: 
    # {
    #   "name": "var",
    #   "values": ["val1","val2",...],
    #   "start_range": "start_val",
    #   "end_range": "end_val",
    #   "step_size": "step_val",
    #   "num_elements": ""
    # }
    # the fields that you don't need can be blank or missing

    # options for the type are: " 
    # "by_value"
    # "range_notation"
    # "linspace"


    # make empty answers list
    answers = []

    # make correct answer
    correct = store_vector(info,type,True)
    answers.append({'tag': 'true', 'ans': correct})


    # construct wrong answers
    while len(answers) < num_answers:

    # ways to mess up creating a vector:
    # other errors handled by the "store vector" functions

        validWrongAnswer = False
        while validWrongAnswer == False:


            # start constructing the answer
            incorrect = store_vector(info,type,False)

            # if it does NOT match any existing answers, then you have a valid wrong answer
            validWrongAnswer = check_duplicate_answers(incorrect,answers)


        answers.append({'tag': 'false', 'ans': incorrect})

    return answers


def use_range_notation(info,num_answers):
  
    # format of the info variable is: 
    # {
    #   "assignment": "var"
    #   "name": "var",
    #   "start_range": "start_val",
    #   "end_range": "end_val",
    #   "step_size": "step_val", <- needs to be a string
    #   "distractor_variables": ["var", "var", etc.]
    # }

    # make empty answers list
    answers = []

    # make correct answer
    correct = info["assignment"] + " = " + info["start_range"] + ":" + info["step_size"] + ":" + info["end_range"] + ";"
    answers.append({'tag': 'true', 'ans': correct})

    # construct wrong answers
    while len(answers) < num_answers:

    # ways to mess up range notation:
    # use semi-colons instead of colons
    # get order of variables wrong (start_range, step_size, end_range)
    # forget to assign to variable
    # assign to wrong variable

        validWrongAnswer = False
        while validWrongAnswer == False:

            # maybe forget to assign
            randomNum = random.randrange(0,12) #increase the upper range to make this happen less often
            forgetToAssign = randomNum == 0

            # maybe assign to wrong variable
            randomNum = random.randrange(0,10)
            wrongAssignment = randomNum == 0

            if forgetToAssign:
                incorrect = ""
            else:
                if wrongAssignment:
                    distractor = info["distractor_variables"][random.randrange(0,len(info["distractor_variables"]))]
                    incorrect = distractor + " = "
                else:
                    incorrect = info["assignment"] + " = "

            # maybe use semi-colon instead of colon
            randomNum = random.randrange(0,10)
            useSemicolon = randomNum == 0

            # maybe get ordering wrong
            randomNum = random.randrange(0,6) #increase the upper range to make this happen less often
            wrongOrdering = randomNum == 0

            if wrongOrdering:
                ordering = np.random.permutation(["start_range","step_size","end_range"])
                incorrect += info[ordering[0]]
                if useSemicolon:
                    incorrect += ";"
                else:
                    incorrect += ":"

                incorrect += info[ordering[1]]
                if useSemicolon:
                    incorrect += ";"
                else:
                    incorrect += ":"

                incorrect += info[ordering[2]]

            else:
                incorrect += info["start_range"]
                if useSemicolon:
                    incorrect += ";"
                else:
                    incorrect += ":"

                incorrect += info["step_size"]
                if useSemicolon:
                    incorrect += ";"
                else:
                    incorrect += ":"

                incorrect += info["end_range"]

            incorrect += ";"

            # if it does NOT match any existing answers or the correct answer, then you have a valid wrong answer
            validWrongAnswer = check_duplicate_answers(incorrect,answers)

        answers.append({'tag': 'false', 'ans': incorrect})

    return answers


def make_crop_range_with_offsets_answers(info,num_answers): 

    # possible wrong operators to use
    operators = [
        [".*",".*"],
        ["./","./"],
        [">","<"],
        ["<",">"],
        ["==","=="],
        ["<=",">="],
    ]
    random.shuffle(operators)
    
    # make empty answers list
    answers = []

    # make correct answer
    correctInfo =  {
      "name": info["internal_variables"][0], # rows
      "values": [info["parameters"][1] + " - " + info["parameters"][3], info["parameters"][1] + " + " + info["parameters"][3]],
    }
    correctRows = store_vector(correctInfo,"by_value",True)
    correctInfo =  {
      "name": info["internal_variables"][1], # columns
      "values": [info["parameters"][2] + " - " + info["parameters"][3], info["parameters"][2] + " + " + info["parameters"][3]],
    }
    correctCols = store_vector(correctInfo,"by_value",True)

    correct = correctRows + "\n    " + correctCols 
    answers.append({'tag': 'true', 'ans': correct})


    # ways to mess up creating the range of rows using an offset:
    # use the wrong parameters in the wrong spot (mix up rows and columns)
    # use range notation instead of just two values
    # math error in dealing with the offset
    # other errors handled by the "make vector" functions

    # construct wrong answers
    while len(answers) < num_answers:

        validWrongAnswer = False
        while validWrongAnswer == False:

            randomNum = random.randrange(0,6) #increase the upper range to make this happen less often
            usedWrongParameters = randomNum == 0

            randomNum = random.randrange(0,6) #increase the upper range to make this happen less often
            usedRangeNotation = randomNum == 0

            randomNum = random.randrange(0,6) #increase the upper range to make this happen less often
            hadAMathError = randomNum == 0

            # start constructing the answer
            incorrect = "" #start with an empty answer


            if usedWrongParameters:
                startValRow = info["parameters"][2] 
                startValCol = info["parameters"][1] 
            else: 
                startValRow = info["parameters"][1]
                startValCol = info["parameters"][2]

            if hadAMathError:
                valuesRow = [startValRow + " " + operators[0][0] + " " + info["parameters"][3], startValRow + " " + operators[0][1] + " " + info["parameters"][3]]
                valuesCol = [startValCol + " " + operators[0][0] + " " + info["parameters"][3], startValCol + " " + operators[0][1] + " " + info["parameters"][3]]
            else: 
                valuesRow = [startValRow + " + " + info["parameters"][3], startValRow + " - " + info["parameters"][3]]
                valuesCol = [startValCol + " + " + info["parameters"][3], startValCol + " - " + info["parameters"][3]]

            vectorInfoRow =  {
                "name": info["internal_variables"][0], # rows
                "values": valuesRow,

                # set some values to use if they messed up and used range notation
                "start_range": valuesRow[0],
                "end_range": valuesRow[1],
                "step_size": "1"
            }
            vectorInfoCol =  {
                "name": info["internal_variables"][1], # columns
                "values": valuesCol,
                # set some values to use if they messed up and used range notation
                "start_range": valuesCol[0],
                "end_range": valuesCol[1],
                "step_size": "1"
            }

            if usedRangeNotation:
                incorrectRow = store_vector(vectorInfoRow,"range_notation",False) 
                incorrectCol = store_vector(vectorInfoCol,"range_notation",False) 
            else:
                incorrectRow = store_vector(vectorInfoRow,"by_value",False) 
                incorrectCol = store_vector(vectorInfoCol,"by_value",False) 

            incorrect = incorrectRow + "\n    " + incorrectCol

            # if it does NOT match any existing answers, then you have a valid wrong answer
            validWrongAnswer = True
            i = 0
            while i < len(answers):
                if incorrect == answers[i]["ans"]:
                    validWrongAnswer = False
                    break
                i += 1

        answers.append({'tag': 'false', 'ans': incorrect})

    return answers


def select_submatrix_image(info,provideCorrectAnswer):
  
    # format of the info variable is: 
    # {
    #   "name": "img",
    #   "row_range": ["val1","val2"],
    #   "col_range": ["val1","val2"],
    # }

    # ways to mess up selecting a sub image (aka cropping)
    # using the wrong brackets/braces
    # mixing up the rows and the columns or flipping the order of the rows/columns values
    # forgetting to include the third layer
    # using commas instead of : 

    # make a copy of info so you can shuffle later without it fucking up the whole problem
    info = copy.deepcopy(info)

    # here are all the sets of braces we can use
    braces = [
        ["[","]"],
        ["(",")"],
        ["{","}"]
        ]

    # construct the correct answer
    correctAnswer = ""
    correctAnswer += info["name"]
    correctAnswer += braces[1][0]
    correctAnswer += info["row_range"][0]
    correctAnswer += ":"
    correctAnswer += info["row_range"][1]
    correctAnswer += ","
    correctAnswer += " "
    correctAnswer += info["col_range"][0]
    correctAnswer += ":"
    correctAnswer += info["col_range"][1]
    correctAnswer += ","
    correctAnswer += " "
    correctAnswer += ":"
    correctAnswer += braces[1][1]


    if provideCorrectAnswer:
        return correctAnswer

    else: # lets make some wrong answers!

        # pick a set of braces (might be right, might be wrong)
        whichBraces = random.choice([0,1,1,2]) # 1 is the correct set, so weight that more heavily

        # maybe shuffle the order of the values
        randomNum = random.randrange(0,3) #increase the upper range to make this happen less often
        mix_order = randomNum == 0 # mix it up if you got a zero
        randomNum = random.randrange(0,3) #increase the upper range to make this happen less often
        flipRowsAndColumns = randomNum == 0 # mix it up if you got a zero

        # maybe forget the third layer
        randomNum = random.randrange(0,3) #increase the upper range to make this happen less often
        forgotThirdLayer = randomNum == 0 # forget third layer if you got a zero

        # maybe use commas instead of : to select a range
        randomNum = random.randrange(0,3) #increase the upper range to make this happen less often
        usedCommas = randomNum == 0 # forget third layer if you got a zero



        # mix things up if you need to
        if mix_order:
            random.shuffle(info["row_range"])
            random.shuffle(info["col_range"])
        if flipRowsAndColumns:
            temp = copy.deepcopy(info["row_range"])
            info["row_range"] = copy.deepcopy(info["col_range"])
            info["col_range"] = temp


        # construct wrong answer
        answer = braces[whichBraces][0]


        answer = ""
        answer += info["name"]
        answer += braces[whichBraces][0]
        answer += info["row_range"][0]
        if usedCommas:
            answer += ","
        else:
            answer += ":"
        answer += info["row_range"][1]
        answer += ","
        answer += " "
        answer += info["col_range"][0]
        if usedCommas:
            answer += ","
        else:
            answer += ":"
        answer += info["col_range"][1]
        if not(forgotThirdLayer):
            answer += ","
            answer += " "
            answer += ":"
        answer += braces[whichBraces][1]

        # return the constructed wrong answer!
        return answer


def crop_image_answers(info,num_answers): 

    # here are all the sets of braces we can use
    braces = [
        ["[","]"],
        ["(",")"],
        ["{","}"]
    ]


    # make empty answers list
    answers = []

    # make correct answer
    correctInfo =  {
        "name": info["arguments"][0],
        "row_range": [info["internal_variables"][0] + "(1)" , info["internal_variables"][0]  + "(2)"],
        "col_range": [info["internal_variables"][1] + "(1)", info["internal_variables"][1]+ "(2)" ],
    }


    # make correct answer
    correct = ""
    correct += correctInfo["name"]
    correct += " = "
    correct += select_submatrix_image(correctInfo,True)
    correct += ";"

    answers.append({'tag': 'true', 'ans': correct})


    # ways to mess up cropping an image:
    # forget to store the cropped image in a variable
    # zero indexed instead of one indexed
    # used wrong braces
    # other errors handled by the "select_submatrix_image" function

    # construct wrong answers
    while len(answers) < num_answers:

        validWrongAnswer = False
        while validWrongAnswer == False:

            # maybe forgot to store the cropped image
            randomNum = random.randrange(0,2) #increase the upper range to make this happen less often
            forgotToStore = randomNum == 0
           
            # pick a set of braces (might be right, might be wrong)
            whichBraces = random.choice([0,1,1,2]) # 1 is the correct set, so weight that more heavily

            # pick a starting index (might be right, might be wrong)
            whichIndexStart = random.choice([0,1,1]) # 1 is the correct starting index, so weight that more heavily

            vars = copy.deepcopy(info["internal_variables"])

            incorrectInfo =  {
                "name": copy.deepcopy(info["arguments"][0]),
                "row_range": [vars[0] + braces[whichBraces][0] + str(whichIndexStart) + braces[whichBraces][1], vars[0] + braces[whichBraces][0] + str(whichIndexStart+1) + braces[whichBraces][1]],
                "col_range": [vars[1] + braces[whichBraces][0] + str(whichIndexStart) + braces[whichBraces][1], vars[1] + braces[whichBraces][0] + str(whichIndexStart+1) + braces[whichBraces][1]],
            }


            # start constructing the answer
            incorrect = "" #start with an empty answer

            if not(forgotToStore):
                incorrect += incorrectInfo["name"]
                incorrect += " = "

            incorrect += select_submatrix_image(incorrectInfo,False)
            incorrect += ";"


            # if it does NOT match any existing answers, then you have a valid wrong answer
            validWrongAnswer = True
            i = 0
            while i < len(answers):
                if incorrect == answers[i]["ans"]:
                    validWrongAnswer = False
                    break
                i += 1

        answers.append({'tag': 'false', 'ans': incorrect})

    return answers


def pull_out_channels_answers(img,channel_vars,num_answers): 

    # here are all the sets of braces we can use
    braces = [
        ["[","]"],
        ["(",")"],
        ["{","}"]
    ]


    # make empty answers list
    answers = []

    # make correct answer
    correct = ""
    i = 0
    while i < len(channel_vars):
        correct += "    " + channel_vars[i] + " = " + img + "(:,:," + str(i+1) + ");"
        if i + 1 < len(channel_vars):
            correct += "\n" # add newline for next channel
        i += 1

    answers.append({'tag': 'true', 'ans': correct})


    # ways to mess up pulling out the channels:
        # forget to store the channels in variables
        # zero indexed instead of one indexed
        # used wrong braces
        # mix up which indices have the : to select all
        # mix up which variable goes on which side of the = sign
        # forget a channel

    # construct wrong answers
    while len(answers) < num_answers:

        validWrongAnswer = False
        while validWrongAnswer == False:

            # maybe forgot to store channels
            randomNum = random.randrange(0,4) #increase the upper range to make this happen less often
            forgotToStore = randomNum == 0
           
            # pick a set of braces (might be right, might be wrong)
            whichBraces = random.choice([0,1,1,1,2]) # 1 is the correct set, so weight that more heavily

            # pick a starting index (might be right, might be wrong)
            whichIndexStart = random.choice([0,1,1,1]) # 1 is the correct starting index, so weight that more heavily

            # pick a layer to pull out (might be right, might be wrong)
            whichIndexPull = random.choice([0,1,2,2,2,2]) # 2 is the correct layer (at least, in Python indexing), so weight that more heavily

            # maybe mixed up layers image variable
            randomNum = random.randrange(0,4) #increase the upper range to make this happen less often
            flippedImgAndChannels = randomNum == 0

            # maybe forgot a channel
            randomNum = random.randrange(0,10) #increase the upper range to make this happen less often
            forgotAChannel = randomNum == 0

            # maybe tried to do it in one line
            randomNum = random.randrange(0,10) #increase the upper range to make this happen less often
            triedOneLine = randomNum == 0

            # maybe forgot to index into the image variable
            randomNum = random.randrange(0,4) #increase the upper range to make this happen less often
            forgotToIndex = randomNum == 0

            if not(flippedImgAndChannels):
                these_channel_vars = copy.deepcopy(channel_vars)
                these_img_vars = [ copy.copy(img), copy.copy(img) , copy.copy(img)]
            else: 
                temp = copy.deepcopy(channel_vars)
                these_channel_vars = [ copy.copy(img), copy.copy(img) , copy.copy(img)]
                these_img_vars = copy.deepcopy(temp)

            updateChannel = [True,True,True]
            if forgotAChannel:
                whichChannel = random.randrange(0,3)
                updateChannel[whichChannel] = False

            # start constructing the answer

            if triedOneLine:
                incorrect = "    "
                incorrect += braces[whichBraces][0]
                for i in range(len(these_channel_vars)):
                    incorrect += these_channel_vars[i]
                    if (i + 1) in range(len(these_channel_vars)):
                        incorrect += "," # add comma for next layer
                incorrect += braces[whichBraces][1]
                incorrect += " = "
                incorrect += img
                incorrect += ";"

            else:

                incorrect_set = ["","",""] #start with an empty answer set
                for i in range(len(these_channel_vars)):
                    if updateChannel[i]:
                        if not(forgotToStore):
                            incorrect_set[i] += these_channel_vars[i] + " = "

                        incorrect_set[i] += these_img_vars[i]
                        incorrect_set[i] += braces[whichBraces][0] 
                        for j in range(3):
                            if j == whichIndexPull:
                                incorrect_set[i] += str(i+whichIndexStart)
                            else:
                                incorrect_set[i] += ":"
                            if (j + 1) in range(3):
                                incorrect_set[i] += "," # add comma for next layer
                        incorrect_set[i] += braces[whichBraces][1] 

                        incorrect_set[i] += ";"





                # assemble the full answer
                incorrect = ""
                for i in range(len(incorrect_set)):
                    if incorrect_set[i] == "":
                        continue # skip any blank lines
                    foundDuplicate = False
                    for j in (range(len(incorrect_set)-i)):
                        if incorrect_set[i] == incorrect_set[j] and i!= j:
                            foundDuplicate = True
                            break # skip any duplicate lines
                    if not(foundDuplicate):
                        incorrect += "    " + incorrect_set[i]
                        if (i + 1) in range(len(incorrect_set)):
                            incorrect += "\n" # add newline for next channel
                # check for an accidental blank answer
                if incorrect == "":
                    continue

            # if it does NOT match any existing answers, then you have a valid wrong answer
            validWrongAnswer = True
            i = 0
            while i < len(answers):
                if incorrect == answers[i]["ans"]:
                    validWrongAnswer = False
                    break
                i += 1

        answers.append({'tag': 'false', 'ans': incorrect})

    return answers


def copy_in_channels_answers(img,channel_vars,num_answers): 

    # here are all the sets of braces we can use
    braces = [
        ["[","]"],
        ["(",")"],
        ["{","}"]
    ]


    # make empty answers list
    answers = []

    # make correct answer
    correct = ""
    i = 0
    while i < len(channel_vars):
        correct += "    " + img + "(:,:," + str(i+1) + ") = " + channel_vars[i] +  ";"
        if i + 1 < len(channel_vars):
            correct += "\n" # add newline for next channel
        i += 1

    answers.append({'tag': 'true', 'ans': correct})


    # ways to mess up pulling out the channels:
        # forget to store the channels in variables
        # zero indexed instead of one indexed
        # used wrong braces
        # mix up which indices have the : to select all
        # mix up which variable goes on which side of the = sign
        # forget a channel
        # tried to do it in one line
        # forgot to index into image variable

    # construct wrong answers
    while len(answers) < num_answers:

        validWrongAnswer = False
        while validWrongAnswer == False:

            # maybe forgot to store channels
            randomNum = random.randrange(0,4) #increase the upper range to make this happen less often
            forgotToStore = randomNum == 0
           
            # pick a set of braces (might be right, might be wrong)
            whichBraces = random.choice([0,1,1,1,2]) # 1 is the correct set, so weight that more heavily

            # pick a starting index (might be right, might be wrong)
            whichIndexStart = random.choice([0,1,1,1]) # 1 is the correct starting index, so weight that more heavily

            # pick a layer to pull out (might be right, might be wrong)
            whichIndexPull = random.choice([0,1,2,2,2,2]) # 2 is the correct layer (at least, in Python indexing), so weight that more heavily

            # maybe mixed up layers image variable
            randomNum = random.randrange(0,4) #increase the upper range to make this happen less often
            flippedImgAndChannels = randomNum == 0

            # maybe forgot a channel
            randomNum = random.randrange(0,10) #increase the upper range to make this happen less often
            forgotAChannel = randomNum == 0

            # maybe tried to do it in one line
            randomNum = random.randrange(0,10) #increase the upper range to make this happen less often
            triedOneLine = randomNum == 0

            # maybe forgot to index into the image variable
            randomNum = random.randrange(0,4) #increase the upper range to make this happen less often
            forgotToIndex = randomNum == 0

            if not(flippedImgAndChannels):
                these_channel_vars = copy.deepcopy(channel_vars)
                these_img_vars = [ copy.copy(img), copy.copy(img) , copy.copy(img)]
            else: 
                temp = copy.deepcopy(channel_vars)
                these_channel_vars = [ copy.copy(img), copy.copy(img) , copy.copy(img)]
                these_img_vars = copy.deepcopy(temp)

            updateChannel = [True,True,True]
            if forgotAChannel:
                whichChannel = random.randrange(0,3)
                updateChannel[whichChannel] = False

            # start constructing the answer

            if triedOneLine:
                incorrect = "    "
                incorrect += braces[whichBraces][0]
                for i in range(len(these_channel_vars)):
                    incorrect += these_channel_vars[i]
                    if (i + 1) in range(len(these_channel_vars)):
                        incorrect += "," # add comma for next layer
                incorrect += braces[whichBraces][1]
                incorrect += " = "
                incorrect += img
                incorrect += ";"

            else:
                incorrect_set = ["","",""] #start with an empty answer set
                for i in range(len(these_channel_vars)):
                    if updateChannel[i]:
                        if not(forgotToStore):
                            incorrect_set[i] += these_img_vars[i]

                            if not(forgotToIndex):
                                incorrect_set[i] += braces[whichBraces][0] 
                                for j in range(3):
                                    if j == whichIndexPull:
                                        incorrect_set[i] += str(i+whichIndexStart)
                                    else:
                                        incorrect_set[i] += ":"
                                    if (j + 1) in range(3):
                                        incorrect_set[i] += "," # add comma for next layer
                                incorrect_set[i] += braces[whichBraces][1]

                            incorrect_set[i] += " = "
                        incorrect_set[i] += these_channel_vars[i]
                        incorrect_set[i] += ";"

                # assemble the full answer
                incorrect = ""
                for i in range(len(incorrect_set)):
                    if incorrect_set[i] == "":
                        continue # skip any blank lines
                    foundDuplicate = False
                    for j in (range(len(incorrect_set)-i)):
                        if incorrect_set[i] == incorrect_set[j] and i!= j:
                            foundDuplicate = True
                            break # skip any duplicate lines
                    if not(foundDuplicate):
                        incorrect += "    " + incorrect_set[i]
                        if (i + 1) in range(len(incorrect_set)):
                            incorrect += "\n" # add newline for next channel
                # check for an accidental blank answer
                
            if incorrect == "":
                continue

            # if it does NOT match any existing answers, then you have a valid wrong answer
            validWrongAnswer = True
            i = 0
            while i < len(answers):
                if incorrect == answers[i]["ans"]:
                    validWrongAnswer = False
                    break
                i += 1


        answers.append({'tag': 'false', 'ans': incorrect})

    return answers


def select_image_pixels_answers(info,num_answers): 

    # info should be this form:
    # info = {
    #     "img": name of the image variable
    #     "varStore": name of the logical array to store the results in,
    #     "thresholds": [
    #         val1,
    #         val2,
    #         val3
    #     ],
    #     "channel_vars": [
    #         name of channel 1 var,
    #         name of channel 2 var,
    #         name of channel 3 var
    #     ],
    #     "comparisons": [ relational operator, relational operator, relational operator ],
    #     "combine": [logical operator, logical operator]
    # }

    # here are all the sets of braces we can use
    braces = [
        ["[","]"],
        ["(",")"],
        ["{","}"]
    ]

    # possible relational operators to use (do not use >= or <= for this type of question, it's just too confusing for an assessment
    relational_operators = [
        ">",
        "<",
        "==",
    ]
    logical_operators = [
        "&",
        "|",
        "~"
    ]

    # make empty answers list
    answers = []




    # make correct answer
    correct = "    "
    correct += info["varStore"]
    correct += " = "
    # correct += "("
    for i in range(3):
        correct += info["channel_vars"][i]
        correct += info["comparisons"][i]
        correct += info["thresholds"][i]
        if i+1 in range(3):
            correct += " " + info["combine"][i] + " "
    # correct += ")"
    correct += ";"



    answers.append({'tag': 'true', 'ans': correct})

    # select = (red > red_min & green < green_max & blue < blue_max );

    # ways to mess up selecting a set of pixels:
        # forget to store the result
        # index into the storage variable
        # used wrong braces
        # use wrong relational operators
        # use wrong logical operators
        # mix up which threshold goes with which channel

    # construct wrong answers
    while len(answers) < num_answers:

        validWrongAnswer = False
        while validWrongAnswer == False:

            # maybe forgot to store channels
            randomNum = random.randrange(0,4) #increase the upper range to make this happen less often
            forgotToStore = randomNum == 0

            # maybe index into the storage variable
            randomNum = random.randrange(0,4) #increase the upper range to make this happen less often
            indexStorageVariable = randomNum == 0
           
            # pick a set of braces (might be right, might be wrong)
            whichBraces = random.choice([0,1,1,1,2]) # 1 is the correct set, so weight that more heavily

            # maybe use wrong relational operators
            randomNum = random.randrange(0,4) #increase the upper range to make this happen less often
            usedWrongRelationalOperators = randomNum == 0

            # maybe use wrong logical operators
            randomNum = random.randrange(0,4) #increase the upper range to make this happen less often
            usedWrongLogicalOperators = randomNum == 0

            # maybe mix up thresholds
            randomNum = random.randrange(0,4) #increase the upper range to make this happen less often
            mixedUpThresholds = randomNum == 0


            # change around some information based on above "random wrongness"

            theseRelationalOperators = []
            if usedWrongRelationalOperators:
                for i in range(len(info["comparisons"])):
                    theseRelationalOperators.append(random.choice(relational_operators))
            else:
                theseRelationalOperators = copy.deepcopy(info["comparisons"])

            theseLogicalOperators = []
            if usedWrongLogicalOperators:
                for i in range(len(info["combine"])):
                    theseLogicalOperators.append(random.choice(logical_operators))
            else:
                theseLogicalOperators = copy.deepcopy(info["combine"])

            theseThresholds = copy.deepcopy(info["thresholds"])
            if mixedUpThresholds:
                random.shuffle(theseThresholds)


            # start constructing the answer
            incorrect = "    "

            if not(forgotToStore):
                incorrect += info["varStore"]
                incorrect += " = "

            if indexStorageVariable:
                incorrect += info["varStore"]

            # incorrect += braces[whichBraces][0]

            for i in range(3):
                incorrect += info["channel_vars"][i]
                incorrect += theseRelationalOperators[i]
                incorrect += theseThresholds[i]
                if i+1 in range(3):
                    incorrect += " " + theseLogicalOperators[i] + " "
            
            # incorrect += braces[whichBraces][1]
            incorrect += ";"

            # if it does NOT match any existing answers, then you have a valid wrong answer
            validWrongAnswer = True
            i = 0
            while i < len(answers):
                if incorrect == answers[i]["ans"]:
                    validWrongAnswer = False
                    break
                i += 1

        answers.append({'tag': 'false', 'ans': incorrect})

    return answers    


def set_channels_answers(info,num_answers): 

    # Here's what the info variable needs to have:
    #     info = {
    #     "img": image variable name,
    #     "channel_vars": [
    #         name of first channel,
    #         name of second channel,
    #         name of third channel
    #     ],
    #     "channel_index_vals": [ # leave as empty strings if updating the whole channel
    #         index values for first channel,
    #         index values for second channel,
    #         index values for third channel
    #     ],
    #     "channel_values": [
    #         {
    #             "update": True or False,
    #             "correct": correct value,
    #             "incorrect": [a bunch of "distractor" values]
    #         },
    #         {
    #             "update": True or False,
    #             "correct": correct value,
    #             "incorrect": [a bunch of "distractor" values]
    #         },
    #         {
    #             "update": True or False,
    #             "correct": correct value,
    #             "incorrect": [a bunch of "distractor" values]
    #         }
    #     ],
    #     "channel_values_the_same": True or False
    # }

    # here are all the sets of braces we can use
    braces = [
        ["[","]"],
        ["(",")"],
        ["{","}"]
    ]


    # make empty answers list
    answers = []

    # make correct answer

    correct_set = ["","",""] #start with an empty answer set

    for i in range(len(info["channel_vars"])):
        correct_set[i] += info["channel_vars"][i] 
        correct_set[i] += braces[1][0] 
        for j in range(len(info["channel_index_vals"][i])):
            correct_set[i] += info["channel_index_vals"][i][j]
            if (j + 1) in range(len(info["channel_index_vals"][i])):
                correct_set[i] += "," # add comma for value
        correct_set[i] += braces[1][1] 
        correct_set[i] += " = "

        for j in range(len(info["channel_values"][i]["correct"])):
            correct_set[i] += info["channel_values"][i]["correct"][j]
            if (j + 1) in range(len(info["channel_values"][i]["correct"])):
                correct_set[i] += "," # add comma for value
            correct_set[i] += ";"


    # assemble the full answer
    correct = ""
    for i in range(len(info["channel_vars"])):
        correct += "    " + correct_set[i]
        if (i + 1) in range(len(info["channel_vars"])):
            correct += "\n" # add newline for next channel


    answers.append({'tag': 'true', 'ans': correct})


    # ways to mess up setting the channels:
        # forget to index into the channel variable
        # index into the image instead of the channel, for each channel
        # index using the wrong version of the logical matrix
        # tried to do this in one line
        # used a third layer with a channel
        # used wrong braces
        # mix up which values go with which channel
        # forget to update a channel when you are supposed to
        # update a channel when you are NOT supposed to

    # construct wrong answers
    while len(answers) < num_answers:

        validWrongAnswer = False
        while validWrongAnswer == False:

            # maybe forgot to index into the channel
            randomNum = random.randrange(0,6) #increase the upper range to make this happen less often
            forgotToIndex = randomNum == 0

            # maybe indexing into the image instead of the channel
            randomNum = random.randrange(0,6) #increase the upper range to make this happen less often
            usedImage = randomNum == 0

            # maybe indexed using the wrong version of the logical matrix
            randomNum = random.randrange(0,6) #increase the upper range to make this happen less often
            usedWrongLogicalMatrix = randomNum == 0
           
            # maybe tried to do this in one line
            randomNum = random.randrange(0,12) #increase the upper range to make this happen less often
            triedOneLine = randomNum == 0

            # maybe used a third layer with the channel
            randomNum = random.randrange(0,6) #increase the upper range to make this happen less often
            triedThirdLayer = randomNum == 0

            # pick a set of braces (might be right, might be wrong)
            whichBraces = random.choice([0,1,1,1,1,2]) # 1 is the correct set, so weight that more heavily

            # maybe used wrong values
            randomNum = random.randrange(0,4) #increase the upper range to make this happen less often
            usedWrongValues = randomNum == 0

            # maybe mixed up which values go with which channel
            randomNum = random.randrange(0,6) #increase the upper range to make this happen less often
            mix_it_up = randomNum == 0

            # maybe missed a channel to update (or NOT update)
            randomNum = random.randrange(0,6) #increase the upper range to make this happen less often
            forgotAChannel = randomNum == 0

            # set up a bunch of stuff depending on this random wrongness

            if usedImage:
                these_channel_vars = [ copy.copy(info["img"]), copy.copy(info["img"]) , copy.copy(info["img"])]
            else: 
                these_channel_vars = copy.deepcopy(info["channel_vars"])

            these_channel_values = []
            randIndex = random.randrange(0,len(info["channel_values"][0]["incorrect"]))
            for i in range(len(info["channel_values"])):
                if usedWrongValues:
                    these_channel_values.append(info["channel_values"][i]["incorrect"][randIndex])
                else:
                    these_channel_values.append(info["channel_values"][i]["correct"])

            these_channel_index_vals = copy.deepcopy(info["channel_index_vals"])
            if usedWrongLogicalMatrix:
                for i in range(len(these_channel_index_vals)):
                    if len(these_channel_index_vals[i]) == 1:
                        #for i in range(len(these_channel_index_vals)):
                        if these_channel_index_vals[i][0].startswith("~"):
                            these_channel_index_vals[i][0].replace("~", "",1) # remove the not operator
                        else:
                            these_channel_index_vals[i][0] = "~" + these_channel_index_vals[i][0] # add the not operator


            if mix_it_up:
                random.shuffle(these_channel_values)
                random.shuffle(these_channel_index_vals)

            if info["channel_values_the_same"]:
                val = copy.deepcopy(these_channel_values[0])
                # val = ["test","test","test"]
                for i in range(len(these_channel_values)):
                    these_channel_values[i] = val


            updateChannel = []
            for i in range(len(info["channel_values"])):
                    updateChannel.append(info["channel_values"][i]["update"])            
            if forgotAChannel:
                whichChannel = random.randrange(0,len(these_channel_values))
                updateChannel[whichChannel] = not(
                    updateChannel[whichChannel])


            # start constructing the answer

            incorrect = "    "
            if triedOneLine:
                incorrect += braces[whichBraces][0] 
                for j in range(len(these_channel_vars)): 
                    incorrect += these_channel_vars[j]
                    if (j + 1) in range(len(these_channel_vars)):
                        incorrect += "," # add comma for value
                incorrect += braces[whichBraces][1] 
                incorrect += " = "
                incorrect += info["img"]
                incorrect += braces[whichBraces][0]
                incorrect += these_channel_index_vals[0][0] 
                incorrect += braces[whichBraces][1] 
                incorrect += ";"

            else: 
                incorrect_set = ["","",""] #start with an empty answer set
                for i in range(len(these_channel_vars)):

                    if updateChannel[i]:

                        incorrect_set[i] += these_channel_vars[i]
                        if not(forgotToIndex):
                            incorrect_set[i] += braces[whichBraces][0] 
                            for j in range(len(these_channel_index_vals[i])):
                                incorrect_set[i] += these_channel_index_vals[i][j]
                                if (j + 1) in range(len(these_channel_index_vals[i])):
                                  incorrect_set[i] += "," # add comma for value
                            if triedThirdLayer:
                                incorrect_set[i] += ", :"
                            incorrect_set[i] += braces[whichBraces][1] 
                        incorrect_set[i] += " = "

                        for j in range(len(these_channel_values[i])):
                            incorrect_set[i] += these_channel_values[i][j]
                            if (j + 1) in range(len(these_channel_values[i])):
                                incorrect_set[i] += "," # add comma for value
                        incorrect_set[i] += ";"

                # assemble the full answer
                incorrect = ""
                for i in range(len(incorrect_set)):
                    if incorrect_set[i] == "":
                        continue # skip any blank lines
                    foundDuplicate = False
                    for j in (range(len(incorrect_set)-i)):
                        #print("i = " + str(i) + " --> " + incorrect_set[i] + ", j = " + str(j)  + " --> " +  incorrect_set[j])
                        if incorrect_set[i] == incorrect_set[j] and i!= j:
                            foundDuplicate = True
                            break # skip any duplicate lines
                    if not(foundDuplicate):
                        incorrect += "    " + incorrect_set[i]
                        if (i + 1) in range(len(incorrect_set)):
                            incorrect += "\n" # add newline for next channel
                # check for an accidental blank answer
                if incorrect == "":
                    continue
            

            # if it does NOT match any existing answers, then you have a valid wrong answer
            validWrongAnswer = True
            i = 0
            while i < len(answers):
                if incorrect == answers[i]["ans"]:
                    validWrongAnswer = False
                    break
                i += 1
            # print("...................................")    
            # print(incorrect)

        answers.append({'tag': 'false', 'ans': incorrect})

    return answers


def make_relational_logical_operation(info,provideCorrectAnswer):
  
    # info should look like this: 
    # { 
    #     "leftVar": "var",
    #     "rightVar": "var",
    #     "operator": "op",
    #     "distractors": ["var","var",...] <- these can be any other variables/values that are floating around in the problem and that students might accidentally use
    #     "distracting_operators" = ["op", "op"] <- if not specified, then just use all of the operators as distracting operators
    # }

    # WAYS TO MESS THIS UP
    # using the wrong operator
    # using a wrong variable (one of the distractors)
    # flip the order of the correct variables when using the correct operator <- DON'T DO THIS ONE (because it means that two answers can be correct for anything other than > and <

    # here are all the operators we can use (skipping <= and >= for assessment purposes -- it's just too confusing)
    if "distracting_operators" not in info:
        operators = ["<",">","==","~=","&","|"]
    else:
        operators = info["distracting_operators"] 
    # now, append a few instances of the correct one so that the correct operator is weighted more heavily later on when we pick random operators
    operators.append(info["operator"])
    operators.append(info["operator"])
    operators.append(info["operator"])

    # construct the correct answer
    correctAnswer = info["leftVar"] + " " + info["operator"] + " " + info["rightVar"]

    if provideCorrectAnswer:
        return correctAnswer

    else: # lets make some wrong answers!

        # pick an operator (might be right, might be wrong)
        whichOperator = random.choice(operators) 

        # maybe flip the order of the variables
        randomNum = random.randrange(0,6) #increase the upper range to make this happen less often
        flipVariables = randomNum == 0 # flip if you got a zero

        # maybe use a distractor for the left variable
        randomNum = random.randrange(0,6) #increase the upper range to make this happen less often
        distractLeft = randomNum == 0 # use a distractor if you got a zero

        # maybe use a distractor for the right variable
        randomNum = random.randrange(0,6) #increase the upper range to make this happen less often
        distractRight = randomNum == 0 # use a distractor if you got a zero


        if distractLeft:
            thisLeft = random.choice(info["distractors"])
        else:
            thisLeft = info["leftVar"]

        if distractRight:
            thisRight = random.choice(info["distractors"])
        else:
            thisRight = info["rightVar"]

        # construct wrong answer
        incorrectAnswer = thisLeft + " " + whichOperator + " " + thisRight

        # return the constructed wrong answer!
        return incorrectAnswer


def make_relational_logical_operation_answers(info,num_answers):

    # info should look like this: 
    # { 
    #     "leftVar": "var",
    #     "rightVar": "var",
    #     "operator": "op",
    #     "distractors": ["var","var",...] <- these can be any other variables/values that are floating around in the problem and that students might accidentally use
    #     "assignment": "var"
    # }


    # ways to mess this up
    # forget to store the comparison
    # store the comparison in the wrong variable (rare)
    # other mistakes handled by the make_relational_comparisons function

    # make empty answers list
    answers = []

    # make correct answer
    correct = info["assignment"] + " = " + make_relational_logical_operation(info,True) + ";"
    answers.append({'tag': 'true', 'ans': correct})

    # construct wrong answers
    while len(answers) < num_answers:

        validWrongAnswer = False
        while validWrongAnswer == False:

            # pick some random wrongness
            randomNum = random.randrange(0,6) #increase the upper range to make this happen less often
            forgotToStore = randomNum == 0

            randomNum = random.randrange(0,6) #increase the upper range to make this happen less often
            usedWrongVariable = randomNum == 0

            # start constructing the answer

            if forgotToStore:
                incorrect = ""
            else:
                if usedWrongVariable:
                    incorrect = random.choice(info["distractors"]) + " = "
                else:
                    incorrect = info["assignment"] + " = "

            incorrect += make_relational_logical_operation(info,False)
            incorrect += ";"

            # if it does NOT match any existing answers, then you have a valid wrong answer
            validWrongAnswer = True
            i = 0
            while i < len(answers):
                if incorrect == answers[i]["ans"]:
                    validWrongAnswer = False
                    break
                i += 1


        answers.append({'tag': 'false', 'ans': incorrect})

    return answers



def make_multiple_relational_logical_operation_answers(info,num_answers):

    # info should look like this: 
    # { 
    #     "vars": ["var", "var", etc.],
    #     "operators": ["op", "op", etc.],
    #     "distractors": ["var","var",...] <- these can be any other variables/values that are floating around in the problem and that students might accidentally use
    #     "assignment": "var"
    # }


    # ways to mess this up
    # forget to store the comparison
    # store the comparison in the wrong variable (rare)
    # other mistakes handled by the make_relational_comparisons function

    # make empty answers list
    answers = []

    vars = info["vars"]
    operators = info["operators"]

    # make correct answer
    correct = info["assignment"] + " = (";
    for i in range(len(vars)-1):
        correct += vars[i] + " " + operators[i] + " "
    correct += vars[len(vars)-1] + ");"
    answers.append({'tag': 'true', 'ans': correct})

    # construct wrong answers
    while len(answers) < num_answers:

        validWrongAnswer = False
        while validWrongAnswer == False:

            # pick some random wrongness
            randomNum = random.randrange(0,6) #increase the upper range to make this happen less often
            forgotToStore = randomNum == 0

            randomNum = random.randrange(0,6) #increase the upper range to make this happen less often
            usedWrongVariable = randomNum == 0

            # start constructing the answer

            if forgotToStore:
                incorrect = "("
            else:
                if usedWrongVariable:
                    incorrect = random.choice(info["distractors"]) + " = ("
                else:
                    incorrect = info["assignment"] + " = ("

            current_left = vars[0]
            for i in range(1,len(vars)):
                new_info = {}
                new_info["leftVar"] = current_left
                new_info["rightVar"] = vars[i]
                new_info["operator"] = operators[i-1]
                new_info["distractors"] = info["distractors"]

                if operators[i-1] == '|' or operators[i-1] == '&':
                    new_info["distracting_operators"] = ['|','&']
                if operators[i-1] == '==' or operators[i-1] == '~=':
                    new_info["distracting_operators"] = ['==','~=']
                if operators[i-1] == '<' or operators[i-1] == '>':
                    new_info["distracting_operators"] = ['<','>']

                current_left = make_relational_logical_operation(new_info,False)

            incorrect += current_left

            incorrect += ");"

            # if it does NOT match any existing answers, then you have a valid wrong answer
            validWrongAnswer = True
            i = 0
            while i < len(answers):
                if incorrect == answers[i]["ans"]:
                    validWrongAnswer = False
                    break
                i += 1


        answers.append({'tag': 'false', 'ans': incorrect})

    return answers




def make_logical_indexing_answers(info,num_answers):
  
    # info should look like this: 
    # { 
    #     "variable": "var",
    #     "indexing_variable": "var",
    #     "assignment": "var",
    #     "distractors": ["var","var",...] <- these can be any other variables/values that are floating around in the problem and that students might accidentally use

    # }


    # ways to mess this up
    # forget to store the new variable
    # store the comparison in the wrong variable (rare)
    # using the wrong braces/brackets

    # here are all the sets of braces we can use
    braces = [
        ["[","]"],
        ["(",")"],
        ["{","}"]
    ]


    # make empty answers list
    answers = []

    # make correct answer
    correct = info["assignment"] + " = " + info["variable"] + braces[1][0] + info["indexing_variable"] + braces[1][1] + ";"
    answers.append({'tag': 'true', 'ans': correct})

    # construct wrong answers
    while len(answers) < num_answers:

        validWrongAnswer = False
        while validWrongAnswer == False:

            # pick some random wrongness
            whichBraces = random.choice(braces)

            randomNum = random.randrange(0,5) #increase the upper range to make this happen less often
            forgotToStore = randomNum == 0

            randomNum = random.randrange(0,5) #increase the upper range to make this happen less often
            usedWrongAssignmentVar = randomNum == 0

            randomNum = random.randrange(0,5) #increase the upper range to make this happen less often
            usedWrongSourceVar = randomNum == 0

            randomNum = random.randrange(0,5) #increase the upper range to make this happen less often
            usedWrongIndexVar = randomNum == 0

            # start constructing the answer

            if forgotToStore:
                incorrect = ""
            else:
                if usedWrongAssignmentVar:
                    incorrect = random.choice(info["distractors"]) + " = "
                else:
                    incorrect = info["assignment"] + " = "

            if usedWrongSourceVar:
                    incorrect += random.choice(info["distractors"]) 
            else:
                incorrect += info["variable"] 
            
            incorrect += whichBraces[0]

            if usedWrongIndexVar:
                    incorrect += random.choice(info["distractors"]) 
            else:
                incorrect += info["indexing_variable"] 

            incorrect += whichBraces[1]

            incorrect += ";"

            # if it does NOT match any existing answers, then you have a valid wrong answer
            validWrongAnswer = True
            i = 0
            while i < len(answers):
                if incorrect == answers[i]["ans"]:
                    validWrongAnswer = False
                    break
                i += 1


        answers.append({'tag': 'false', 'ans': incorrect})

    return answers



def check_duplicate_answers(incorrect,answers):
    # if it does NOT match any existing answers, then you have a valid wrong answer

    # first, assume that this IS a valid wrong answer
    validWrongAnswer = True
    i = 0
    while i < len(answers):
        if incorrect == answers[i]["ans"]:

            # if you found a duplicate, then it's not valid :( 
            validWrongAnswer = False
            break
        i += 1
    
    return validWrongAnswer

# ----------------------------------------------------------------
# ----------------------------------------------------------------
# ----------------------------------------------------------------
# ----------------------------------------------------------------







