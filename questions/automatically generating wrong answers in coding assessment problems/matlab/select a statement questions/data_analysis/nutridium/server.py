import random
import copy




# ----------------------------------------------------------------
# PROBLEM DESCRIPTION
# ----------------------------------------------------------------

# This problem has students implement a basic data analysis function.
# In general, the function needs to do 5 things (not necessarily in this order): 
#    1. call max or min on some aspect of the data
#    2. use a relational operator to identify some characteristic
#    3. use a relational operator to identify some other characteristic
#    4. use a logical operator to identify some combination of the characteristics
#    5. use logical indexing to select part of some data


# IF YOU ARE GOING TO USE THIS TEMPLATE - There's an even more templated version under actual assessment question / data_analysis / chemical_reaction - I would use that one :)






def generate(data):

    # ----------------------------------------------------------------
    # IMPORT FUNCTIONS FOR GENERATING ANSWERS
    # ----------------------------------------------------------------


    import sys
    sys.path.append(data["options"]["server_files_course_path"])
    from generatingAnswers import func_header_answers
    from generatingAnswers import make_logical_indexing_answers
    from generatingAnswers import func_call_answers
    from generatingAnswers import make_multiple_relational_logical_operation_answers


    # ------------------------------------------------------------------------
    # DATA FOR THE PROBLEM -- JUST CHANGE THIS PART TO MAKE A NEW PROBLEM! :)
    # ------------------------------------------------------------------------

    scenarios = [
        {
            "plant-name": "Nutridium",

            "criteria1": "temperature",
            "criteria2": "soil acidity",

            "function_name": "bestLoc",
            "parameters": ["temps","acidities", "lowTemp", "highTemp"],
            "parameter-descriptions": ["a 1xN vector with temperature information for each location", "a 1xN vector with soil acidity information for each location (corresponds to the temperature information in the first parameter)", "the lowest temperature that Nutridium can grow at", "the highest temperature that Nutridium can grow at"],
            "return_variables": ["index", "temp", "acidity"],
            "returnValues-descriptions": ["the index of the best location", "the temperature at the best location", "the soil acidity at the best location"],
        }
        
    ]

    # ----------------------------------------------------------------
    # CREATE THE PROBLEM -- DON'T CHANGE ANYTHING FROM HERE ON DOWN
    # ----------------------------------------------------------------

    random.shuffle(scenarios)

    # populate the scenario information
    data['params']['plant-name'] = scenarios[0]["plant-name"]

    data['params']['criteria1'] = scenarios[0]["criteria1"]
    data['params']['criteria2'] = scenarios[0]["criteria2"]

    data['params']['function_name'] = scenarios[0]["function_name"]

    # --------------------------------------------------------
    # SET UP FUNCTION
    # --------------------------------------------------------
    # create the parameter list of descriptions and the code to declare the arguments
    parameterList = ""
    for j in range(len(scenarios[0]["parameters"])):
        parameterList += str(j+1) + ". " + scenarios[0]["parameter-descriptions"][j] + " \r\n"

    # create the return value list of descriptions
    returnVarList = ""
    for j in range(len(scenarios[0]["return_variables"])):
        returnVarList += str(j+1) + ". " + scenarios[0]["returnValues-descriptions"][j] + " \r\n"

    data['params']['parameterList'] = parameterList
    data['params']['returnVarList'] = returnVarList

    # all the parameter info
    i = 0
    while i < len(scenarios[0]["parameters"]):
        temp = "param"+str(i+1)
        data['params'][temp] = scenarios[0]["parameters"][i]
        temp = "param"+str(i+1)+"description"
        data['params'][temp] = scenarios[0]["parameter-descriptions"][i]
        i += 1

    # all the return variable info
    i = 0
    while i < len(scenarios[0]["return_variables"]):
        temp = "rv"+str(i+1)
        data['params'][temp] = scenarios[0]["return_variables"][i]
        temp = "rv"+str(i+1)+"description"
        data['params'][temp] = scenarios[0]["returnValues-descriptions"][i]
        i += 1

    # --------------------------------------------------------
    # STEP 1 (FUNCTION HEADER)
    # --------------------------------------------------------
    answers = func_header_answers(scenarios[0],5)
    line_num = 'funcline'+str(1)
    data['params'][line_num] = answers

    # --------------------------------------------------------
    # STEP 2 (LOGICAL INDEXING)
    # --------------------------------------------------------
    info = {}
    info["vars"] = [data['params']['param1'],data['params']['param3'],data['params']['param1'],data['params']['param4']]
    info['operators'] = ['<','|','>']
    info['assignment'] = 'which'
    info['distractors'] = [data['params']['param2']]

    answers = make_multiple_relational_logical_operation_answers(info,5)
    for i in range(len(answers)):
        answers[i]['ans'] += '\n'+data['params']['param2']+'(which) = 0;\n'+data['params']['param1']+'(which) = 0;'
    line_num = 'funcline'+str(2)
    data['params'][line_num] = answers

    # --------------------------------------------------------
    # STEP 3 (CALL MAX)
    # --------------------------------------------------------
    info = {}
    info["function_name"] = "max"
    info["parameters"] = [data['params']['param2']]
    info["arguments"] = [data['params']['param2']]
    info["return_variables"] = [data['params']['rv3'], data['params']['rv1']]
    info["assignments"] = [data['params']['rv3'], data['params']['rv1']]
    info["distractor_variables"] = [data['params']['param1'], data['params']['rv2']]
    info["distractor_functions"] = ["min"]

    answers = func_call_answers(info,5)
    line_num = 'funcline'+str(3)
    data['params'][line_num] = answers


    # --------------------------------------------------------
    # STEP 4 (INDEX)
    # --------------------------------------------------------
    info = {}
    info["variable"] = data['params']['param1']
    info["indexing_variable"] = data['params']['rv1']
    info['assignment'] = data['params']['rv2']
    info["distractors"] = [data['params']['param2'], data['params']['rv3']]

    answers = make_logical_indexing_answers(info,5)
    line_num = 'funcline'+str(4)
    data['params'][line_num] = answers