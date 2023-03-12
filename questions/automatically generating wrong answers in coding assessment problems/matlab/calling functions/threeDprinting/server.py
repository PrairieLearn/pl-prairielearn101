import random
import string

# ----------------------------------------------------------------
# PROBLEM DESCRIPTION
# ----------------------------------------------------------------

# This is a function calling problem. There are at least two parameters
# and at least two return variables for this function. 

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
    from generatingAnswers import make_return_variables
    from generatingAnswers import func_call_answers
    from generatingAnswers import make_arguments
    from generatingAnswers import func_header_answers
    from generatingAnswers import make_parameters

    # get characters to use to generate random "id numbers" later
    letters = string.ascii_letters


    # ------------------------------------------------------------------------
    # DATA FOR THE PROBLEM -- JUST CHANGE THIS PART TO MAKE A NEW PROBLEM! :)
    # ------------------------------------------------------------------------

    # here are some possible function names 
    functionName = ["printEstimate","costEstimate","approxCost","costCalculation","printCost"]

    # Here is one required set of parameters and arguments
    p_and_a_set_reqd = [
        {
        "parameter": "volume",
        "argument": "V",
        "description": "the volume of a 3D print",
        "argument_value": str(round(random.uniform(2,8)*1.17,2))
        },
        {
        "parameter": "volAmount",
        "argument": "V_total",
        "description": "the volume of a 3D print",
        "argument_value": str(round(random.uniform(2,8)*1.17,2))
        },
        {
        "parameter": "printVol",
        "argument": "printV",
        "description": "the volume of a 3D print",
        "argument_value": str(round(random.uniform(2,8)*1.17,2))
        }
    ]

    # Here's a bunch more sets of parameters/arguments to choose from later
    p_and_a_set_1 = [
        {
        "parameter": "filament_type",
        "argument": "t",
        "description": "the type of filament to be used in the 3D print",
        "argument_value": "\"" + ''.join(random.choice(letters) for i in range(5)) + "\""
        },
        {
        "parameter": "filament_option",
        "argument": "opt",
        "description": "the option of filament to be used in the 3D print",
        "argument_value": "\"" + ''.join(random.choice(letters) for i in range(5)) + "\""
        },
        {
        "parameter": "filament_id",
        "argument": "ID_num",
        "description": "the ID number of the filament to be used in the 3D print",
        "argument_value": "\"" + ''.join(random.choice(letters) for i in range(5)) + "\""
        }
    ]
    p_and_a_set_2 = [
        {
        "parameter": "weight",
        "argument": "W",
        "description": "the weight of the filament to be used in the 3D print",
        "argument_value": str(round(random.uniform(2,8)*1.17,2))
        },
        {
        "parameter": "mass",
        "argument": "M",
        "description": "the mass of filament to be used in the 3D print",
        "argument_value": str(round(random.uniform(2,8)*1.17,2))
        },
        {
        "parameter": "density",
        "argument": "D",
        "description": "the density of filament to be used in the 3D print",
        "argument_value": str(round(random.uniform(2,8)*1.17,2))
        }
    ]
    p_and_a_set_3 = [
        {
        "parameter": "machine_type",
        "argument": "machine_choice",
        "description": "the type of machine that will create the 3D print",
        "argument_value": str(round(random.uniform(2,8)*1.17,2))
        },
        {
        "parameter": "machine",
        "argument": "choice",
        "description": "the type of machine that will create the 3D print",
        "argument_value": str(round(random.uniform(2,8)*1.17,2))
        },
        {
        "parameter": "printer_type",
        "argument": "printer_choice",
        "description": "the type of printer that will create the 3D print",
        "argument_value": str(round(random.uniform(2,8)*1.17,2))
        },
        {
        "parameter": "printer",
        "argument": "printer_option",
        "description": "the type of printer that will create the 3D print",
        "argument_value": str(round(random.uniform(2,8)*1.17,2))
        },
    ]
    p_and_a_set_4 = [
        {
        "parameter": "capacity",
        "argument": "how_busy",
        "description": "how busy the 3D print lab currently is as a percentage of full capacity (this value should be between 0 and 100)",
        "argument_value": str(random.randrange(0,10)*10)
        },
        {
        "parameter": "how_busy",
        "argument": "capacity",
        "description": "how busy the 3D print lab currently is as a percentage of full capacity (this value should be between 0 and 100)",
        "argument_value": str(random.randrange(0,10)*10)
        },
        {
        "parameter": "availability",
        "argument": "percent_in_use",
        "description": "how many printers are available to use, as a percentage of the total number of printers in the lab (this value should be between 0 and 100)",
        "argument_value": str(random.randrange(0,10)*10)
        },
        {
        "parameter": "percent_in_use",
        "argument": "availability",
        "description": "how many printers are available to use, as a percentage of the total number of printers in the lab (this value should be between 0 and 100)",
        "argument_value": str(random.randrange(0,10)*10)
        },
    ]



    # Here's a bunch of return variables to choose from later
    # For this type of question, let the assignment variables be the same
    # name as the return variables, since this is a "Level 1" type question
    return_variable_set_1 = [
        {
            "name": "filament",
            "description": "an estimate of the length of filament is required for the 3D print",
            "assignment": "filament",
        },
        {
            "name": "lengthFil",
            "description": "an estimate of the length of filament is required for the 3D print",
            "assignment": "lengthFil",
        },
        {
            "name": "filamentLength",
            "description": "an estimate of the length of filament is required for the 3D print",
            "assignment": "filamentLength",
        },
        {
            "name": "filLength",
            "description": "an estimate of the length of filament is required for the 3D print",
            "assignment": "filLength",
        }
    ]
    return_variable_set_2 = [
        {
            "name": "cost",
            "description": "an estimate of how much this 3D print will cost",
            "assignment": "cost",
        },
        {
            "name": "customerCost",
            "description": "an estimate of how much this 3D print will cost",
            "assignment": "customerCost",
        },
        {
            "name": "estCost",
            "description": "an estimate of how much this 3D print will cost",
            "assignment": "estCost",
        },
        {
            "name": "filCost",
            "description": "an estimate of how much this 3D print will cost",
            "assignment": "filCost",
        }
    ]
    return_variable_set_3 = [
        {
            "name": "printTime",
            "description": "the estimated time for the 3D print",
            "assignment": "printTime",
        },
        {
            "name": "time2print",
            "description": "the estimated time for the 3D print",
            "assignment": "time2print",
        },
        {
            "name": "print_time",
            "description": "the estimated time for the 3D print",
            "assignment": "print_time",
        },
        {
            "name": "time_to_print",
            "description": "the estimated time for the 3D print",
            "assignment": "time_to_print",
        }
    ]



    # ----------------------------------------------------------------
    # CREATE THE PROBLEM
    # ----------------------------------------------------------------

    # shuffle all the specified information above; it helps with randomizing the problem variants
    random.shuffle(functionName)

    # shuffle the parameters/arguments and combine them into one set
    random.shuffle(p_and_a_set_reqd)
    random.shuffle(p_and_a_set_1)
    random.shuffle(p_and_a_set_2)
    random.shuffle(p_and_a_set_3)
    random.shuffle(p_and_a_set_4)
    p_and_a_set_all = [
        p_and_a_set_1,
        p_and_a_set_2,
        p_and_a_set_3,
        p_and_a_set_4
    ]
    random.shuffle(p_and_a_set_all)

    # shuffle the random variables and combine them into one set
    random.shuffle(return_variable_set_1)
    random.shuffle(return_variable_set_2)
    random.shuffle(return_variable_set_3)
    return_variable_set_all = [return_variable_set_1,return_variable_set_2,return_variable_set_3]
    random.shuffle(return_variable_set_all)

    # Determine number of parameters and return variables for this question variant
    numParams = random.randint(2,3)
    numReturnVars = random.randint(2,3)

    # Create the set of parameters and return variables

    # first, add the required parameter
    parameter_set = []
    parameter_set.append(p_and_a_set_reqd[0])

    # then add the remaining parameters, randomly chosen
    i = 0
    while i < numParams:
        parameter_set.append(p_and_a_set_all[i][0])
        i += 1

    # JUST FOR THIS PROBLEM BECAUSE I SET IT UP DUMB
    numParams += 1 # add 1 to the number of parameters because of the "required" one

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
            "parameters": parameters,
            "parameter_descriptions": parameter_descriptions,
            "return_variables": return_variables,
            "return_variable_descriptions": return_variable_descriptions,
            "arguments": arguments,
            "argument_values": argument_values,
            "assignments": assignments,
        }
    ]


    # ----------------------------------------------------------------
    # SAVE THE DATA FOR PRAIRIELEARN TO USE
    # ----------------------------------------------------------------

    # function description
    data['params']['functionName'] = scenarios[0]["function_name"]


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





    # save the answer data for the problem
    answers = func_call_answers(scenarios[0],5)
    line_num = 'line'+str(1)
    data['params'][line_num] = answers