import random
import copy




# ----------------------------------------------------------------
# PROBLEM DESCRIPTION
# ----------------------------------------------------------------

# This is a problem that has students write functions to load data into a vector of structs and also a function to print a vector of structs



def generate(data):

    # ----------------------------------------------------------------
    # IMPORT FUNCTIONS FOR GENERATING ANSWERS
    # ----------------------------------------------------------------


    import sys
    sys.path.append(data["options"]["server_files_course_path"])
    from generatingAnswersCplusplus import func_header_answers


    # ------------------------------------------------------------------------
    # DATA FOR THE PROBLEM -- JUST CHANGE THIS PART TO MAKE A NEW PROBLEM! :)
    # ------------------------------------------------------------------------
    scenarios = [
        {
            "company": {
                "name": "Ascrizzi Safety Solutions, Inc.",
                "task_description": "categorize their drones so that the appropriate drone can be quickly deployed for disaster relief after earthquakes, tornadoes, fires, and other natural disasters",
                "task_description_short": "categorize the drones"
            },
            "function": {
                "name1": "loadDrones",
                "name2": "printDrones"
            },
            "impl": {
                "vector": "squad",
                "istream": "inputData",
                "ostream": "outputData",
                "singleStruct": "drone"
            },
            "struct": {
                "generic_type": "information about each drone",
                "name": "Drone",
                "type1": "bool",
                "type2": "string",
                "type3": "double",
                "type4": "int",
                "member1": "isDeployed",
                "member2": "name",
                "member3": "capacity",
                "member4": "numRotors",
                "desc2": " kg capacity",
                "desc3": " rotors"
            },
            "input": {
                "filename": "drones.txt",
                "order": "deployment status (0 = false, 1 = true), name of drone, capacity (in kg), number of rotors",
                "name1": "Droneo_and_Juliet",
                "val1_1": "75.10",
                "val1_2": "12",
                "val1_3": "0",
                "status1": "available",
                "name2": "The_Ever_Spinner",
                "val2_1": "9.5",
                "val2_2": "4",
                "val2_3": "1",
                "status2": "responding to an incident",
                "name3": "Droney_McDroneface",
                "val3_1": "27.83",
                "val3_2": "6",
                "val3_3": "0",
                "status3": "available"
            }
        }
    ]

    # scenario = {
    #     "company_name": "Ascrizzi Safety Solutions, Inc.",

    #     "intro": "",

    #     "task": "categorize their drones so that the appropriate drone can be quickly deployed for disaster relief after earthquakes, tornadoes, fires, and other natural disasters",

    #     "task_short" : "categorize the drones",

    #     "data_input": [
    #         { 
    #             "filename": "drones.txt",
    #             "order": "deployment status (0 = false, 1 = true), name of drone, capacity (in kg), number of rotors",
    #             "name1": "Droneo_and_Juliet",
    #             "val1_1": "75.10",
    #             "val1_2": "12",
    #             "val1_3": "0",
    #             "status1": "available",
    #             "name2": "The_Ever_Spinner",
    #             "val2_1": "9.5",
    #             "val2_2": "4",
    #             "val2_3": "1",
    #             "status2": "responding to an incident",
    #             "name3": "Droney_McDroneface",
    #             "val3_1": "27.83",
    #             "val3_2": "6",
    #             "val3_3": "0",
    #             "status3": "available"
    #         },
    #     ],

    #     "struct": {
    #         "generic_type": "information about each drone",
    #         "name": "Drone",
    #         "type1": "bool",
    #         "type2": "string",
    #         "type3": "double",
    #         "type4": "int",
    #         "member1": "isDeployed",
    #         "member2": "name",
    #         "member3": "capacity",
    #         "member4": "numRotors",
    #         "desc2": " kg capacity",
    #         "desc3": " rotors"
    #     }, 

    #     "variables": {
    #         "vector": "squad",
    #         "istream": "inputData",
    #         "ostream": "outputData",
    #         "singleStruct": "drone"
    #     }
    # }

    
    # helper_functions = [
    #     {
    #         "function_name": "load" + scenario["struct"]["name"] + "s",
    #         "short_description": "crop an image",
    #         "description": "populates `" + scenario["variables"]["vector"] + "` with the information in the `" + scenario["data_input"]["filename"] + "` file. You may assume `" + scenario["data_input"]["filename"] + "` exists and contains data in correct order. The function does not return anything.",
    #         "parameters": [scenario["variables"]["vector"],scenario["variables"]["istream"],],
    #         "parameter_descriptions": ["a vector of `" + scenario["struct"]["name"] + "` variables","an input stream object connected to the `" + scenario["data_input"]["filename"] + "` file"],
    #         # "return_variables": ["img"],
    #         # "return_variable_descriptions": ["a 3D array representing the cropped image"],
    #         # "arguments": ["img","90","470","70"], #this zooms in to Michigan
    #         # "assignments": ["img_crop"],
    #         # "internal_variables": ["rows","cols"],
    #         # "steps": [
    #         #     "Create the function header",
    #         #     "Determine the range of rows and columns to keep",
    #         #     "Keep the portion of the image in these ranges",
    #         # ],
    #         # "algorithm": [
    #         #     "Determine the range of rows and columns to keep. The rows and columns should go from (specified value passed into the function - the offset) to (specified value passed into the function + the offset).",
    #         #     "Overwrite the image variable with just the portion that is specified by the ranges for the rows and columns.",
    #         # ],
    #     },
    #     {
    #         "function_name": "print" + scenario["struct"]["name"] + "s",
    #         "short_description": "highlight an image",
    #         "description": "returns an image that is highlighted according to the criteria passed in to the function. In this case, the areas that are \"high red and low green/blue\" are highlighted and the other areas are dimmed",
    #         "parameters": ["img","r_min","g_max","b_max"],
    #         "parameter_descriptions": ["a 3D array representing an image in RGB format", "the minimum value for the red channel (value: 0-255)","the maximum value for the green channel (value: 0-255)","the maximum value for the blue channel (value: 0-255)"],
    #         "return_variables": ["img"],
    #         "return_variable_descriptions": ["a 3D array representing the highlighted version of the image"],
    #         "arguments": ["img", "250", "150", "150"],
    #         "assignments": ["img_highlighted"],
    #         "internal_variables": ["red","green","blue","select"],
    #         "dim_value": "40", # make sure this matches the corresponding step description below
    #         "comparisons": [">", "<" , "<"], #these are the correct RGB comparisons
    #         "combine": ["&", "&" ], # how to combine the comparisons
    #         "steps": [
    #             "Create the function header",
    #             "Pull out the RGB channels",
    #             "Find the areas to highlight",
    #             "Highlight these areas by making them as bright as possible",
    #             "Set the other areas to be 40% of their original values",
    #             "Copy the RGB channels back into the image",
    #         ],
    #         "algorithm": [
    #             "Pull out the RGB channels so that the function can work with them individually.",
    #             "Find the locations to highlight. The locations to highlight are those locations that have a red value greater than the minimum red value, a green value less the maximum green value, and a blue value less than the maximum blue value.",
    #             "Highlight these locations by making them as bright as possible -- set the red, green, and blue values for these locations to be their highest possible values in image representation.",
    #             "To make the highlighting stand out more, dim all the other locations -- set the red, green, and blue values for these locations to be 40% of their original values.",
    #             "Copy the RGB channels back into the image so that the image variable has been updated with the new, highlighted version.",
    #         ],
    #     },
    # ]
        
    # scenario["helper_functions"] = copy.deepcopy(helper_functions)

    # scenarios.append(scenario)
        
    # old = {
    #         "company": {
    #             "name": "Ascrizzi Safety Solutions, Inc.",
    #             "task_description": "categorize their drones so that the appropriate drone can be quickly deployed for disaster relief after earthquakes, tornadoes, fires, and other natural disasters",
    #             "task_description_short": "categorize the drones"
    #         },
    #         "function": {
    #             "name1": "loadDrones",
    #             "name2": "printDrones"
    #         },
    #         "impl": {
    #             "vector": "squad",
    #             "istream": "inputData",
    #             "ostream": "outputData",
    #             "singleStruct": "drone"
    #         },
    #         "struct": {
    #             "generic_type": "information about each drone",
    #             "name": "Drone",
    #             "type1": "bool",
    #             "type2": "string",
    #             "type3": "double",
    #             "type4": "int",
    #             "member1": "isDeployed",
    #             "member2": "name",
    #             "member3": "capacity",
    #             "member4": "numRotors",
    #             "desc2": " kg capacity",
    #             "desc3": " rotors"
    #         },
    #         "input": {
    #             "filename": "drones.txt",
    #             "order": "deployment status (0 = false, 1 = true), name of drone, capacity (in kg), number of rotors",
    #             "name1": "Droneo_and_Juliet",
    #             "val1_1": "75.10",
    #             "val1_2": "12",
    #             "val1_3": "0",
    #             "status1": "available",
    #             "name2": "The_Ever_Spinner",
    #             "val2_1": "9.5",
    #             "val2_2": "4",
    #             "val2_3": "1",
    #             "status2": "responding to an incident",
    #             "name3": "Droney_McDroneface",
    #             "val3_1": "27.83",
    #             "val3_2": "6",
    #             "val3_3": "0",
    #             "status3": "available"
    #         }
    #     }
        
    



    # ----------------------------------------------------------------
    # CREATE THE PROBLEM -- DON'T CHANGE ANYTHING FROM HERE ON DOWN
    # ----------------------------------------------------------------

    random.shuffle(scenarios)
    
    # populate the scenario information
    data['params']['company_name'] = scenarios[0]["company"]["name"]
    data['params']['company_task_description'] = scenarios[0]["company"]["task_description"]
    data['params']['company_task_description_short'] = scenarios[0]["company"]["task_description_short"]



    data['params']['function_name1'] = scenarios[0]["function"]["name1"]
    data['params']['function_name2'] = scenarios[0]["function"]["name2"]

    data['params']['impl_vector'] = scenarios[0]["impl"]["vector"]
    data['params']['impl_istream'] = scenarios[0]["impl"]["istream"]
    data['params']['impl_ostream'] = scenarios[0]["impl"]["ostream"]
    data['params']['impl_singleStruct'] = scenarios[0]["impl"]["singleStruct"]

    
    data['params']['struct_generic_type'] = scenarios[0]["struct"]["generic_type"]
    data['params']['struct_name'] = scenarios[0]["struct"]["name"]
    data['params']['struct_type1'] = scenarios[0]["struct"]["type1"]
    data['params']['struct_type2'] = scenarios[0]["struct"]["type2"]
    data['params']['struct_type3'] = scenarios[0]["struct"]["type3"]
    data['params']['struct_type4'] = scenarios[0]["struct"]["type4"]
    data['params']['struct_member1'] = scenarios[0]["struct"]["member1"]
    data['params']['struct_member2'] = scenarios[0]["struct"]["member2"]
    data['params']['struct_member3'] = scenarios[0]["struct"]["member3"]
    data['params']['struct_member4'] = scenarios[0]["struct"]["member4"]
    data['params']['struct_desc2'] = scenarios[0]["struct"]["desc2"]
    data['params']['struct_desc3'] = scenarios[0]["struct"]["desc3"]



    data['params']['input_filename'] = scenarios[0]["input"]["filename"]
    data['params']['input_order'] = scenarios[0]["input"]["order"]
    data['params']['input_name1'] = scenarios[0]["input"]["name1"]
    data['params']['input_val1_1'] = scenarios[0]["input"]["val1_1"]
    data['params']['input_val1_2'] = scenarios[0]["input"]["val1_2"]
    data['params']['input_val1_3'] = scenarios[0]["input"]["val1_3"]
    data['params']['input_status1'] = scenarios[0]["input"]["status1"]
    data['params']['input_name2'] = scenarios[0]["input"]["name2"]
    data['params']['input_val2_1'] = scenarios[0]["input"]["val2_1"]
    data['params']['input_val2_2'] = scenarios[0]["input"]["val2_2"]
    data['params']['input_val2_3'] = scenarios[0]["input"]["val2_3"]
    data['params']['input_status2'] = scenarios[0]["input"]["status2"]
    data['params']['input_name3'] = scenarios[0]["input"]["name3"]
    data['params']['input_val3_1'] = scenarios[0]["input"]["val3_1"]
    data['params']['input_val3_2'] = scenarios[0]["input"]["val3_2"]
    data['params']['input_val3_3'] = scenarios[0]["input"]["val3_3"]
    data['params']['input_status3'] = scenarios[0]["input"]["status3"]





    # --------------------------------------------------------
    # FUNCTION 1
    # --------------------------------------------------------
    

    data['params']['func1description'] = "FUNCTION TO LOAD DATA"

    # --------------------------------------------------------
    # STEP 1
    # --------------------------------------------------------

    data['params']['func1step1description'] = "TODO MAYBE"

    # helper_function_info = scenarios[0]["helper_functions"][0]
    # data['params']['helper1functionname'] = helper_function_info["function_name"]

    # # all the parameter info
    # i = 0
    # while i < len(helper_function_info["parameters"]):
    #     temp = "helper1param"+str(i+1)
    #     data['params'][temp] = helper_function_info["parameters"][i]
    #     temp = "helper1param"+str(i+1)+"description"
    #     data['params'][temp] = helper_function_info["parameter_descriptions"][i]
    #     i += 1

    # # all the return variable info
    # i = 0
    # while i < len(helper_function_info["return_variables"]):
    #     temp = "helper1rv"+str(i+1)
    #     data['params'][temp] = helper_function_info["return_variables"][i]
    #     temp = "helper1rv"+str(i+1)+"description"
    #     data['params'][temp] = helper_function_info["return_variable_descriptions"][i]
    #     i += 1
