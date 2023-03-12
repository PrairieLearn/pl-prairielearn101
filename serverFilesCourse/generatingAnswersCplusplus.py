from math import dist
import random
import string
import copy


# --------------------------------------------------------
# FUNCTIONS FOR GENERATING ANSWERS
# --------------------------------------------------------



def make_parameters(info,provideCorrectAnswer):



    parameters = copy.deepcopy(info["parameters"])
    # arguments = copy.deepcopy(info["arguments"])
    distractor_types = copy.deepcopy(info["distractor_types"])

  
    # WAYS TO MESS THIS UP
    # using the wrong brackets/braces
    # using the arguments instead of the parameters -- SKIP FOR C++
    # forgetting the parameters
    # mixing up the order of the parameters
    # forgetting the types for the parameters
    # passing by value and/or reference (whichever is wrong)

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
        if parameters[i]["pass_by_reference"] == "const":
            correctAnswer += "const "
        correctAnswer += parameters[i]["type"] + " "
        if parameters[i]["pass_by_reference"]:  # works for both pass by reference and pass by const reference
            correctAnswer += "&"
        correctAnswer += parameters[i]["name"]
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
        whichBraces = random.choice([0,1,1,1,1,1,1,1,2]) # 1 is the correct set, so weight that more heavily

        # if the wrong answer forgets the parameters, we can 
        # immediately return a wrong answer (using a random set of braces)
        randomNum = random.randrange(0,20) #increase the upper range to make this happen less often
        forget_parameters = randomNum == 0
        if forget_parameters:
            answer = braces[whichBraces][0] + " " + braces[whichBraces][1]
            return answer

        # otherwise, construct some other wrong answer
        else:

            # # maybe flip the parameters with the arguments
            # randomNum = random.randrange(0,6) #increase the upper range to make this happen less often
            # flipVariables = randomNum == 0 # flip if you got a zero

            # # which variables are we using, arguments or parameters?
            variable_set = parameters
            # if flipVariables:
            #     for i in range(len(variable_set)):
            #         variable_set[i]["name"] = arguments[i]
            

            # maybe shuffle the order of the variables
            randomNum = random.randrange(0,3) #increase the upper range to make this happen less often
            mix_it_up = randomNum == 0 # mix it up if you got a zero
            if mix_it_up:
                random.shuffle(variable_set)

            # maybe forget the parameter types
            randomNum = random.randrange(0,3) #increase the upper range to make this happen less often
            forget_types = randomNum == 0


            answer = braces[whichBraces][0]
            i = 0
            while i < len(variable_set):

                # maybe use the wrong type
                randomNum = random.randrange(0,3) #increase the upper range to make this happen less often
                wrong_type = randomNum == 0

                # maybe pass the parameter in wrong
                randomNum = random.randrange(0,2) #increase the upper range to make this happen less often
                wrong_pass = randomNum == 0
                
                # logic to pass in the parameter wrongly (this isn't very slick, but hopefully this is the most transparent way of laying this out)
                if wrong_pass:
                    if parameters[i]["pass_by_reference"] == "const":
                        answer += ""
                    else:
                        answer += random.choice(["const ", ""])
                else:
                    if parameters[i]["pass_by_reference"] == "const":
                        answer += "const "
                    else:
                        answer += ""

                if not forget_types:
                    if wrong_type:
                        answer += random.choice(distractor_types) + " "
                    else:
                        answer += variable_set[i]["type"] + " "

                # logic to pass in the parameter wrongly (this isn't very slick, but hopefully this is the most transparent way of laying this out)
                if wrong_pass:
                    if not parameters[i]["pass_by_reference"]:
                        answer += "&"
                    else:
                        answer += ""
                else:
                    if not parameters[i]["pass_by_reference"]:
                        answer += ""
                    else:
                        answer += "&"

                    
                answer += variable_set[i]["name"]

                if i + 1 < len(variable_set):
                    answer += ", "
                else:
                    answer += braces[whichBraces][1]
                    break
                i += 1
            
            # return the constructed wrong answer!
            return answer


