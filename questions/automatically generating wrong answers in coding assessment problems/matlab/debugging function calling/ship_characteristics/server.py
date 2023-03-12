import random
import string
import copy

# ----------------------------------------------------------------
# PROBLEM DESCRIPTION
# ----------------------------------------------------------------

# This is a debugging problem about calling functions. Students need to both correctly choose the bug from a list of commonly seen bugs, AND correctly select how to fix the bug.

# This problem is about simulating ship characteristics. 


def generate(data):

    # ----------------------------------------------------------------
    # IMPORT FUNCTIONS FOR GENERATING ANSWERS
    # ----------------------------------------------------------------


    import sys
    sys.path.append(data["options"]["server_files_course_path"])
    from generatingAnswers import make_return_variables
    from generatingAnswers import make_parameters
    from generatingAnswers import buggy_func_call_answers



    # get characters to use to generate random "id numbers" later
    letters = string.ascii_letters



    # ------------------------------------------------------------------------
    # DATA FOR THE PROBLEM -- JUST CHANGE THIS PART TO MAKE A NEW PROBLEM! :)
    # ------------------------------------------------------------------------

    # this is a super short "what's this function about" phrase 
    function_topic = "simulating ship characteristics"

    # Here's a bunch of reasonable names we could pick for this function
    functionName = ["simShips","generateShips","ships","shipSim","findShips"]
    random.shuffle(functionName)

    # Here's a bunch of sets of parameters/arguments to choose from later
    p_and_a_set_1 = [
        {
        "parameter": "vol",
        "argument": "V",
        "description": "a vector of possible ship volumes",
        "argument_value": "[" + str(round(random.uniform(2,8)*1.17,2)) + "E4 : 1.0E4 : " + str(round(random.uniform(2,8)*1.17,2))+ "E5]"
        },
        {
        "parameter": "V",
        "argument": "vol",
        "description": "a vector of possible ship volumes",
        "argument_value": "[" + str(round(random.uniform(2,8)*1.17,2)) + "E4 : 1.0E4 : " + str(round(random.uniform(2,8)*1.17,2))+ "E5]"
        },
        {
        "parameter": "weight",
        "argument": "W",
        "description": "a vector of possible ship weights",
        "argument_value": "[" + str(round(random.uniform(2,8)*1.17,2)) + "E4 : 1.0E4 : " + str(round(random.uniform(2,8)*1.17,2))+ "E5]"
        },
        {
        "parameter": "W",
        "argument": "weight",
        "description": "a vector of possible ship weights",
        "argument_value": "[" + str(round(random.uniform(2,8)*1.17,2)) + "E4 : 1.0E4 : " + str(round(random.uniform(2,8)*1.17,2))+ "E5]"
        }
    ]
    p_and_a_set_2 = [
        {
        "parameter": "depth",
        "argument": "D",
        "description": "a vector of possible ship depths",
        "argument_value": "[" + str(round(random.uniform(2,4)*1.17,2)) + " : 0.1 : " + str(round(random.uniform(7,8)*1.17,2))+ "]"
        },
        {
        "parameter": "D",
        "argument": "depth",
        "description": "a vector of possible ship depths",
        "argument_value": "[" + str(round(random.uniform(2,4)*1.17,2)) + " : 0.1 : " + str(round(random.uniform(7,8)*1.17,2))+ "]"
        },
        {
        "parameter": "draft",
        "argument": "T",
        "description": "a vector of possible ship drafts",
        "argument_value": "[" + str(round(random.uniform(2,4)*1.17,2)) + " : 0.1 : " + str(round(random.uniform(7,8)*1.17,2))+ "]"
        },
        {
        "parameter": "T",
        "argument": "draft",
        "description": "a vector of possible ship drafts",
        "argument_value": "[" + str(round(random.uniform(2,4)*1.17,2)) + " : 0.1 : " + str(round(random.uniform(7,8)*1.17,2))+ "]"
        }
    ]
    p_and_a_set_3 = [
        {
        "parameter": "beam",
        "argument": "B",
        "description": "a vector of possible ship beams (the *beam* of a ship is the width of the ship at its widest point)",
        "argument_value": "[" + str(round(random.uniform(3,5)*1.17,2)) + " : 0.1 : " + str(round(random.uniform(10,20)*1.17,2))+ "]"
        },
        {
        "parameter": "B",
        "argument": "beam",
        "description": "a vector of possible ship beams (the *beam* of a ship is the width of the ship at its widest point)",
        "argument_value": "[" + str(round(random.uniform(3,5)*1.17,2)) + " : 0.1 : " + str(round(random.uniform(10,20)*1.17,2))+ "]"
        },
        {
        "parameter": "len",
        "argument": "L",
        "description": "a vector of possible ship lengths",
        "argument_value": "[" + str(round(random.uniform(20,40)*1.17,2)) + " : 0.5 : " + str(round(random.uniform(80,150)*1.17,2))+ "]"
        },
        {
        "parameter": "L",
        "argument": "len",
        "description": "a vector of possible ship lengths",
        "argument_value": "[" + str(round(random.uniform(20,40)*1.17,2)) + " : 0.5 : " + str(round(random.uniform(80,150)*1.17,2))+ "]"
        }
    ]
    p_and_a_set_4 = [
        {
        "parameter": "C_B",
        "argument": "blockCoef",
        "description": "a vector of possible ship block coefficients",
        "argument_value": "[" + str(round(random.uniform(4,5)/10,2)) + " : 0.05 : " + str(round(random.uniform(7,9)/10,2))+ "]"
        },
        {
        "parameter": "C_W",
        "argument": "wpCoef",
        "description": "a vector of possible ship waterplane coefficients",
        "argument_value": "[" + str(round(random.uniform(4,5)/10,2)) + " : 0.05 : " + str(round(random.uniform(7,9)/10,2))+ "]"
        },
                {
        "parameter": "A_W",
        "argument": "wpArea",
        "description": "a vector of possible ship waterplane areas",
        "argument_value": "[" + str(round(random.uniform(2,8)*1.17,2)) + "E4 : 1.0E4 : " + str(round(random.uniform(2,8)*1.17,2))+ "E5]"
        },
        {
        "parameter": "I_L",
        "argument": "longInertia",
        "description": "a vector of possible ship longitudinal centers of inertia",
        "argument_value": "[" + str(round(random.uniform(2,8)*1.17,2)) + "E4 : 1.0E4 : " + str(round(random.uniform(2,8)*1.17,2))+ "E5]"
        }
    ]
    p_and_a_set_5 = [
        {
        "parameter": "LCF",
        "argument": "longCF",
        "description": "a vector of possible ship longitudinal centers of flotation",
        "argument_value": "[" + str(round(random.uniform(20,40)*1.17,2)) + " : 0.5 : " + str(round(random.uniform(80,150)*1.17,2))+ "]"
        },
        {
        "parameter": "LCB",
        "argument": "longCB",
        "description": "a vector of possible ship longitudinal centers of buoyancy",
        "argument_value": "[" + str(round(random.uniform(20,40)*1.17,2)) + " : 0.5 : " + str(round(random.uniform(80,150)*1.17,2))+ "]"
        },
        {
        "parameter": "VCB",
        "argument": "vertCB",
        "description": "a vector of possible ship vertical centers of buoyancy",
        "argument_value": "[" + str(round(random.uniform(2,4)*1.17,2)) + " : 0.1 : " + str(round(random.uniform(7,8)*1.17,2))+ "]"
        }
    ]


    # Here's a bunch of return variables to choose from later
    # For this type of question, let the assignment variables be the same
    # name as the return variables, since this is a "Level 1" type question
    return_variable_set_1 = [
        {
            "name": "allShips",
            "description": "a table of the characteristics of all of the ships generated in the simulation",
            "assignment": "allShips",
        },
        {
            "name": "ships",
            "description": "a table of the characteristics of all of the ships generated in the simulation",
            "assignment": "ships",
        }
    ]
    return_variable_set_2 = [
        {
            "name": "viableShips",
            "description": "a table of the characteristics of the ships that qualify as viable",
            "assignment": "viableShips",
        },
        {
            "name": "shipsViable",
            "description": "a table of the characteristics of the ships that qualify as viable",
            "assignment": "shipsViable",
        }
    ]
    return_variable_set_3 = [
        {
            "name": "summary",
            "description": "a table containing summary statistics of the simulation",
            "assignment": "summary",
        },
        {
            "name": "report",
            "description": "a table containing summary statistics of the simulation",
            "assignment": "report",
        },
        {
            "name": "statsReport",
            "description": "a table containing summary statistics of the simulation",
            "assignment": "statsReport",
        }
    ]






    # ----------------------------------------------------------------
    # CREATE THE PROBLEM -- DON'T CHANGE ANYTHING FROM HERE ON DOWN
    # ----------------------------------------------------------------


    # shuffle all the specified information above; it helps with randomizing the problem variants
    random.shuffle(functionName)

    # shuffle the parameters/arguments and combine them into one set
    random.shuffle(p_and_a_set_1)
    random.shuffle(p_and_a_set_2)
    random.shuffle(p_and_a_set_3)
    random.shuffle(p_and_a_set_4)
    random.shuffle(p_and_a_set_5)
    p_and_a_set_all = [
        p_and_a_set_1,
        p_and_a_set_2,
        p_and_a_set_3,
        p_and_a_set_4,
        p_and_a_set_5
    ]
    random.shuffle(p_and_a_set_all)

    # shuffle the random variables and combine them into one set
    random.shuffle(return_variable_set_1)
    random.shuffle(return_variable_set_2)
    random.shuffle(return_variable_set_3)
    return_variable_set_all = [return_variable_set_1,return_variable_set_2,return_variable_set_3]
    random.shuffle(return_variable_set_all)



    # Determine number of parameters and return variables for this question variant
    numParams = random.randint(2,4)
    numReturnVars = random.randint(2,3)

    # Create the set of parameters and return variables
    parameter_set = []
    i = 0
    while i < numParams:
        parameter_set.append(p_and_a_set_all[i][0])
        i += 1

    # shuffle the parameters
    random.shuffle(parameter_set)

    # now get the randomly chosen return variables
    return_variable_set = []
    i = 0
    while i < numReturnVars:
        return_variable_set.append(return_variable_set_all[i][0])
        i += 1

    # shuffle the return variables
    random.shuffle(return_variable_set)




    # Create a scenario so that random function headers can be created
    # all the ways to make variants have already been shuffled, so select the first one 
    # (or first N) of each thing

    # set up the parameter/argument information
    parameters = []
    parameter_descriptions = []
    arguments = []
    argument_values = []
    j = 0
    while j < len(parameter_set):
        parameters.append(parameter_set[j]["parameter"])
        parameter_descriptions.append(parameter_set[j]["description"])
        arguments.append(parameter_set[j]["argument"])
        argument_values.append(parameter_set[j]["argument_value"])
        j += 1

    # set up the return variable information
    return_variables = []
    return_variable_descriptions = []
    assignments = []
    j = 0
    while j < len(return_variable_set):
        return_variables.append(return_variable_set[j]["name"])
        return_variable_descriptions.append(return_variable_set[j]["description"])
        assignments.append(return_variable_set[j]["assignment"])
        j += 1


    scenarios = [
        {
            "function_name": functionName[0],
            "topic": function_topic,
            "parameters": parameters,
            "parameter_descriptions": parameter_descriptions,
            "return_variables": return_variables,
            "return_variable_descriptions": return_variable_descriptions,
            "arguments": arguments,
            "argument_values": argument_values,
            "assignments": assignments,
        }
    ]





    # Get the buggy answers
    buggy_answers = buggy_func_call_answers(scenarios[0])



    



    # ----------------------------------------------------------------
    # SAVE THE DATA FOR PRAIRIELEARN TO USE
    # ----------------------------------------------------------------

    # function description
    data['params']['functionName'] = scenarios[0]["function_name"]
    data['params']['topic'] = scenarios[0]["topic"]

    # create the parameter list of descriptions and the code to declare the arguments
    j = 0
    parameterList = ""
    argumentList = ""
    while j < numParams:
        parameterList += str(j+1) + ". " + scenarios[0]["parameter_descriptions"][j] + " \r\n"
        argumentList += scenarios[0]["arguments"][j] + " = " + scenarios[0]["argument_values"][j] + "; \r\n"
        j += 1

    # create the return value list of descriptions
    j = 0
    returnVarList = ""
    while j < numReturnVars:
        returnVarList += str(j+1) + ". " + scenarios[0]["return_variable_descriptions"][j] + " \r\n"
        j += 1

    data['params']['parameterList'] = parameterList
    data['params']['argumentList'] = argumentList
    data['params']['returnVarList'] = returnVarList

    # create the function header
    functionHeader = "function "
    functionHeader += make_return_variables(scenarios[0]["return_variables"],scenarios[0]["parameters"],True)
    functionHeader += " = " + scenarios[0]["function_name"]
    functionHeader += make_parameters(scenarios[0]["return_variables"],scenarios[0]["parameters"],True)

    data['params']['functionHeader'] = functionHeader


    # list all the bugs
    ALL_BUGS  = []
    i = 0
    while i < len(buggy_answers):
        ALL_BUGS.append({'tag': 'false', 'ans': buggy_answers[i]["bug"]})
        i += 1


    # list all the fixes
    ALL_FIXES  = []
    i = 0
    while i < len(buggy_answers):
        ALL_FIXES.append({'tag': 'false', 'ans': buggy_answers[i]["fix"]})
        i += 1



    # shuffle random integers to correspond to the different wrong calls
    index_numbers = []
    i = 0
    while i < len(buggy_answers):
        index_numbers.append(i)
        i += 1
    random.shuffle(index_numbers)



    # FUNCTION CALL 1
    data['params']['call1'] = buggy_answers[index_numbers[0]]["ans"]
    q1bugs = copy.deepcopy(ALL_BUGS)
    q1bugs[index_numbers[0]]['tag'] = 'true'
    data['params']['bugs1'] = q1bugs
    q1fixes = copy.deepcopy(ALL_FIXES)
    q1fixes[index_numbers[0]]['tag'] = 'true'
    data['params']['fixes1'] = q1fixes

    # FUNCTION CALL 2
    data['params']['call2'] = buggy_answers[index_numbers[1]]["ans"]
    q2bugs = copy.deepcopy(ALL_BUGS)
    q2bugs[index_numbers[1]]['tag'] = 'true'
    data['params']['bugs2'] = q2bugs
    q2fixes = copy.deepcopy(ALL_FIXES)
    q2fixes[index_numbers[1]]['tag'] = 'true'
    data['params']['fixes2'] = q2fixes

    # FUNCTION CALL 3
    data['params']['call3'] = buggy_answers[index_numbers[2]]["ans"]
    q3bugs = copy.deepcopy(ALL_BUGS)
    q3bugs[index_numbers[2]]['tag'] = 'true'
    data['params']['bugs3'] = q3bugs
    q3fixes = copy.deepcopy(ALL_FIXES)
    q3fixes[index_numbers[2]]['tag'] = 'true'
    data['params']['fixes3'] = q3fixes

    # # FUNCTION CALL 4
    # data['params']['call4'] = buggy_answers[index_numbers[3]]["ans"]
    # q4bugs = copy.deepcopy(ALL_BUGS)
    # q4bugs[index_numbers[3]]['tag'] = 'true'
    # data['params']['bugs4'] = q4bugs
    # q4fixes = copy.deepcopy(ALL_FIXES)
    # q4fixes[index_numbers[3]]['tag'] = 'true'
    # data['params']['fixes4'] = q4fixes



