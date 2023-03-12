import random
import string
import copy

# ----------------------------------------------------------------
# PROBLEM DESCRIPTION
# ----------------------------------------------------------------

# This is a debugging problem about calling functions. Students need to both correctly choose the bug from a list of commonly seen bugs, AND correctly select how to fix the bug.

# This problem is about 3D printing. The original function was part of a multiple choice problem in either the F20 or W21 exam. Laura can't remember :) 


def generate(data):

    # ----------------------------------------------------------------
    # IMPORT FUNCTIONS FOR GENERATING ANSWERS
    # ----------------------------------------------------------------


    import sys
    sys.path.append(data["options"]["server_files_course_path"])
    from generatingAnswersCplusplus import make_parameters
    from generatingAnswersCplusplus import buggy_func_call_answers



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

    # These are pass by CONST reference sets
    p_and_a_set_1 = [
        {
        "name": "vol",
        "argument": "V",
        "description": "a vector of possible ship volumes",
        "argument_value": "TBF",
        "type": "vector<double>",
        "pass_by_reference": "const",
        },
        {
        "name": "V",
        "argument": "vol",
        "description": "a vector of possible ship volumes",
        "argument_value": "TBF",
        "type": "vector<double>",
        "pass_by_reference": "const",
        },
        {
        "name": "weight",
        "argument": "W",
        "description": "a vector of possible ship weights",
        "argument_value": "TBF",
        "type": "vector<double>",
        "pass_by_reference": "const",
        },
        {
        "name": "W",
        "argument": "weight",
        "description": "a vector of possible ship weights",
        "argument_value": "TBF",
        "type": "vector<double>",
        "pass_by_reference": "const",
        }
    ]
    p_and_a_set_2 = [
        {
        "name": "depth",
        "argument": "D",
        "description": "a vector of possible ship depths",
        "argument_value": "TBF",
        "type": "vector<double>",
        "pass_by_reference": "const",
        },
        {
        "name": "D",
        "argument": "depth",
        "description": "a vector of possible ship depths",
        "argument_value": "TBF",
        "type": "vector<double>",
        "pass_by_reference": "const",
        },
        {
        "name": "draft",
        "argument": "T",
        "description": "a vector of possible ship drafts",
        "argument_value": "TBF",
        "type": "vector<double>",
        "pass_by_reference": "const",
        },
        {
        "name": "T",
        "argument": "draft",
        "description": "a vector of possible ship drafts",
        "argument_value": "TBF",
        "type": "vector<double>",
        "pass_by_reference": "const",
        }
    ]
    p_and_a_set_3 = [
        {
        "name": "beam",
        "argument": "B",
        "description": "a vector of possible ship beams (the *beam* of a ship is the width of the ship at its widest point)",
        "argument_value": "TBF",
        "type": "vector<double>",
        "pass_by_reference": "const",
        },
        {
        "name": "B",
        "argument": "beam",
        "description": "a vector of possible ship beams (the *beam* of a ship is the width of the ship at its widest point)",
        "argument_value": "TBF",
        "type": "vector<double>",
        "pass_by_reference": "const",
        },
        {
        "name": "len",
        "argument": "L",
        "description": "a vector of possible ship lengths",
        "argument_value": "TBF",
        "type": "vector<double>",
        "pass_by_reference": "const",
        },
        {
        "name": "L",
        "argument": "len",
        "description": "a vector of possible ship lengths",
        "argument_value": "TBF",
        "type": "vector<double>",
        "pass_by_reference": "const",
        }
    ]
    p_and_a_set_4 = [
        {
        "name": "C_B",
        "argument": "blockCoef",
        "description": "a vector of possible ship block coefficients",
        "argument_value": "TBF",
        "type": "vector<double>",
        "pass_by_reference": "const",
        },
        {
        "name": "C_W",
        "argument": "wpCoef",
        "description": "a vector of possible ship waterplane coefficients",
        "argument_value": "TBF",
        "type": "vector<double>",
        "pass_by_reference": "const",
        },
                {
        "name": "A_W",
        "argument": "wpArea",
        "description": "a vector of possible ship waterplane areas",
        "argument_value": "TBF",
        "type": "vector<double>",
        "pass_by_reference": "const",
        },
        {
        "name": "I_L",
        "argument": "longInertia",
        "description": "a vector of possible ship longitudinal centers of inertia",
        "argument_value": "TBF",
        "type": "vector<double>",
        "pass_by_reference": "const",
        }
    ]
    p_and_a_set_5 = [
        {
        "name": "LCF",
        "argument": "longCF",
        "description": "a vector of possible ship longitudinal centers of flotation",
        "argument_value": "TBF",
        "type": "vector<double>",
        "pass_by_reference": "const",
        },
        {
        "name": "LCB",
        "argument": "longCB",
        "description": "a vector of possible ship longitudinal centers of buoyancy",
        "argument_value": "TBF",
        "type": "vector<double>",
        "pass_by_reference": "const",
        },
        {
        "name": "VCB",
        "argument": "vertCB",
        "description": "a vector of possible ship vertical centers of buoyancy",
        "argument_value": "TBF",
        "type": "vector<double>",
        "pass_by_reference": "const",
        }
    ]


    # These are a bunch of pass by reference variables
    return_variable_set_1 = [
        {
            "name": "allShips",
            "description": "a vector of structs of the characteristics of all of the ships generated in the simulation (starts empty, and then the function \"fills up\" the vector)",
            "argument": "allShips",
            "argument_value": "",
            "type": "vector<ShipData>",
            "pass_by_reference": True,
        },
        {
            "name": "ships",
            "description": "a vector of structs of the characteristics of all of the ships generated in the simulation (starts empty, and then the function \"fills up\" the vector)",
            "argument": "ships",
            "argument_value": "",
            "type": "vector<ShipData>",
            "pass_by_reference": True,
        }
    ]
    return_variable_set_2 = [
        {
            "name": "viableShips",
            "description": "a vector of structs of the characteristics of the ships that qualify as viable (starts empty, and then the function \"fills up\" the vector)",
            "argument": "viableShips",
            "argument_value": "",
            "type": "vector<ShipData>",
            "pass_by_reference": True,
        },
        {
            "name": "shipsViable",
            "description": "a vector of structs of the characteristics of the ships that qualify as viable (starts empty, and then the function \"fills up\" the vector)",
            "argument": "shipsViable",
            "argument_value": "",
            "type": "vector<ShipData>",
            "pass_by_reference": True,
        }
    ]
    return_variable_set_3 = [
        {
            "name": "summary",
            "description": "a struct containing summary statistics of the simulation (starts empty, and then the function \"fills up\" the struct)",
            "argument": "summary",
            "argument_value": "",
            "type": "Summary",
            "pass_by_reference": True,
        },
        {
            "name": "report",
            "description": "a struct containing summary statistics of the simulation (starts empty, and then the function \"fills up\" the struct)",
            "argument": "report",
            "argument_value": "",
            "type": "Summary",
            "pass_by_reference": True,
        },
        {
            "name": "statsReport",
            "description": "a struct containing summary statistics of the simulation (starts empty, and then the function \"fills up\" the struct)",
            "argument": "statsReport",
            "argument_value": "",
            "type": "Summary",
            "pass_by_reference": True,
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

    p_and_a_set_all_PBCR = [
        p_and_a_set_1,
        p_and_a_set_2,
        p_and_a_set_3,
        p_and_a_set_4,
        p_and_a_set_5
    ]
    random.shuffle(p_and_a_set_all_PBCR)


    # shuffle the random variables and combine them into one set
    random.shuffle(return_variable_set_1)
    random.shuffle(return_variable_set_2)
    random.shuffle(return_variable_set_3)
    p_and_a_set_all_PBR = [
        return_variable_set_1,
        return_variable_set_2,
        return_variable_set_3
    ]
    random.shuffle(p_and_a_set_all_PBR)



    # Determine number of parameters and return variables for this question variant
    numParamsPBCR = random.randint(1,2)
    numParamsPBR = random.randint(1,1)


    # Create the set of parameters and return variables
    parameter_set = []
    i = 0
    while i < numParamsPBCR:
        parameter_set.append(p_and_a_set_all_PBCR[i][0])
        i += 1
    i = 0
    while i < numParamsPBR:
        parameter_set.append(p_and_a_set_all_PBR[i][0])
        i += 1


    # shuffle the parameters
    random.shuffle(parameter_set)






    # Create a scenario so that random function headers can be created
    # all the ways to make variants have already been shuffled, so select the first one 
    # (or first N) of each thing

    # set up the parameter/argument information
    parameters = []
    parameter_types = []
    parameter_descriptions = []
    arguments = []
    argument_values = []
    j = 0
    while j < len(parameter_set):
        parameters.append(parameter_set[j]["name"])
        parameter_types.append(parameter_set[j]["type"])
        parameter_descriptions.append(parameter_set[j]["description"])
        arguments.append(parameter_set[j]["argument"])
        argument_values.append(parameter_set[j]["argument_value"])
        j += 1

    # set up the return variable information
    return_variables = []
    return_variable_types = []
    return_variable_descriptions = []
    assignments = []
    j = 0
    functionType = "void" # assume there are no return values and this is a void function
    # while j < len(return_variable_set):
    #     return_variables.append(return_variable_set[j]["name"])
    #     return_variable_types.append(return_variable_set[j]["type"])
    #     return_variable_descriptions.append(return_variable_set[j]["description"])
    #     assignments.append(return_variable_set[j]["assignment"])
    #     functionType = return_variable_set[j]["type"] # if there is a return value, change the function type
    #     j += 1
    numReturnVars = 0

    scenarios = [
        {
            "function_name": functionName[0],
            "function_type": functionType,
            "topic": function_topic,
            "parameters": parameter_set,
            "parameter_descriptions": parameter_descriptions,
            "return_variables": [],
            "return_variable_descriptions": return_variable_descriptions,
            "arguments": arguments,
            "argument_values": argument_values,
            "assignments": assignments,
            "distractor_functions": ["func", "another_func" ],
            "distractor_types":[
                "string","char","int","double","bool", "vector", "summary", "ShipData", "vector<Summary>"
            ],
            "distractor_rvs":[
                "x",
                "isValid" 
            ]
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
    while j < len(parameter_set):
        parameterList += str(j+1) + ". " + scenarios[0]["parameter_descriptions"][j] + " \r\n"
        if scenarios[0]["argument_values"][j] == "": #declare the variable ONLY
            argumentList += scenarios[0]["parameters"][j]["type"] + " " + scenarios[0]["arguments"][j] + "; \r\n"
        elif scenarios[0]["argument_values"][j] == "TBF": #initialize with comment of "code to initialize the vector"
            argumentList += scenarios[0]["parameters"][j]["type"] + " " + scenarios[0]["arguments"][j] + " = //code that initializes the vector  \r\n"
        else:
            argumentList += scenarios[0]["parameters"][j]["type"] + " " + scenarios[0]["arguments"][j] + " = " + scenarios[0]["argument_values"][j] + "; \r\n"
        j += 1

    # create the return value list of descriptions
    j = 0
    returnVarList = ""


    data['params']['parameterList'] = parameterList
    data['params']['argumentList'] = argumentList
    data['params']['returnVarList'] = returnVarList

    # create the function header
    functionHeader = scenarios[0]["function_type"] + " "
    functionHeader += scenarios[0]["function_name"]
    functionHeader += make_parameters(scenarios[0],True)
    functionHeader += " {"

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



    # Create the questions, but need to coordinate the void vs. non-void functions

    i = 1
    numProblems = 2
    iBug = 0
    while i <= numProblems:
        
        bug = buggy_answers[index_numbers[iBug]]["bug"]
        if numReturnVars == 0 and bug == "forgotten to store the return value from a non-void function":
            iBug += 1
            continue
        elif numReturnVars == 1 and bug == "tried to store a return value from a void function":
            iBug += 1
            continue
        else:
            questionName = "call" + str(i)
            data['params'][questionName] = buggy_answers[index_numbers[iBug]]["ans"]
            bugs = copy.deepcopy(ALL_BUGS)
            bugs[index_numbers[iBug]]['tag'] = 'true'
            bugsAnswers = "bugs" + str(i)
            data['params'][bugsAnswers] = bugs
            fixes = copy.deepcopy(ALL_FIXES)
            fixes[index_numbers[iBug]]['tag'] = 'true'
            fixesAnswers = "fixes" + str(i)
            data['params'][fixesAnswers] = fixes
            iBug += 1
            i += 1



    # # FUNCTION CALL 1
    # data['params']['call1'] = buggy_answers[index_numbers[0]]["ans"]
    # q1bugs = copy.deepcopy(ALL_BUGS)
    # q1bugs[index_numbers[0]]['tag'] = 'true'
    # data['params']['bugs1'] = q1bugs
    # q1fixes = copy.deepcopy(ALL_FIXES)
    # q1fixes[index_numbers[0]]['tag'] = 'true'
    # data['params']['fixes1'] = q1fixes

    # # FUNCTION CALL 2
    # data['params']['call2'] = buggy_answers[index_numbers[1]]["ans"]
    # q2bugs = copy.deepcopy(ALL_BUGS)
    # q2bugs[index_numbers[1]]['tag'] = 'true'
    # data['params']['bugs2'] = q2bugs
    # q2fixes = copy.deepcopy(ALL_FIXES)
    # q2fixes[index_numbers[1]]['tag'] = 'true'
    # data['params']['fixes2'] = q2fixes

    # # FUNCTION CALL 3
    # data['params']['call3'] = buggy_answers[index_numbers[2]]["ans"]
    # q3bugs = copy.deepcopy(ALL_BUGS)
    # q3bugs[index_numbers[2]]['tag'] = 'true'
    # data['params']['bugs3'] = q3bugs
    # q3fixes = copy.deepcopy(ALL_FIXES)
    # q3fixes[index_numbers[2]]['tag'] = 'true'
    # data['params']['fixes3'] = q3fixes

    # # FUNCTION CALL 4
    # data['params']['call4'] = buggy_answers[index_numbers[3]]["ans"]
    # q4bugs = copy.deepcopy(ALL_BUGS)
    # q4bugs[index_numbers[3]]['tag'] = 'true'
    # data['params']['bugs4'] = q4bugs
    # q4fixes = copy.deepcopy(ALL_FIXES)
    # q4fixes[index_numbers[3]]['tag'] = 'true'
    # data['params']['fixes4'] = q4fixes