def make_arguments(info,provideCorrectAnswer):

    parameters = copy.deepcopy(info["parameters"])
    arguments = copy.deepcopy(info["arguments"])
    distractor_types = copy.deepcopy(info["distractor_types"])

  
    # WAYS TO MESS THIS UP
    # using the wrong brackets/braces
    # using the parameters instead of the arguments 
    # forgetting the arguments
    # mixing up the order of the arguments
    # including the types for the arguments
    # including an & for pass by reference 

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
            correctAnswer += braces[1][1]
            break
        i += 1

    if provideCorrectAnswer:
        return correctAnswer

    else: # lets make some wrong answers!

        # pick a set of braces (might be right, might be wrong)
        whichBraces = random.choice([0,1,1,1,1,1,1,1,2]) # 1 is the correct set, so weight that more heavily

        # if the wrong answer forgets the arguments, we can 
        # immediately return a wrong answer (using a random set of braces)
        randomNum = random.randrange(0,20) #increase the upper range to make this happen less often
        forget_parameters = randomNum == 0
        if forget_parameters:
            answer = braces[whichBraces][0] + " " + braces[whichBraces][1]
            return answer

        # otherwise, construct some other wrong answer
        else:

            # maybe flip the parameters with the arguments
            randomNum = random.randrange(0,6) #increase the upper range to make this happen less often
            flipVariables = randomNum == 0 # flip if you got a zero

            # which variables are we using, arguments or parameters?
            variable_set = parameters # to get the type data
            if not flipVariables:
                for i in range(len(variable_set)):
                    variable_set[i]["name"] = arguments[i]
            

            # maybe shuffle the order of the variables
            randomNum = random.randrange(0,3) #increase the upper range to make this happen less often
            mix_it_up = randomNum == 0 # mix it up if you got a zero
            if mix_it_up:
                random.shuffle(variable_set)

            # maybe include the parameter types
            randomNum = random.randrange(0,3) #increase the upper range to make this happen less often
            include_types = randomNum == 0

            answer = braces[whichBraces][0]
            i = 0
            while i < len(variable_set):
                
                # maybe use the wrong type
                randomNum = random.randrange(0,3) #increase the upper range to make this happen less often
                wrong_type = randomNum == 0

                if include_types:
                    if wrong_type:
                        answer += random.choice(distractor_types) + " "
                    else:
                        answer += variable_set[i]["type"] + " "

                # maybe include an ampersand
                randomNum = random.randrange(0,6) #increase the upper range to make this happen less often
                include_ampersand = randomNum == 0

                if include_ampersand:
                    answer += "&"
                    
                answer += variable_set[i]["name"]

                if i + 1 < len(variable_set):
                    answer += ", "
                else:
                    answer += braces[whichBraces][1]
                    break
                i += 1
            
            # return the constructed wrong answer!
            return answer


def func_header_answers(info,isPrototype,num_answers):
  

    # info needs to have at least this information:
    # info = {
    #     "function_name": "name", 
    #     "function_type": "type",
    #     "parameters": [
    #         {
    #             "name": "param",
    #             "type": "type",
    #             "pass_by_reference": True,
    #         },
    #         {
    #             "name": "param",
    #             "type": "type",
    #             "pass_by_reference": False,
    #         }
    #     ],
    #     "return_variables": [
    #         {
    #             "name": "rv",
    #         },
    #     ],
    #     "arguments": ["var","var", etc.], 
    #     "assignments": ["var","var", etc.],
    #     "distractor_functions": ["name", "name", etc.],
    #     "distractor_types":[
    #         "type","type", etc.
    #     ]
    # }

    # make empty answers list
    answers = []

    correct = info["function_type"] + " "
    correct += info["function_name"]
    correct += make_parameters(info,True)
    if isPrototype:
        correct += ";"
    else: 
        correct += " {"

    answers.append({'tag': 'true', 'ans': correct})

    
    
    # ways to mess up a function header:
    # including the word "function"
    # forgetting the function type
    # using the wrong function type
    # messing up the parameters (lots of ways)
    # swapping { and ; depending on if it's the start of the function definition or it's the function prototype

    # construct wrong answers
    while len(answers) < num_answers:

        validWrongAnswer = False
        while validWrongAnswer == False:

            # pick some random wrongness
            randomNum = random.randrange(0,12) #increase the upper range to make this happen less often
            includeFunctionWord = randomNum == 0

            randomNum = random.randrange(0,4) #increase the upper range to make this happen less often
            forgetType = randomNum == 0

            randomNum = random.randrange(0,4) #increase the upper range to make this happen less often
            usedWrongType = randomNum == 0

            # maybe use the header wrong ( definition vs. prototype )
            randomNum = random.randrange(0,4) #increase the upper range to make this happen less often
            wrongUse = randomNum == 0

            # start constructing the answer
            if includeFunctionWord:
                incorrect = "function" + " "
            else:
                incorrect = ""

            if not forgetType:
                if usedWrongType:
                    incorrect += random.choice(info["distractor_types"]) + " "
                else: 
                    incorrect += info["function_type"] + " "
            incorrect += info["function_name"]

            incorrect += make_parameters(info,False)

            if (wrongUse and isPrototype) or (not wrongUse and not isPrototype):
                incorrect += " {"
            else:
                incorrect += ";"
            

            # if it does NOT match any existing answers, then you have a valid wrong answer
            validWrongAnswer = check_duplicate_answers(incorrect,answers)


        answers.append({'tag': 'false', 'ans': incorrect})

    return answers