# void loadDrones(vector<Drone> &squad, istream &inputData) {

    helper_function_info = {
        "function_name": scenarios[0]["function"]["name1"],
        "function_type": "void",
        "parameters": [
            {
                "name": scenarios[0]["impl"]["vector"],
                "type": "vector<"+ scenarios[0]["struct"]["name"] + ">",
                "pass_by_reference": True,
            },
            {
                "name": scenarios[0]["impl"]["istream"],
                "type": "istream",
                "pass_by_reference": True,
            }
        ],
        
        "return_variables": [
            {
                "name": "",
            },
        ],
        "arguments": ["var","var"], 
        "assignments": ["var","var"],
        "distractor_functions": ["func", "another_func" ],
        "distractor_types":[
            "string","char","int","double","bool", "vector", "vector<"+ scenarios[0]["struct"]["name"] + ">"
        ],
    }

    answers = func_header_answers(helper_function_info,False,5)
    line_num = 'func1line'+str(1)
    data['params'][line_num] = answers



    # --------------------------------------------------------
    # STEP 2
    # --------------------------------------------------------

    # initialize struct

    data['params']['func1step2description'] = "TODO MAYBE"

    answers = [
        {
            'tag': 'true', 
            'ans':"    " + scenarios[0]["struct"]["name"] + " " +  scenarios[0]["impl"]["singleStruct"] + ";",
        },
        {
            'tag': 'false', 
            'ans':"    " + scenarios[0]["impl"]["singleStruct"] + " " +  scenarios[0]["struct"]["name"] + ";"
        },
        {
            'tag': 'false', 
            'ans':"    " + scenarios[0]["struct"]["type1"] + " " + scenarios[0]["struct"]["member1"] + ";\n    " + scenarios[0]["struct"]["type2"] + " " + scenarios[0]["struct"]["member2"] + ";\n    " + scenarios[0]["struct"]["type3"] + " " + scenarios[0]["struct"]["member3"] + ";\n    " + scenarios[0]["struct"]["type4"] + " " + scenarios[0]["struct"]["member4"] + ";"
        },

        {
            'tag': 'false', 
            'ans':"    vector<" + scenarios[0]["struct"]["name"] + "> " + scenarios[0]["impl"]["vector"] + ";"
        },

    ]

    line_num = 'func1line'+str(2)
    data['params'][line_num] = answers


    # --------------------------------------------------------
    # STEP 3
    # --------------------------------------------------------

    data['params']['func1step3description'] = "TODO MAYBE"

    answers = [
        {
            'tag': 'true', 
            'ans': "    while (" + scenarios[0]["impl"]["istream"] + " >> " + scenarios[0]["impl"]["singleStruct"] + "." + scenarios[0]["struct"]["member1"] + " >> " + scenarios[0]["impl"]["singleStruct"] + "." + scenarios[0]["struct"]["member2"] + " >> " + scenarios[0]["impl"]["singleStruct"] + "." + scenarios[0]["struct"]["member3"] + " >> " + scenarios[0]["impl"]["singleStruct"] + "." + scenarios[0]["struct"]["member4"] + ") {",
        },
        {
            'tag': 'false', 
            'ans': "    while (" + scenarios[0]["impl"]["istream"] + " >> " + scenarios[0]["impl"]["singleStruct"] + "." + scenarios[0]["struct"]["member2"] + " >> " + scenarios[0]["impl"]["singleStruct"] + "." + scenarios[0]["struct"]["member4"] + " >> " + scenarios[0]["impl"]["singleStruct"] + "." + scenarios[0]["struct"]["member1"] + " >> " + scenarios[0]["impl"]["singleStruct"] + "." + scenarios[0]["struct"]["member3"] + ") {"
        },
        {
            'tag': 'false', 
            'ans': "    for (int i = 0; i < " + scenarios[0]["impl"]["vector"] + ".size(); ++i) {"
        },

        {
            'tag': 'false', 
            'ans': "    while (getline(" + scenarios[0]["impl"]["istream"] + ", " + scenarios[0]["impl"]["singleStruct"] + ")) {"
        },

    ]
    line_num = 'func1line'+str(3)
    data['params'][line_num] = answers





    # --------------------------------------------------------
    # STEP 4
    # --------------------------------------------------------

    data['params']['func1step4description'] = "TODO MAYBE"

    answers = [
        {
            'tag': 'true', 
            'ans': "        " + scenarios[0]["impl"]["vector"] + ".push_back(" + scenarios[0]["impl"]["singleStruct"] + ");"
        },
        {
            'tag': 'false', 
            'ans': "        " + scenarios[0]["impl"]["vector"] + ".add_element(" + scenarios[0]["struct"]["member1"] + ", " + scenarios[0]["struct"]["member2"] + ", " + scenarios[0]["struct"]["member3"] + ", " + scenarios[0]["struct"]["member4"] + ");"
        },
        {
            'tag': 'false', 
            'ans': "        " + scenarios[0]["impl"]["vector"] + ".at(i) = " + scenarios[0]["impl"]["singleStruct"] + ";",
        },
        {
            'tag': 'false', 
            'ans': "        " + scenarios[0]["impl"]["vector"] + ".pop_back(" + scenarios[0]["impl"]["singleStruct"] + ");"
        },

    ]
    line_num = 'func1line'+str(4)
    data['params'][line_num] = answers



    # --------------------------------------------------------
    # STEP 5
    # --------------------------------------------------------

    data['params']['func1step5description'] = "TODO MAYBE"

    answers = [
        {
            'tag': 'true', 
            'ans': "    }  // END OF LOOP"
        }

    ]
    line_num = 'func1line'+str(5)
    data['params'][line_num] = answers


    # --------------------------------------------------------
    # STEP 6
    # --------------------------------------------------------

    data['params']['func1step5description'] = "TODO MAYBE"

    answers = [
        {
            'tag': 'true', 
            'ans': "}  // END OF FUNCTION"
        }

    ]
    line_num = 'func1line'+str(6)
    data['params'][line_num] = answers



    # --------------------------------------------------------
    # FUNCTION 2
    # --------------------------------------------------------

    data['params']['func2description'] = "FUNCTION TO PRINT DATA"


    # --------------------------------------------------------
    # STEP 1
    # --------------------------------------------------------

    data['params']['func2step1description'] = "TODO MAYBE"

    helper_function_info = {
        "function_name": scenarios[0]["function"]["name2"],
        "function_type": "void",
        "parameters": [
            {
                "name": scenarios[0]["impl"]["vector"],
                "type": "vector<"+ scenarios[0]["struct"]["name"] + ">",
                "pass_by_reference": "const",
            },
            {
                "name": scenarios[0]["impl"]["ostream"],
                "type": "ostream",
                "pass_by_reference": True,
            }
        ],
        
        "return_variables": [
            {
                "name": "",
            },
        ],
        "arguments": ["var","var"], 
        "assignments": ["var","var"],
        "distractor_functions": ["func", "another_func" ],
        "distractor_types":[
            "string","char","int","double","bool", "vector", "vector<"+ scenarios[0]["struct"]["name"] + ">"
        ],
    }

    answers = func_header_answers(helper_function_info,False,5)
    line_num = 'func2line'+str(1)
    data['params'][line_num] = answers



    # --------------------------------------------------------
    # STEP 2
    # --------------------------------------------------------

    data['params']['func2step2description'] = "TODO MAYBE"

    answers = [
        {
            'tag': 'true', 
            'ans': "    for (int i = 0; i < " + scenarios[0]["impl"]["vector"] + ".size(); ++i) {"
        },
        {
            'tag': 'false', 
            'ans': "    for (int i = 0; i < 4; ++i) {"
        },

        {
            'tag': 'false', 
            'ans': "    while (" + scenarios[0]["impl"]["ostream"] + " << " + scenarios[0]["impl"]["vector"] + ".at(i)) {",
        },
        {
            'tag': 'false', 
            'ans': "    while (i < " + scenarios[0]["impl"]["vector"] + ".size()) {"
        },

    ]

    line_num = 'func2line'+str(2)
    data['params'][line_num] = answers


    # --------------------------------------------------------
    # STEP 3
    # --------------------------------------------------------

    data['params']['func2step3description'] = "TODO MAYBE"

    answers = [
        {
            'tag': 'true', 
            'ans': "        " + scenarios[0]["impl"]["ostream"] + " << " + scenarios[0]["impl"]["vector"] + ".at(i)." + scenarios[0]["struct"]["member2"] + " << \":\" << endl;"
        },
        {
            'tag': 'false', 
            'ans': "        " + scenarios[0]["impl"]["ostream"] + " << " + scenarios[0]["impl"]["vector"] + "." + scenarios[0]["struct"]["member2"] + ".at(i) << \":\" ;"
        },

        {
            'tag': 'false', 
            'ans': "        " + scenarios[0]["impl"]["ostream"] + " << " + scenarios[0]["impl"]["singleStruct"] + ".at(i)." + scenarios[0]["struct"]["member2"] + " << \":\" << endl;",
        },
        {
            'tag': 'false', 
            'ans': "        " + scenarios[0]["impl"]["ostream"] + " << " + scenarios[0]["impl"]["vector"] + "." + scenarios[0]["struct"]["member2"] + ".at(i) << \":\" << endl;"
        },

    ]

    line_num = 'func2line'+str(3)
    data['params'][line_num] = answers


    # --------------------------------------------------------
    # STEP 4
    # --------------------------------------------------------

    data['params']['func2step4description'] = "TODO MAYBE"

    answers = [
        {
            'tag': 'true', 
            'ans': "        if (" + scenarios[0]["impl"]["vector"] + ".at(i)." + scenarios[0]["struct"]["member1"] + ") {\n            " + scenarios[0]["impl"]["ostream"] + " << \"  \" << \"" + scenarios[0]["input"]["status2"] + "\" << endl; \n        } else {\n            " + scenarios[0]["impl"]["ostream"] + " << \"  \" << \"available\" << endl;\n        }"
        },
        {
            'tag': 'false', 
            'ans': "        if (!" + scenarios[0]["impl"]["vector"] + ".at(i)." + scenarios[0]["struct"]["member1"] + ") {\n            " + scenarios[0]["impl"]["ostream"] + " << \"  \" << \"" + scenarios[0]["input"]["status2"] + "\" << endl; \n        } else {\n            " + scenarios[0]["impl"]["ostream"] + " << \"  \" << \"available\" << endl;\n        }"
        },
    ]

    line_num = 'func2line'+str(4)
    data['params'][line_num] = answers



    # --------------------------------------------------------
    # STEP 5
    # --------------------------------------------------------

    data['params']['func2step5description'] = "TODO MAYBE"

    answers = [
        {
            'tag': 'true', 
            'ans': "        " + scenarios[0]["impl"]["ostream"] + " << \"  \" << " + scenarios[0]["impl"]["vector"] + ".at(i)." + scenarios[0]["struct"]["member3"] + " << \"" + scenarios[0]["struct"]["desc2"] + "\" << endl; \n        " + scenarios[0]["impl"]["ostream"] + " << \"  \" << " + scenarios[0]["impl"]["vector"] + ".at(i)." + scenarios[0]["struct"]["member4"] + " << \"" + scenarios[0]["struct"]["desc3"] + "\" << endl;"
        },
        {
            'tag': 'false', 
            'ans': "        " + scenarios[0]["impl"]["ostream"] + " << \"  \" << " + scenarios[0]["impl"]["vector"] + "." + scenarios[0]["struct"]["member3"] + ".at(i) << \"" + scenarios[0]["struct"]["desc2"] + "\"; \n        " + scenarios[0]["impl"]["ostream"] + " << \"  \" << " + scenarios[0]["impl"]["vector"] + "." + scenarios[0]["struct"]["member4"] + ".at(i) << \"" + scenarios[0]["struct"]["desc3"] + "\";"
        },
        {
            'tag': 'false', 
            'ans': "        " + scenarios[0]["impl"]["ostream"] + " << \"  \" << " + scenarios[0]["impl"]["vector"] + "." + scenarios[0]["struct"]["member3"] + ".at(i) << \"" + scenarios[0]["struct"]["desc2"] + "\" << endl; \n        " + scenarios[0]["impl"]["ostream"] + " << \"  \" << " + scenarios[0]["impl"]["vector"] + "." + scenarios[0]["struct"]["member4"] + ".at(i) << \"" + scenarios[0]["struct"]["desc3"] + "\" << endl;"
        },
        {
            'tag': 'false', 
            'ans': "        cout << \"  \" << " + scenarios[0]["impl"]["vector"] + ".at(i)." + scenarios[0]["struct"]["member3"] + " << \"" + scenarios[0]["struct"]["desc2"] + "\" << endl; \n        cout << \"  \" << " + scenarios[0]["impl"]["vector"] + ".at(i)." + scenarios[0]["struct"]["member4"] + " << \"" + scenarios[0]["struct"]["desc3"] + "\" << endl;"
        },
        {
            'tag': 'false', 
            'ans': "        cout << \"  \" << " + scenarios[0]["impl"]["vector"] + "." + scenarios[0]["struct"]["member3"] + ".at(i) << \"" + scenarios[0]["struct"]["desc2"] + "\"; \n        cout << \"  \" << " + scenarios[0]["impl"]["vector"] + "." + scenarios[0]["struct"]["member4"] + ".at(i) << \"" + scenarios[0]["struct"]["desc3"] + "\";"
        },
        {
            'tag': 'false', 
            'ans': "        cout << \"  \" << " + scenarios[0]["impl"]["vector"] + "." + scenarios[0]["struct"]["member3"] + ".at(i) << \"" + scenarios[0]["struct"]["desc2"] + "\" << endl; \n        cout << \"  \" << " + scenarios[0]["impl"]["vector"] + "." + scenarios[0]["struct"]["member4"] + ".at(i) << \"" + scenarios[0]["struct"]["desc3"] + "\" << endl;"
        },
    ]

    line_num = 'func2line'+str(5)
    data['params'][line_num] = answers


    # --------------------------------------------------------
    # STEP 6
    # --------------------------------------------------------

    data['params']['func2step6description'] = "TODO MAYBE"

    answers = [
        {
            'tag': 'true', 
            'ans': "        " + scenarios[0]["impl"]["ostream"] + " << endl;"
        },

    ]


    line_num = 'func2line'+str(6)
    data['params'][line_num] = answers



    # --------------------------------------------------------
    # STEP 7
    # --------------------------------------------------------

    answers = [
        {
            'tag': 'true', 
            'ans': "    }  // END OF LOOP"
        }

    ]
    line_num = 'func2line'+str(7)
    data['params'][line_num] = answers




    # --------------------------------------------------------
    # STEP 8
    # --------------------------------------------------------

    answers = [
        {
            'tag': 'true', 
            'ans': "}  // END OF FUNCTION"
        }

    ]
    line_num = 'func2line'+str(8)
    data['params'][line_num] = answers