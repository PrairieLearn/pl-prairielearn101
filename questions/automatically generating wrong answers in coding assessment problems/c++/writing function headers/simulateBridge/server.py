import random
import string

# ----------------------------------------------------------------
# PROBLEM DESCRIPTION
# ----------------------------------------------------------------

# This is a writing a function header problem. There are at least 
# three parameters: pass by value, pass by reference, pass by 
# const reference. 

# This problem is about simulating bridges. It was orginally a helper 
# function in the driver problem from the F20 MATLAB exam:

# function [cars, wind] = simulate(yield_s, tensile_s, n_sim)  
#   % SIMULATE Conducts simulations of the bridge according to  
#   % its tensile strength and yield strength by placing the  
#   % bridge under high load (lots of cars and high wind speeds).  
#   % The number of simulations conducted is determined by n_sim.  
#   % Two vectors are returned, containing an entry for each  
#   % simulation. The vectors represent the number of cars and  
#   % the wind speed at which the bridge failed in the simulation.  
#
#   % IMPLEMENTATION NOT SHOWN 
# end


def generate(data):


    # ----------------------------------------------------------------
    # IMPORT FUNCTIONS FOR GENERATING ANSWERS
    # ----------------------------------------------------------------


    import sys
    sys.path.append(data["options"]["server_files_course_path"])
    from generatingAnswersCplusplus import func_header_answers


    # get characters to use to generate random "id numbers" later
    letters = string.ascii_letters


    # ------------------------------------------------------------------------
    # DATA FOR THE PROBLEM -- JUST CHANGE THIS PART TO MAKE A NEW PROBLEM! :)
    # ------------------------------------------------------------------------

    # here are some possible function names 
    functionName = ["simulate","simBridge"]
    functionType = "void"
    functionTopic = "simulates bridge failure"

    # Here are the required sets of parameters and arguments
    p_and_a_set_reqd_1 = [
        {
        "name": "n_sim",
        "type": "int",
        "pass_by_reference": False,
        "argument": "N",
        "description": "the number of simulations to run",
        "argument_value": str(random.randrange(2,5) * 10000)
        },
        {
        "name": "N",
        "type": "int",
        "pass_by_reference": False,
        "argument": "n_sim",
        "description": "the number of simulations to run",
        "argument_value": str(random.randrange(2,5) * 10000)
        },
        {
        "name": "numSim",
        "type": "int",
        "pass_by_reference": False,
        "argument": "N_sim",
        "description": "the number of simulations to run",
        "argument_value": str(random.randrange(2,5) * 10000)
        }
    ]
    p_and_a_set_reqd_2 = [
        {
        "name": "type",
        "type": "string",
        "pass_by_reference": "const",
        "argument": "t",
        "description": "the type of steel to be used in the bridge",
        "argument_value": "\"" + ''.join(random.choice(letters) for i in range(5)) + "\""
        },
        {
        "name": "option",
        "type": "string",
        "pass_by_reference": "const",
        "argument": "opt",
        "description": "the option of steel to be used in the bridge",
        "argument_value": "\"" + ''.join(random.choice(letters) for i in range(5)) + "\""
        },
        {
        "name": "id",
        "type": "string",
        "pass_by_reference": "const",
        "argument": "ID_num",
        "description": "the ID of the steel to be used in the bridge",
        "argument_value": "\"" + ''.join(random.choice(letters) for i in range(5)) + "\""
        }
    ]

    # Here's a bunch more sets of parameters/arguments to choose from later
    p_and_a_set_1 = [
        {
        "name": "length",
        "type": "double",
        "pass_by_reference": False,
        "argument": "L",
        "description": "the length of the bridge",
        "argument_value": str(round(random.uniform(1,2)*100.17,2)) 
        },
        {
        "name": "L",
        "type": "double",
        "pass_by_reference": False,
        "argument": "length",
        "description": "the length of the bridge",
        "argument_value": str(round(random.uniform(1,2)*100.17,2))  
        },
        {
        "name": "len",
        "type": "double",
        "pass_by_reference": False,
        "argument": "length_bridge",
        "description": "the length of the bridge",
        "argument_value": str(round(random.uniform(1,2)*100.17,2)) 
        }
    ]
    
    p_and_a_set_2 = [
        {
        "name": "weight",
        "type": "double",
        "pass_by_reference": False,
        "argument": "W",
        "description": "the average weight of the vehicles crossing over the bridge",
        "argument_value": str(round(random.uniform(2,8)*1.17,2))
        },
        {
        "name": "mass",
        "type": "double",
        "pass_by_reference": False,
        "argument": "M",
        "description": "the average mass of the vehicles crossing over the bridge",
        "argument_value": str(round(random.uniform(2,8)*1.17,2))
        },
        {
        "name": "freq",
        "type": "double",
        "pass_by_reference": False,
        "argument": "F",
        "description": "the average frequency of vehicles crossing over the bridge",
        "argument_value": str(round(random.uniform(2,8)*1.17,2))
        }
    ]
    p_and_a_set_3 = [
        {
        "name": "width",
        "type": "double",
        "pass_by_reference": False,
        "argument": "w",
        "description": "the width of the bridge",
        "argument_value": str(round(random.uniform(2,8)*1.17,2))
        },
        {
        "name": "w",
        "type": "double",
        "pass_by_reference": False,
        "argument": "width",
        "description": "the width of the bridge",
        "argument_value": str(round(random.uniform(2,8)*1.17,2))
        },
        {
        "name": "height",
        "type": "double",
        "pass_by_reference": False,
        "argument": "h",
        "description": "the height of the bridge",
        "argument_value": str(round(random.uniform(2,8)*1.17,2))
        },
        {
        "name": "h",
        "type": "double",
        "pass_by_reference": False,
        "argument": "height",
        "description": "the height of the bridge",
        "argument_value": str(round(random.uniform(2,8)*1.17,2))
        }
    ]

    # Here's a bunch of pass by reference vectors to choose from
    return_variable_set_1 = [
        {
            "name": "cars",
            "type": "vector <double>",
            "pass_by_reference": True,
            "description": "a vector of the number of cars on the bridge when the bridge failed",
            "assignment": "cars",
            "argument_value": str(round(random.uniform(25,100))) + "<br>" + str(round(random.uniform(25,100))) + "<br>" + str(round(random.uniform(25,100))),
        },
        {
            "name": "numCars",
            "type": "vector <double>",
            "pass_by_reference": True,
            "description": "a vector of the number of cars on the bridge when the bridge failed",
            "assignment": "numCars",
            "argument_value": str(round(random.uniform(25,100))) + "<br>" + str(round(random.uniform(25,100))) + "<br>" + str(round(random.uniform(25,100))),
        },
        {
            "name": "nCars",
            "type": "vector <double>",
            "pass_by_reference": True,
            "description": "a vector of the number of cars on the bridge when the bridge failed",
            "assignment": "nCars",
            "argument_value": str(round(random.uniform(25,100))) + "<br>" + str(round(random.uniform(25,100))) + "<br>" + str(round(random.uniform(25,100))),
        },
        {
            "name": "N_cars",
            "type": "vector <double>",
            "pass_by_reference": True,
            "description": "a vector of the number of cars on the bridge when the bridge failed",
            "assignment": "N_cars",
            "argument_value": str(round(random.uniform(25,100))) + "<br>" + str(round(random.uniform(25,100))) + "<br>" + str(round(random.uniform(25,100))),
        }
    ]
    return_variable_set_2 = [
        {
            "name": "wind",
            "type": "vector <double>",
            "pass_by_reference": True,
            "description": "a vector of the wind speeds when the bridge failed",
            "assignment": "wind",
            "argument_value": str(round(random.uniform(1,2)*4.17,2)) + "<br>" + str(round(random.uniform(3,4)*4.17,2)) + "<br>" + str(round(random.uniform(5,6)*4.17,2)),
        },
        {
            "name": "windSpeed",
            "type": "vector <double>",
            "pass_by_reference": True,
            "description": "a vector of the wind speeds when the bridge failed",
            "assignment": "windSpeed",
            "argument_value": str(round(random.uniform(1,2)*4.17,2)) + "<br>" + str(round(random.uniform(3,4)*4.17,2)) + "<br>" + str(round(random.uniform(5,6)*4.17,2)),
        },
        {
            "name": "max_wind",
            "type": "vector <double>",
            "pass_by_reference": True,
            "description": "a vector of the wind speeds when the bridge failed",
            "assignment": "max_wind",
            "argument_value": str(round(random.uniform(1,2)*4.17,2)) + "<br>" + str(round(random.uniform(3,4)*4.17,2)) + "<br>" + str(round(random.uniform(5,6)*4.17,2)),
        },
        {
            "name": "maxWind",
            "type": "vector <double>",
            "pass_by_reference": True,
            "description": "a vector of the wind speeds when the bridge failed",
            "assignment": "maxWind",
            "argument_value": str(round(random.uniform(1,2)*4.17,2)) + "<br>" + str(round(random.uniform(3,4)*4.17,2)) + "<br>" + str(round(random.uniform(5,6)*4.17,2)),
        }
    ]
    return_variable_set_3 = [
        {
            "name": "direction",
            "type": "vector <double>",
            "pass_by_reference": True,
            "description": "a vector of the wind directions when the bridge failed",
            "assignment": "direction",
            "argument_value": str(round(random.uniform(0,225)*1.59,2)) + "<br>" + str(round(random.uniform(0,225)*1.59,2)) + "<br>" + str(round(random.uniform(0,225)*1.59,2)),
        },
        {
            "name": "windDirection",
            "type": "vector <double>",
            "pass_by_reference": True,
            "description": "a vector of the wind directions when the bridge failed",
            "assignment": "windDirection",
            "argument_value": str(round(random.uniform(0,225)*1.59,2)) + "<br>" + str(round(random.uniform(0,225)*1.59,2)) + "<br>" + str(round(random.uniform(0,225)*1.59,2)),
        },
        {
            "name": "max_wind",
            "type": "vector <double>",
            "pass_by_reference": True,
            "description": "a vector of the wind directions when the bridge failed",
            "assignment": "max_wind",
            "argument_value": str(round(random.uniform(0,225)*1.59,2)) + "<br>" + str(round(random.uniform(0,225)*1.59,2)) + "<br>" + str(round(random.uniform(0,225)*1.59,2)),
        },
        {
            "name": "wind_direction",
            "type": "vector <double>",
            "pass_by_reference": True,
            "description": "a vector of the wind directions when the bridge failed",
            "assignment": "wind_direction",
            "argument_value": str(round(random.uniform(0,225)*1.59,2)) + "<br>" + str(round(random.uniform(0,225)*1.59,2)) + "<br>" + str(round(random.uniform(0,225)*1.59,2)),
        }
    ]



    # ----------------------------------------------------------------
    # CREATE THE PROBLEM
    # ----------------------------------------------------------------

    # shuffle all the specified information above; it helps with randomizing the problem variants
    random.shuffle(functionName)

    # shuffle the parameters/arguments and combine them into one set
    random.shuffle(p_and_a_set_reqd_1)
    random.shuffle(p_and_a_set_reqd_2)
    random.shuffle(p_and_a_set_1)
    random.shuffle(p_and_a_set_2)
    random.shuffle(p_and_a_set_3)

    p_and_a_set_all = [
        p_and_a_set_1,
        p_and_a_set_2,
        p_and_a_set_3,
    ]
    random.shuffle(p_and_a_set_all)


    # shuffle the random variables and combine them into one set
    random.shuffle(return_variable_set_1)
    random.shuffle(return_variable_set_2)
    random.shuffle(return_variable_set_3)

    return_variable_set_all = [return_variable_set_1,return_variable_set_2,return_variable_set_3]
    random.shuffle(return_variable_set_all)

    # # Determine number of parameters and return variables for this question variant
    # numParams = random.randint(2,3)
    # numReturnVars = random.randint(2,3)



    # Create the set of parameters and return variables

    # first, add the required parameters
    parameter_set = []
    parameter_set.append(p_and_a_set_reqd_1[0])
    parameter_set.append(p_and_a_set_reqd_2[0])

    # then add another randomly chosen parameter
    parameter_set.append(p_and_a_set_all[0][0])

    # then add one of the pass by reference vectors
    parameter_set.append(return_variable_set_all[0][0])
    PBR_var_name = return_variable_set_all[0][0]["name"]

    # shuffle the parameters
    random.shuffle(parameter_set)

    # now get the randomly chosen return variables
    # SKIP FOR THIS VERSION -- MAKING THIS A VOID FUNCTION
    # return_variable_set = []
    # i = 0
    # while i < numReturnVars:
    #     return_variable_set.append(return_variable_set_all[i][0])
    #     i += 1
 
    # # shuffle the return variables
    # random.shuffle(return_variable_set)


    # Create a scenario so that random function headers can be created

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
        # arguments.append(parameter_set[j]["argument"])
        # argument_values.append(parameter_set[j]["argument_value"])
        j += 1

    # # set up the return variable information
    # return_variables = []
    # return_variable_types = []
    # return_variable_descriptions = []
    # assignments = []
    # j = 0
    # functionType = "void" # assume there are no return values and this is a void function
    # while j < len(return_variable_set):
    #     return_variables.append(return_variable_set[j]["name"])
    #     return_variable_types.append(return_variable_set[j]["type"])
    #     return_variable_descriptions.append(return_variable_set[j]["description"])
    #     assignments.append(return_variable_set[j]["assignment"])
    #     functionType = return_variable_set[j]["type"] # if there is a return value, change the function type
    #     j += 1


    scenarios = [
        {
            "function_name": functionName[0],
            "function_type": functionType,
            "topic": functionTopic,
            "parameters": parameter_set,
            "parameter_descriptions": parameter_descriptions,
            # "return_variables": return_variable_set,
            # "return_variable_descriptions": return_variable_descriptions,
            # "arguments": arguments,
            # "argument_values": argument_values,
            # "assignments": assignments,
            "distractor_functions": ["func", "another_func" ],
            "distractor_types":[
                "string","char","int","double","bool", 
            ],
            "distractor_rvs":[
                "x",
                "isReliable" 
            ]
        }
    ]


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
        parameterList += "<tr> <td>" + str(j+1) + " </td>" 
        parameterList += "<td> <code>" + scenarios[0]["parameters"][j]["name"] + "</code> </td>"
        parameterList += "<td> " + scenarios[0]["parameter_descriptions"][j] + " </td>"
        parameterList += "<td> <code>" + scenarios[0]["parameters"][j]["argument_value"] + "</code> </td>"
        if scenarios[0]["parameters"][j]["pass_by_reference"] == "const":
            parameterList += "<td> no </td> "
        elif scenarios[0]["parameters"][j]["pass_by_reference"]:
            parameterList += "<td> yes </td> "
        else: 
            parameterList += "<td> no </td> "
        parameterList += " </tr>\n"
        # argumentList += scenarios[0]["arguments"][j] + " = " + scenarios[0]["argument_values"][j] + "; \r\n"
        j += 1

    # create the return value list of descriptions
    # j = 0
    # returnVarList = ""
    # while j < numReturnVars:
    #     returnVarList += str(j+1) + ". " + scenarios[0]["return_variable_descriptions"][j] + " \r\n"
    #     j += 1

    data['params']['parameterList'] = parameterList
    # data['params']['argumentList'] = argumentList
    # data['params']['returnVarList'] = returnVarList

    # # create the function header
    # functionHeader = "function "
    # functionHeader += make_return_variables(scenarios[0]["return_variables"],scenarios[0]["parameters"],True)
    # functionHeader += " = " + scenarios[0]["function_name"]
    # functionHeader += make_parameters(scenarios[0]["return_variables"],scenarios[0]["parameters"],True)

    # data['params']['functionHeader'] = functionHeader


    data['params']['PBR_var'] = PBR_var_name


    # save the answer data for the problem
    answers = func_header_answers(scenarios[0],False,5)
    line_num = 'line'+str(1)
    data['params'][line_num] = answers