def func_call_answers(info,num_answers):

    # info needs to have at least this information:
    # info = {
    #     "function_name": "name", 
    #     "function_type": "type",
    #     "parameters": [
    #         {
    #             "name": "param",
    #             "type": "type",
    #             "pass_by": "value",
    #         },
    #         {
    #             "name": "param",
    #             "type": "type",
    #             "pass_by": "reference",
    #         }
    #     ],
    #     "return_variables": [
    #         {
    #             "name": "rv",
    #         },
    #     ],
    #     "arguments": ["var","var", etc.], 
    #     "assignments": ["var","var", etc.],
    #     "distractor_functions": ["name", "name", etc.],
    #     "distractor_types": [
    #         "type","type", etc.
    #     ]
    #     "distractor_rvs": [
    #         "x",
    #         "isReliable"
    #     ]
    # }  



    # make empty answers list
    answers = []

    correct = ""
    if (not len(info["assignments"]) == 0):
        correct += info["function_type"] + " "
        correct += info["assignments"][0]
        correct += " = "
    correct += info["function_name"]
    correct += make_arguments(info,True)
    correct += ";"

    answers.append({'tag': 'true', 'ans': correct})


    # ways to mess up calling a function:
    # including the word "function"
    # forgot equal sign
    # flipping the arguments with the assignment variables [DON'T DO FOR NOW]
    # using the parameters instead of the arguments
    # trying to store the return value from a void function
    # MAYBE FOR THE FUTURE: storing the value into the wrong type variable
    # MAYBE FOR THE FUTURE: using the return variables instead of the assignment variables (this might be harder for our students to catch than we can catch)
    # MAYBE FOR THE FUTURE: use the wrong function (list distractor names, this is less of an issue with C++ because we don't really use many built-in functions)

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

            randomNum = random.randrange(0,6) #increase the upper range to make this happen less often
            storedVoidReturn = randomNum == 0

            # # if there are distractor functions available, maybe use one
            # if usedWrongName and ("distractor_functions" in info):
            #     if (len(info["distractor_functions"]) > 0):
            #         thisFuncName = random.choice(info["distractor_functions"])
            #     else: 
            #         thisFuncName = info["function_name"]
            # else:
            #      thisFuncName = info["function_name"]

            thisFuncName = info["function_name"]


            # start constructing the answer
            incorrect = "" #start with an empty answer

            # skip the assignment step if this is a void function and did NOT try to store a return value
            skipAssignment = info["function_type"] == "void" and not storedVoidReturn

            if not skipAssignment:
                if info["function_type"] == "void":
                    assignVar = random.choice(info["distractor_types"]) + " " + random.choice(info["distractor_rvs"])
                else:
                    assignVar = info["function_type"] + " " + info["assignments"][0]
                if not(forgotEqualSign):
                    if flipArgumentsAndReturnVariables:
                        incorrect += make_arguments(info,False)
                    else:
                        incorrect += assignVar
                    if incorrect != "":
                        incorrect += " = "

            if includeFunctionWord:
                incorrect += "function "

            incorrect += thisFuncName

            # if flipArgumentsAndReturnVariables: #also covers using parameters instead
            #     incorrect += make_arguments(info,False)
            # else: 
            #     incorrect += make_arguments(info["arguments"],info["parameters"],False)
            incorrect += make_arguments(info,False)

            incorrect += ";"

            # if it does NOT match any existing answers, then you have a valid wrong answer
            validWrongAnswer = check_duplicate_answers(incorrect,answers)



        answers.append({'tag': 'false', 'ans': incorrect})

    return answers


def buggy_func_call_answers(info):
    


    # The correct answer, stored in the wrong_answer variable (for copy and paste below)
    wrong_answer = ""
    if (not len(info["assignments"]) == 0):
        wrong_answer += info["function_type"] + " "
        wrong_answer += info["assignments"][0]
        wrong_answer += " = "
    wrong_answer += info["function_name"]
    wrong_answer += make_arguments(info,True)
    wrong_answer += ";"

    # Construct wrong answers
    wrong_answers = []

    # Ways to mess up calling a function:

    # 1. including the word "function"
    wrong_answer = ""
    if (not len(info["assignments"]) == 0):
        wrong_answer += info["function_type"] + " "
        wrong_answer += info["assignments"][0]
        wrong_answer += " = "
    wrong_answer += "function "
    wrong_answer += info["function_name"]
    wrong_answer += make_arguments(info,True)
    wrong_answer += ";"

    answer = {
        "ans": wrong_answer,
        "bug": "included the word \"function\" when calling the function",
        "fix": "remove the word \"function\" -- you just have to use the name of the function"
    }
    wrong_answers.append(answer)


    # 2. using the wrong brackets/braces
    wrong_answer = ""
    if (not len(info["assignments"]) == 0):
        wrong_answer += info["function_type"] + " "
        wrong_answer += info["assignments"][0]
        wrong_answer += " = "
    wrong_answer += info["function_name"]
    args = make_arguments(info,True)
    args = args.replace("(","[")
    args = args.replace(")","]")
    wrong_answer += args
    wrong_answer += ";"


    answer = {
        "ans": wrong_answer,
        "bug": "used the wrong brackets/braces/parentheses",
        "fix": "use () for passing the arguments"
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
    tempInfo = copy.deepcopy(info)
    tempInfo["arguments"] = shuffled_args

    # now, make the answer
    wrong_answer = ""
    if (not len( tempInfo["assignments"]) == 0):
        wrong_answer += info["function_type"] + " "
        wrong_answer +=  tempInfo["assignments"][0]
        wrong_answer += " = "
    wrong_answer +=  tempInfo["function_name"]
    wrong_answer += make_arguments( tempInfo,True)
    wrong_answer += ";"

    answer = {
        "ans": wrong_answer,
        "bug": "mixed up the order of the arguments",
        "fix": "double check that they are passing the correct arguments to the correct parameters"
    }
    wrong_answers.append(answer)


    # 4. storing the return value from a void function
    random_type = random.choice(["int","double","void","string","bool","char"])
    wrong_answer = ""
    wrong_answer += random_type + " "
    wrong_answer += random.choice(info["distractor_rvs"])
    wrong_answer += " = "
    wrong_answer += info["function_name"]
    wrong_answer += make_arguments(info,True)
    wrong_answer += ";"

    answer = {
        "ans": wrong_answer,
        "bug": "tried to store a return value from a void function",
        "fix": "remove the variable and equal sign -- you just call a void function and it does its stuff"
    }
    wrong_answers.append(answer)


    # 5. forgetting to store return variable from non-void function
    wrong_answer = ""
    wrong_answer += info["function_name"]
    wrong_answer += make_arguments(info,True)
    wrong_answer += ";"

    answer = {
        "ans": wrong_answer,
        "bug": "forgotten to store the return value from a non-void function",
        "fix": "add a declared variable and an equal sign before the function call"
    }
    wrong_answers.append(answer)



    # 6. used the function header

    wrong_answer = info["function_type"] + " "
    wrong_answer += info["function_name"]
    wrong_answer += make_parameters(info,True)
    wrong_answer += ";"

    answer = {
        "ans": wrong_answer,
        "bug": "used the function header instead of calling the function",
        "fix": "review how to call a function (given the function header)"
    }
    wrong_answers.append(answer)



    # 7. using the wrong variables (just in general) 

    # make some wrong variables
    prefixes = ["new_","old_","temp_","test_","TEMP_","TEST_","NEW_","OLD_"]
    suffixes = ["_new","_old","_1","_2","_3","_v1","_v2","_v3","_temp","_test"]

    parameters = copy.deepcopy(info["parameters"])
    arguments = copy.deepcopy(info["arguments"])

    i = 0
    while i < len(arguments):
        if (random.getrandbits(2)):
            arguments[i] = random.choice(prefixes) + arguments[i]
        else:
            if (random.getrandbits(2)):
                arguments[i] = arguments[i] + random.choice(suffixes)
            else:
                arguments[i] = parameters[i]["name"] + random.choice(suffixes)
        i += 1

    tempInfo = copy.deepcopy(info)
    
    tempInfo["arguments"] = arguments

    wrong_answer = ""
    if (not len(tempInfo["assignments"]) == 0):
        wrong_answer += info["function_type"] + " "
        wrong_answer += tempInfo["assignments"][0]
        wrong_answer += " = "
    wrong_answer += tempInfo["function_name"]
    wrong_answer += make_arguments(tempInfo,True)
    wrong_answer += ";"

    answer = {
        "ans": wrong_answer,
        "bug": "used variables that either do not exist or were not intended to be used in this function call",
        "fix": "double-check that the correct variables are being used in this function call"
    }
    wrong_answers.append(answer)



    # 8. included the types with the arguments 

    wrong_answer = ""
    if (not len(info["assignments"]) == 0):
        wrong_answer += info["function_type"] + " "
        wrong_answer += info["assignments"][0]
        wrong_answer += " = "
    wrong_answer += info["function_name"]
    wrong_answer += "("
    for i in range(len(info["arguments"])):
        wrong_answer += info["parameters"][i]["type"] + " "
        wrong_answer += info["arguments"][i]
        if i + 1 < len(arguments):
            wrong_answer += ", "
    wrong_answer += ")"
    wrong_answer += ";"

    answer = {
        "ans": wrong_answer,
        "bug": "included the variable types with the arguments",
        "fix": "remove the variable types (those go in the function header, but not when calling the function)"
    }
    wrong_answers.append(answer)


    # 9. included an & for pass by reference parameters

    wrong_answer = ""
    if (not len(info["assignments"]) == 0):
        wrong_answer += info["function_type"] + " "
        wrong_answer += info["assignments"][0]
        wrong_answer += " = "
    wrong_answer += info["function_name"]
    wrong_answer += "("
    for i in range(len(info["arguments"])):
        if info["parameters"][i]["pass_by_reference"]:
            wrong_answer += "&"
        wrong_answer += info["arguments"][i]
        if i + 1 < len(arguments):
            wrong_answer += ", "
    wrong_answer += ")"
    wrong_answer += ";"

    answer = {
        "ans": wrong_answer,
        "bug": "included an & for arguments that are being passed by reference",
        "fix": "remove the & (that goes in the function header, but not when calling the function)"
    }
    wrong_answers.append(answer)



    return wrong_answers





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







# # info needs to have at least this information:
# info = {
#     "function_name": "test_func", 
#     "function_type": "void",
#     "parameters": [
#         {
#             "name": "param1",
#             "type": "int",
#             "pass_by_reference": True,
#         },
#         {
#             "name": "param2",
#             "type": "double",
#             "pass_by_reference": False,
#         }
#     ],
#     "return_variables": [
#         {
#             "name": "rv",
#         },
#     ],
#     "arguments": ["arg1","arg2" ], 
#     "assignments": [
#         # "assign1"
#     ],
#     "distractor_functions": ["func", "another_func" ],
#     "distractor_types":[
#         "string","char","int","double","bool", 
#     ],
#     "distractor_rvs":[
#         "x",
#         "isReliable" 
#     ]
# }



# num_answers = 5
# answers = buggy_func_call_answers(info)

# for i in range(len(answers)):
#     print("   " + answers[i]["ans"])
#     print("      " + answers[i]["bug"])
#     print("      " + answers[i]["fix"])



# Binary search functions

def output_statement(info, num_answers):

    # Correct statement looks something like this:
    # cout << "Enter the optimal temperature: ";

    # info should look like this: 
    # { 
    #     "stream": "cout",
    #     "distractor_streams": ["cin","out"],
    #     "value": '"Enter the optimal temperature: "', // or a variable name
    #     "endl": False // True if you want an endl at the end of the output
    #     "distractor_vars": ["var1", "var2"] // can be empty if you don't want any distractor variables
    # }

    # ways to mess this up
    # use wrong stream
    # use >> instead of <<
    # forget semicolon
    # output wrong variable

    # make empty answers list
    answers = []

    # make correct answer
    correct = info["stream"] + " << " + info["value"]
    if info["endl"]:
        correct += " << endl;"
    else:
        correct += ";"
    answers.append({'tag': 'true', 'ans': correct})

    # construct wrong answers
    while len(answers) < num_answers:

        validWrongAnswer = False
        while validWrongAnswer == False:

            # pick some random wrongness
            randomNum = random.randrange(0,6) #increase the upper range to make this happen less often
            wrongStream = randomNum == 0

            randomNum = random.randrange(0,6) #increase the upper range to make this happen less often
            wrongOperator = randomNum == 0

            randomNum = random.randrange(0,10) #increase the upper range to make this happen less often
            noSemicolon = randomNum == 0

            if len(info["distractor_vars"]) > 0:
                randomNum = random.randrange(0,6) #increase the upper range to make this happen less often
                wrongVariable = randomNum == 0
            else:
                wrongVariable = False

            # start constructing the answer

            if wrongStream:
                incorrect = random.choice(info["distractor_streams"])
            else:
                incorrect = info["stream"]

            if wrongOperator:
                incorrect += " >> "
            else:
                incorrect += " << "

            if wrongVariable:
                incorrect += random.choice(info["distractor_vars"])
            else:
                incorrect += info["value"]

            if info["endl"]:
                if wrongOperator:
                    incorrect += " >> "
                else:
                    incorrect += " << "

                incorrect += "endl"

            if not noSemicolon:
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




def input_statement(info, num_answers):

    # Correct statement looks something like this:
    # cin << target_temp;

    # info should look like this: 
    # { 
    #     "stream": "cin",
    #     "distractor_streams": ["cout","fin"],
    #     "value": "target_temp",
    # }

    # ways to mess this up
    # use wrong stream
    # use << instead of >>
    # use endl with input
    # forget semicolon

    # make empty answers list
    answers = []

    # make correct answer
    correct = info["stream"] + " >> " + info["value"] + ";"
    answers.append({'tag': 'true', 'ans': correct})

    # construct wrong answers
    while len(answers) < num_answers:

        validWrongAnswer = False
        while validWrongAnswer == False:

            # pick some random wrongness
            randomNum = random.randrange(0,6) #increase the upper range to make this happen less often
            wrongStream = randomNum == 0

            randomNum = random.randrange(0,6) #increase the upper range to make this happen less often
            wrongOperator = randomNum == 0

            randomNum = random.randrange(0,6) #increase the upper range to make this happen less often
            useEndl = randomNum == 0

            randomNum = random.randrange(0,10) #increase the upper range to make this happen less often
            noSemicolon = randomNum == 0

            # start constructing the answer

            if wrongStream:
                incorrect = random.choice(info["distractor_streams"])
            else:
                incorrect = info["stream"]

            if wrongOperator:
                incorrect += " << "
            else:
                incorrect += " >> "

            incorrect += info["value"]

            if useEndl:
                if wrongOperator:
                    incorrect += " << "
                else:
                    incorrect += " >> "

                incorrect += "endl"

            if not noSemicolon:
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




def binary_search_loop(info,num_answers):

    # should be: while (m_high - m_low > tolerance) {

    # info should look like this: 
    # { 
    #     "high_var": "m_high",
    #     "low_var": "m_low",
    #     "tolerance_var": "tolerance",
    #     "distractor_vars": ["m_mid","celsius"],
    # }

    # ways to mess this up
    # use for instead of while
    # use + instead of -
    # use < instead of >
    # get variables wrong

    # make empty answers list
    answers = []

    # make correct answer
    correct = "while (" + info["high_var"] + " - " + info["low_var"] + " > " + info["tolerance_var"] + ") {"
    answers.append({'tag': 'true', 'ans': correct})

    # construct wrong answers
    while len(answers) < num_answers:

        validWrongAnswer = False
        while validWrongAnswer == False:

            # pick some random wrongness
            randomNum = random.randrange(0,6) #increase the upper range to make this happen less often
            forNotWhile = randomNum == 0

            randomNum = random.randrange(0,6) #increase the upper range to make this happen less often
            plusNotMinus = randomNum == 0

            randomNum = random.randrange(0,6) #increase the upper range to make this happen less often
            lessThanNotGreaterThan = randomNum == 0

            randomNum = random.randrange(0,6) #increase the upper range to make this happen less often
            wrongFirstVariable = randomNum == 0

            randomNum = random.randrange(0,6) #increase the upper range to make this happen less often
            wrongSecondVariable = randomNum == 0

            randomNum = random.randrange(0,6) #increase the upper range to make this happen less often
            wrongThirdVariable = randomNum == 0

            # start constructing the answer

            if forNotWhile:
                incorrect = "for ("
            else:
                incorrect = "while ("

            if wrongFirstVariable:
                incorrect += random.choice(info["distractor_vars"] + [info["low_var"]] + [info["tolerance_var"]])
            else:
                incorrect += info["high_var"]

            if plusNotMinus:
                incorrect += " + "
            else:
                incorrect += " - "

            if wrongSecondVariable:
                incorrect += random.choice(info["distractor_vars"] + [info["high_var"]] + [info["tolerance_var"]])
            else:
                incorrect += info["low_var"]

            if lessThanNotGreaterThan:
                incorrect += " < "
            else:
                incorrect += " > "

            if wrongThirdVariable:
                incorrect += random.choice(info["distractor_vars"] + [info["high_var"]] + [info["low_var"]])
            else:
                incorrect += info["tolerance_var"]

            incorrect += ") {"

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




def binary_search_midpoint(info,num_answers):

    # correct answer: m_mid = (m_low + m_high) / 2.0;

    # info should look like this: 
    # { 
    #     "high_var": "m_high",
    #     "low_var": "m_low",
    #     "mid_var": "m_mid"
    #     "distractor_vars": ["celsius"],
    # }

    # ways to mess this up
    # use multiplication instead of division
    # forget to assign
    # get variables wrong

    # make empty answers list
    answers = []

    # make correct answer
    correct = "    " + info["mid_var"] + " = (" + info["low_var"] + " + " + info["high_var"] + ") / 2.0;" 
    answers.append({'tag': 'true', 'ans': correct})

    # construct wrong answers
    while len(answers) < num_answers:

        validWrongAnswer = False
        while validWrongAnswer == False:

            # pick some random wrongness
            randomNum = random.randrange(0,6) #increase the upper range to make this happen less often
            multiplicationNotDivision = randomNum == 0

            randomNum = random.randrange(0,10) #increase the upper range to make this happen less often
            forgetToAssign = randomNum == 0

            randomNum = random.randrange(0,6) #increase the upper range to make this happen less often
            wrongFirstVariable = randomNum == 0

            randomNum = random.randrange(0,6) #increase the upper range to make this happen less often
            wrongSecondVariable = randomNum == 0

            randomNum = random.randrange(0,6) #increase the upper range to make this happen less often
            wrongThirdVariable = randomNum == 0

            # start constructing the answer
            incorrect = "    "

            if not forgetToAssign:
                if wrongFirstVariable:
                    incorrect += random.choice(info["distractor_vars"] + [info["low_var"]] + [info["high_var"]]) + " = "
                else:
                    incorrect += info["mid_var"] + " = "

            incorrect += "("

            if wrongSecondVariable:
                incorrect += random.choice(info["distractor_vars"] + [info["mid_var"]]) + " + "
            else:
                incorrect += info["low_var"] + " + "

            if wrongThirdVariable:
                incorrect += random.choice(info["distractor_vars"] + [info["mid_var"]]) + ") "
            else:
                incorrect += info["high_var"] + ") "

            if multiplicationNotDivision:
                incorrect += "* 2.0;"
            else:
                incorrect += "/ 2.0;"

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




def temperature_calculation(info, num_answers):
    
    #should be: double celsius = 4.2 * cos(calculate_value(m)) + 13.7;

    # info should look like this: 
    # { 
    #     "assignment_var": "celsius",
    #     "helper_function": "calculate_value",
    #     "month_var": "m_mid"
    #     "distractor_vars": ["m_low","m_high"],
    # }

    # ways to mess this up
    # use wrong variable for m
    # don't declare celsius as a double
    # forget to assign
    # use brackets in function call instead of parens

    # make empty answers list
    answers = []

    # make correct answer
    correct = "    double " + info["assignment_var"] + " = 4.2 * cos(" + info["helper_function"] + "(" + info["month_var"] + ")) + 13.7;"
    answers.append({'tag': 'true', 'ans': correct})

    # construct wrong answers
    while len(answers) < num_answers:

        validWrongAnswer = False
        while validWrongAnswer == False:

            # pick some random wrongness
            randomNum = random.randrange(0,6) #increase the upper range to make this happen less often
            noDeclaration = randomNum == 0

            randomNum = random.randrange(0,10) #increase the upper range to make this happen less often
            forgetToAssign = randomNum == 0

            randomNum = random.randrange(0,10) #increase the upper range to make this happen less often
            bracketsNotParens = randomNum == 0

            randomNum = random.randrange(0,6) #increase the upper range to make this happen less often
            wrongVariable = randomNum == 0

            # start constructing the answer
            incorrect = "    "

            if not forgetToAssign:
                if not noDeclaration:
                    incorrect += "double "
                incorrect += info["assignment_var"] + " = "
            
            incorrect += "4.2 * cos(" + info["helper_function"]

            if bracketsNotParens:
                incorrect += "["
            else:
                incorrect += "("

            if wrongVariable:
                incorrect += random.choice(info["distractor_vars"])
            else:
                incorrect += info["month_var"]

            if bracketsNotParens:
                incorrect += "]"
            else:
                incorrect += ")"

            incorrect += ") + 13.7;"

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




def density_calculation(info, num_answers):
    
    #should be: double density = 270 * calculate_value(t * t) + (calculate_value(t) * calculate_value(t));

    # info should look like this: 
    # { 
    #     "assignment_var": "density",
    #     "helper_function": "calculate_value",
    #     "month_var": "midT"
    #     "distractor_vars": ["lowT","highT"],
    # }

    # ways to mess this up
    # use wrong variable for t
    # don't declare density as a double
    # forget to assign
    # use brackets in function call instead of parens

    # make empty answers list
    answers = []

    # make correct answer
    correct = "    double " + info["assignment_var"] + " = 270 * " + info["helper_function"] + "(" + info["month_var"] + " * " + info["month_var"] + ") + (" + info["helper_function"] + "(" + info["month_var"] + ") * " + info["helper_function"] + "(" + info["month_var"] + "));"
    answers.append({'tag': 'true', 'ans': correct})

    # construct wrong answers
    while len(answers) < num_answers:

        validWrongAnswer = False
        while validWrongAnswer == False:

            # pick some random wrongness
            randomNum = random.randrange(0,6) #increase the upper range to make this happen less often
            noDeclaration = randomNum == 0

            randomNum = random.randrange(0,10) #increase the upper range to make this happen less often
            forgetToAssign = randomNum == 0

            randomNum = random.randrange(0,10) #increase the upper range to make this happen less often
            bracketsNotParens = randomNum == 0

            randomNum = random.randrange(0,6) #increase the upper range to make this happen less often
            wrongVariable = randomNum == 0

            # start constructing the answer
            incorrect = "    "

            if not forgetToAssign:
                if not noDeclaration:
                    incorrect += "double "
                incorrect += info["assignment_var"] + " = "
            
            incorrect += "270 * " + info["helper_function"]

            if bracketsNotParens:
                incorrect += "["
            else:
                incorrect += "("

            wrongVariableChoice = random.choice(info["distractor_vars"])
            if wrongVariable:
                incorrect += wrongVariableChoice
            else:
                incorrect += info["month_var"]

            incorrect += " * "

            if wrongVariable:
                incorrect += wrongVariableChoice
            else:
                incorrect += info["month_var"]

            if bracketsNotParens:
                incorrect += "]"
            else:
                incorrect += ")"

            incorrect += " + (" + info["helper_function"]

            if bracketsNotParens:
                incorrect += "["
            else:
                incorrect += "("

            if wrongVariable:
                incorrect += wrongVariableChoice
            else:
                incorrect += info["month_var"]

            if bracketsNotParens:
                incorrect += "]"
            else:
                incorrect += ")"

            incorrect += " * " + info["helper_function"]

            if bracketsNotParens:
                incorrect += "["
            else:
                incorrect += "("

            if wrongVariable:
                incorrect += wrongVariableChoice
            else:
                incorrect += info["month_var"]

            if bracketsNotParens:
                incorrect += "]"
            else:
                incorrect += ")"

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




def binary_search_condition(info, num_answers):
    
    #should be: if (celsius > temp_target) {
    #    m_low = m_mid;
    #} else {
    #    m_high = m_mid;
    #}

    # info should look like this: 
    # { 
    #     "celsius_var": "celsius",
    #     "temp_target_var": "temp_target",
    #     "m_low_var": "m_low",
    #     "m_high_var": "m_high",
    #     "m_mid_var": "m_mid"
    # }

    # ways to mess this up
    # assign to m_mid instead of m_low and m_high
    # confuse m_mid with either m_low or m_high (the one that's not being assigned to)
    # re-declare m_low and m_high
    # use "else if" instead of "else"
    # use < rather than > (but don't change anything else)

    # make empty answers list
    answers = []

    # make correct answer
    correct =  "        if (" + info["celsius_var"] + " > " + info["temp_target_var"] + ") {\n"
    correct += "            " + info["m_low_var"] + " = " + info["m_mid_var"] + ";\n"
    correct += "        } else {\n"
    correct += "            " + info["m_high_var"] + " = " + info["m_mid_var"] + ";\n"
    correct += "        }"
    answers.append({'tag': 'true', 'ans': correct})

    # construct wrong answers
    while len(answers) < num_answers:

        validWrongAnswer = False
        while validWrongAnswer == False:

            # pick some random wrongness
            randomNum = random.randrange(0,6) #increase the upper range to make this happen less often
            mMidNotMLow = randomNum == 0

            randomNum = random.randrange(0,10) #increase the upper range to make this happen less often
            mMidNotMHigh = randomNum == 0

            randomNum = random.randrange(0,6) #increase the upper range to make this happen less often
            confuseMMid1 = randomNum == 0

            randomNum = random.randrange(0,6) #increase the upper range to make this happen less often
            confuseMMid2 = randomNum == 0

            randomNum = random.randrange(0,10) #increase the upper range to make this happen less often
            elseIf = randomNum == 0

            randomNum = random.randrange(0,10) #increase the upper range to make this happen less often
            redeclare = randomNum == 0

            randomNum = random.randrange(0,6) #increase the upper range to make this happen less often
            wrongOperator = randomNum == 0

            if wrongOperator: #only one thing changes

                incorrect =  "        if (" + info["celsius_var"] + " < " + info["temp_target_var"] + ") {\n"
                incorrect += "            " + info["m_low_var"] + " = " + info["m_mid_var"] + ";\n"
                incorrect += "        } else {\n"
                incorrect += "            " + info["m_high_var"] + " = " + info["m_mid_var"] + ";\n"
                incorrect += "        }"

            else: #not wrongOperator

                # start constructing the answer
                incorrect =  "        if (" + info["celsius_var"] + " > " + info["temp_target_var"] + ") {\n"
                incorrect += "            "

                if redeclare:
                    incorrect += "double "
                
                if mMidNotMLow:
                    incorrect += info["m_mid_var"]
                else:
                    incorrect += info["m_low_var"]

                incorrect += " = "

                if confuseMMid1:
                    incorrect += info["m_high_var"]
                else:
                    incorrect += info["m_mid_var"]

                incorrect += ";\n"

                if elseIf:
                    incorrect += "        } else if {\n"
                else:
                    incorrect += "        } else {\n"

                incorrect += "            "

                if redeclare:
                    incorrect += "double "

                if mMidNotMHigh:
                    incorrect += info["m_mid_var"]
                else:
                    incorrect += info["m_high_var"]

                incorrect += " = "

                if confuseMMid2:
                    incorrect += info["m_low_var"]
                else:
                    incorrect += info["m_mid_var"]

                incorrect += ";\n"
                incorrect += "        }"

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

