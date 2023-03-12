import random
import copy




# ----------------------------------------------------------------
# PROBLEM DESCRIPTION
# ----------------------------------------------------------------

# This is a driver program that primarily manipulates images, ala the Watch Display script from Project 2. 
# There are 7 steps to this driver program:
#   1. clear the workspace and close existing figures
#   2. load an image
#   3. get some information from a helper function
#   4. get some information from a different helper function
#   5. create new image by calling a helper function
#   6. crop the image using indexing (indices can be from a helper function earlier!)
#   7. save the new image to a file


# This problem is about 3D printing. The original function was part of a multiple choice problem in either the F20 or W21 exam. Laura can't remember :) 



def generate(data):

    # ----------------------------------------------------------------
    # IMPORT FUNCTIONS FOR GENERATING ANSWERS
    # ----------------------------------------------------------------


    import sys
    sys.path.append(data["options"]["server_files_course_path"])
    from generatingAnswers import func_header_answers
    from generatingAnswers import make_crop_range_with_offsets_answers
    from generatingAnswers import crop_image_answers
    from generatingAnswers import pull_out_channels_answers
    from generatingAnswers import select_image_pixels_answers
    from generatingAnswers import set_channels_answers
    from generatingAnswers import copy_in_channels_answers

    # ------------------------------------------------------------------------
    # DATA FOR THE PROBLEM -- JUST CHANGE THIS PART TO MAKE A NEW PROBLEM! :)
    # ------------------------------------------------------------------------

    scenarios = [
        {
            "company_name": "We Love Plants",

            "intro": "NASA and NOAA have collected satellite images that calculate the Vegetation Health Image (VHI) of regions of the world. The VHI shows the drought status of a particular region, and these satellite images allow scientists to predict crop yields from various parts of the world. Here is an example VHI: ",

            "task": "For this exercise, we will take a look at a satellite image of the United States, and particularly look at which parts of Michigan are experiencing drought.",

            "data_description": "VHI data",
            "location": "Michigan",

            "input_images": [
                { 
                    "filename": "vhi_us_july_2019.png",
                    "variable": "img",
                    "caption": "The Vegetation Health Index map shows crop health in the continguous United States from July 22, 2019. source: https://www.nasa.gov/feature/how-satellite-maps-help-prevent-another-great-grain-robbery"
                },
            ],
            "output_images": [
                { 
                    "filename": "",
                    "variable": "predicted_drought",
                },
                { 
                    "filename": "MichiganDrought2019.png",
                    "variable": "zoom_in",
                }
            ],
            "data_input": [
                { 
                    "filename": "rainfall.mat",
                    "variable": "rainfall",
                },
            ],
            "helper_functions": [
                {
                    "function_name": "cropImage",
                    "short_description": "crop an image",
                    "description": "returns a cropped image. The image is cropped by using a center location (passed in via a row index and a column index) and a \"zoom offset\" (also passed in); the resulting image has a width and height of (1 + 2 * (zoom offset))",
                    "parameters": ["img","iRow","iCol","offset"],
                    "parameter_descriptions": ["a 3D array representing an image","the row index to center the crop around","the column index to center the crop around","the offset to use (e.g. how many rows/columns to keep around that center point specifed by the row and column parameters)"],
                    "return_variables": ["img"],
                    "return_variable_descriptions": ["a 3D array representing the cropped image"],
                    "arguments": ["img","90","470","70"], #this zooms in to Michigan
                    "assignments": ["img_crop"],
                    "internal_variables": ["rows","cols"],
                    "steps": [
                        "Create the function header",
                        "Determine the range of rows and columns to keep",
                        "Keep the portion of the image in these ranges",
                    ],
                    "algorithm": [
                        "Determine the range of rows and columns to keep. The rows and columns should go from (specified value passed into the function - the offset) to (specified value passed into the function + the offset).",
                        "Overwrite the image variable with just the portion that is specified by the ranges for the rows and columns.",
                    ],
                },
                {
                    "function_name": "highlightRed",
                    "short_description": "highlight an image",
                    "description": "returns an image that is highlighted according to the criteria passed in to the function. In this case, the areas that are \"high red and low green/blue\" are highlighted and the other areas are dimmed",
                    "parameters": ["img","r_min","g_max","b_max"],
                    "parameter_descriptions": ["a 3D array representing an image in RGB format", "the minimum value for the red channel (value: 0-255)","the maximum value for the green channel (value: 0-255)","the maximum value for the blue channel (value: 0-255)"],
                    "return_variables": ["img"],
                    "return_variable_descriptions": ["a 3D array representing the highlighted version of the image"],
                    "arguments": ["img", "250", "150", "150"],
                    "assignments": ["img_highlighted"],
                    "internal_variables": ["red","green","blue","select"],
                    "dim_value": "40", # make sure this matches the corresponding step description below
                    "comparisons": [">", "<" , "<"], #these are the correct RGB comparisons
                    "combine": ["&", "&" ], # how to combine the comparisons
                    "steps": [
                        "Create the function header",
                        "Pull out the RGB channels",
                        "Find the areas to highlight",
                        "Highlight these areas by making them as bright as possible",
                        "Set the other areas to be 40% of their original values",
                        "Copy the RGB channels back into the image",
                    ],
                    "algorithm": [
                        "Pull out the RGB channels so that the function can work with them individually.",
                        "Find the locations to highlight. The locations to highlight are those locations that have a red value greater than the minimum red value, a green value less the maximum green value, and a blue value less than the maximum blue value.",
                        "Highlight these locations by making them as bright as possible -- set the red, green, and blue values for these locations to be their highest possible values in image representation.",
                        "To make the highlighting stand out more, dim all the other locations -- set the red, green, and blue values for these locations to be 40% of their original values.",
                        "Copy the RGB channels back into the image so that the image variable has been updated with the new, highlighted version.",
                    ],
                },
            ]
        }
        
    ]

    # ----------------------------------------------------------------
    # CREATE THE PROBLEM -- DON'T CHANGE ANYTHING FROM HERE ON DOWN
    # ----------------------------------------------------------------

    random.shuffle(scenarios)
    
    # populate the scenario information
    data['params']['company_name'] = scenarios[0]["company_name"]
    data['params']['image_in'] = scenarios[0]["input_images"][0]["filename"]
    data['params']['image_in_caption'] = scenarios[0]["input_images"][0]["caption"]
    data['params']['image_out'] = scenarios[0]["output_images"][1]["filename"]
    data['params']['task'] = scenarios[0]["task"]
    data['params']['intro'] = scenarios[0]["intro"]
    data['params']['data_description'] = scenarios[0]["data_description"]
    data['params']['location'] = scenarios[0]["location"]



    # create the example script
    example_script = ""
    example_script += "% Read in map image" + "\n"
    example_script += "img = imread('" + scenarios[0]["input_images"][0]["filename"] + "');" + "\n"
    example_script += "\n"
    example_script += "% Crop to Michigan" + "\n"
    example_script += "img = " + scenarios[0]["helper_functions"][0]["function_name"]+ "(" + scenarios[0]["helper_functions"][0]["arguments"][0] + ", "+ scenarios[0]["helper_functions"][0]["arguments"][1] +", "+ scenarios[0]["helper_functions"][0]["arguments"][2] +", "+ scenarios[0]["helper_functions"][0]["arguments"][3] +");" + "\n"
    example_script += "\n"
    example_script += "% Highlight the \"high red, low green/blue\" areas" + "\n"
    example_script += "img = " + scenarios[0]["helper_functions"][1]["function_name"] + "(" + scenarios[0]["helper_functions"][1]["arguments"][0] + ", "+ scenarios[0]["helper_functions"][1]["arguments"][1] +", "+ scenarios[0]["helper_functions"][1]["arguments"][2] +", "+ scenarios[0]["helper_functions"][1]["arguments"][3] +");" + "\n"
    example_script += "\n"
    example_script += "% Display image" + "\n"
    example_script += "imshow(img);" + "\n"

    data['params']['example_script'] = example_script





    # --------------------------------------------------------
    # FUNCTION 1
    # --------------------------------------------------------
    data['params']['func1name'] = scenarios[0]["helper_functions"][0]["function_name"]
    data['params']['func1shortdescription'] = scenarios[0]["helper_functions"][0]["short_description"]
    data['params']['func1description'] = scenarios[0]["helper_functions"][0]["description"]

   # create the parameter list of descriptions and the code to declare the arguments
    parameterList = ""
    for j in range(len(scenarios[0]["helper_functions"][0]["parameters"])):
        parameterList += str(j+1) + ". " + scenarios[0]["helper_functions"][0]["parameter_descriptions"][j] + " \r\n"


    # create the return value list of descriptions
    returnVarList = ""
    for j in range(len(scenarios[0]["helper_functions"][0]["return_variables"])):
        returnVarList += str(j+1) + ". " + scenarios[0]["helper_functions"][0]["return_variable_descriptions"][j] + " \r\n"

    data['params']['func1parameterList'] = parameterList
    data['params']['func1returnVarList'] = returnVarList

    # create the algorithm
    algorithm = ""
    for j in range(len(scenarios[0]["helper_functions"][0]["algorithm"])):
        algorithm += "* " + scenarios[0]["helper_functions"][0]["algorithm"][j] + " \r\n"

    data['params']['func1algorithm'] = algorithm



    # --------------------------------------------------------
    # STEP 1
    # --------------------------------------------------------

    data['params']['func1step1description'] = scenarios[0]["helper_functions"][0]["steps"][0]

    helper_function_info = scenarios[0]["helper_functions"][0]
    data['params']['helper1functionname'] = helper_function_info["function_name"]

    # all the parameter info
    i = 0
    while i < len(helper_function_info["parameters"]):
        temp = "helper1param"+str(i+1)
        data['params'][temp] = helper_function_info["parameters"][i]
        temp = "helper1param"+str(i+1)+"description"
        data['params'][temp] = helper_function_info["parameter_descriptions"][i]
        i += 1

    # all the return variable info
    i = 0
    while i < len(helper_function_info["return_variables"]):
        temp = "helper1rv"+str(i+1)
        data['params'][temp] = helper_function_info["return_variables"][i]
        temp = "helper1rv"+str(i+1)+"description"
        data['params'][temp] = helper_function_info["return_variable_descriptions"][i]
        i += 1


    answers = func_header_answers(helper_function_info,5)
    line_num = 'func1line'+str(1)
    data['params'][line_num] = answers



    # --------------------------------------------------------
    # STEP 2
    # --------------------------------------------------------

    data['params']['func1step2description'] = scenarios[0]["helper_functions"][0]["steps"][1]

    info = scenarios[0]["helper_functions"][0]
    answers = make_crop_range_with_offsets_answers(info,5)
    line_num = 'func1line'+str(2)
    data['params'][line_num] = answers


    # --------------------------------------------------------
    # STEP 3
    # --------------------------------------------------------

    data['params']['func1step3description'] = scenarios[0]["helper_functions"][0]["steps"][2]
    answers = crop_image_answers(info,5)
    line_num = 'func1line'+str(3)
    data['params'][line_num] = answers




    # --------------------------------------------------------
    # FUNCTION 2
    # --------------------------------------------------------

    data['params']['func2name'] = scenarios[0]["helper_functions"][1]["function_name"]
    data['params']['func2shortdescription'] = scenarios[0]["helper_functions"][1]["short_description"]
    data['params']['func2description'] = scenarios[0]["helper_functions"][1]["description"]

   # create the parameter list of descriptions and the code to declare the arguments
    parameterList = ""
    for j in range(len(scenarios[0]["helper_functions"][1]["parameters"])):
        parameterList += str(j+1) + ". " + scenarios[0]["helper_functions"][1]["parameter_descriptions"][j] + " \r\n"


    # create the return value list of descriptions
    returnVarList = ""
    for j in range(len(scenarios[0]["helper_functions"][1]["return_variables"])):
        returnVarList += str(j+1) + ". " + scenarios[0]["helper_functions"][1]["return_variable_descriptions"][j] + " \r\n"

    data['params']['func2parameterList'] = parameterList
    data['params']['func2returnVarList'] = returnVarList

    # create the algorithm
    algorithm = ""
    for j in range(len(scenarios[0]["helper_functions"][1]["algorithm"])):
        algorithm += "* " + scenarios[0]["helper_functions"][1]["algorithm"][j] + " \r\n"

    data['params']['func2algorithm'] = algorithm


    # --------------------------------------------------------
    # STEP 1
    # --------------------------------------------------------

    data['params']['func2step1description'] = scenarios[0]["helper_functions"][1]["steps"][0]

    helper_function_info = scenarios[0]["helper_functions"][1]
    data['params']['helper2functionname'] = helper_function_info["function_name"]

    # all the parameter info
    i = 0
    while i < len(helper_function_info["parameters"]):
        temp = "helper2param"+str(i+1)
        data['params'][temp] = helper_function_info["parameters"][i]
        temp = "helper2param"+str(i+1)+"description"
        data['params'][temp] = helper_function_info["parameter_descriptions"][i]
        i += 1

    # all the return variable info
    i = 0
    while i < len(helper_function_info["return_variables"]):
        temp = "helper2rv"+str(i+1)
        data['params'][temp] = helper_function_info["return_variables"][i]
        temp = "helper2rv"+str(i+1)+"description"
        data['params'][temp] = helper_function_info["return_variable_descriptions"][i]
        i += 1


    answers = func_header_answers(helper_function_info,5)
    line_num = 'func2line'+str(1)
    data['params'][line_num] = answers



    # --------------------------------------------------------
    # STEP 2
    # --------------------------------------------------------

    data['params']['func2step2description'] = scenarios[0]["helper_functions"][1]["steps"][1]


    img = scenarios[0]["helper_functions"][1]["parameters"][0]
    channel_vars = [
        scenarios[0]["helper_functions"][1]["internal_variables"][0],
        scenarios[0]["helper_functions"][1]["internal_variables"][1],
        scenarios[0]["helper_functions"][1]["internal_variables"][2]
    ]
    answers = pull_out_channels_answers(img,channel_vars,5)
    line_num = 'func2line'+str(2)
    data['params'][line_num] = answers


    # --------------------------------------------------------
    # STEP 3
    # --------------------------------------------------------


    info = {
        "img": scenarios[0]["helper_functions"][1]["parameters"][0],
        "varStore": scenarios[0]["helper_functions"][1]["internal_variables"][3],
        "thresholds": [
            scenarios[0]["helper_functions"][1]["parameters"][1],
            scenarios[0]["helper_functions"][1]["parameters"][2],
            scenarios[0]["helper_functions"][1]["parameters"][3]
        ],
        "channel_vars": [
            scenarios[0]["helper_functions"][1]["internal_variables"][0],
            scenarios[0]["helper_functions"][1]["internal_variables"][1],
            scenarios[0]["helper_functions"][1]["internal_variables"][2]
        ],
        "comparisons": scenarios[0]["helper_functions"][1]["comparisons"],
        "combine": scenarios[0]["helper_functions"][1]["combine"]
    }


    data['params']['func2step3description'] = scenarios[0]["helper_functions"][1]["steps"][2]
    answers = select_image_pixels_answers(info,5)
    line_num = 'func2line'+str(3)
    data['params'][line_num] = answers


    # --------------------------------------------------------
    # STEP 4
    # --------------------------------------------------------


    info = {
        "img": scenarios[0]["helper_functions"][1]["parameters"][0],
        "channel_vars": [
            scenarios[0]["helper_functions"][1]["internal_variables"][0],
            scenarios[0]["helper_functions"][1]["internal_variables"][1],
            scenarios[0]["helper_functions"][1]["internal_variables"][2]
        ],
        "channel_index_vals": [ # leave as empty strings if updating the whole channel
            [ scenarios[0]["helper_functions"][1]["internal_variables"][3] ],
            [ scenarios[0]["helper_functions"][1]["internal_variables"][3] ],
            [ scenarios[0]["helper_functions"][1]["internal_variables"][3] ]
        ],
        "channel_values": [
            {
                "update": True,
                "correct": ["255"],
                "incorrect": [
                    ["0"+""],
                    ["1"+""],
                    ["255 ./ 2"+""],
                    ["max_brightness"+""]
                ]
            },
            {
                "update": True,
                "correct": ["255"+""],
                "incorrect": [
                    ["0"+""],
                    ["1"+""],
                    ["255 ./ 2"+""],
                    ["max_brightness"+""]
                ]
            },
            {
                "update": True,
                "correct": ["255"+""],
                "incorrect": [
                    ["0"+""],
                    ["1"+""],
                    ["255 ./ 2"+""],
                    ["max_brightness"+""]
                ]
            }
        ],
        "channel_values_the_same": True
    }

    data['params']['func2step4description'] = scenarios[0]["helper_functions"][1]["steps"][3]
    answers = set_channels_answers(info,5)
    line_num = 'func2line'+str(4)
    data['params'][line_num] = answers



    # --------------------------------------------------------
    # STEP 5
    # --------------------------------------------------------


    info = {
        "img": scenarios[0]["helper_functions"][1]["parameters"][0],
        "channel_vars": [
            scenarios[0]["helper_functions"][1]["internal_variables"][0],
            scenarios[0]["helper_functions"][1]["internal_variables"][1],
            scenarios[0]["helper_functions"][1]["internal_variables"][2]
        ],
        "channel_index_vals": [ # leave as empty strings if updating the whole channel
            [ ("~" + scenarios[0]["helper_functions"][1]["internal_variables"][3]) ],
            [ ("~" + scenarios[0]["helper_functions"][1]["internal_variables"][3]) ],
            [ ("~" + scenarios[0]["helper_functions"][1]["internal_variables"][3]) ]
        ],
        "channel_values": [
            {
                "update": True,
                "correct": ["0." + scenarios[0]["helper_functions"][1]["dim_value"] + " .* " + scenarios[0]["helper_functions"][1]["internal_variables"][0] + "(" + "~" + scenarios[0]["helper_functions"][1]["internal_variables"][3] + ")"],
                "incorrect": [
                    [scenarios[0]["helper_functions"][1]["dim_value"] + " .* " + scenarios[0]["helper_functions"][1]["internal_variables"][0] + "(" + "~" + scenarios[0]["helper_functions"][1]["internal_variables"][3] + ")"],
                    ["0." + scenarios[0]["helper_functions"][1]["dim_value"] + " .* " + scenarios[0]["helper_functions"][1]["internal_variables"][0] + "(" + scenarios[0]["helper_functions"][1]["internal_variables"][3] + ")"],
                    ["dim(" + scenarios[0]["helper_functions"][1]["dim_value"] + ")"],
                    [str(100-int(scenarios[0]["helper_functions"][1]["dim_value"])) + " .* " + scenarios[0]["helper_functions"][1]["internal_variables"][0] + "(" + "~" + scenarios[0]["helper_functions"][1]["internal_variables"][3] + ")"],
                    ["0." + str(100-int(scenarios[0]["helper_functions"][1]["dim_value"])) + " .* " + scenarios[0]["helper_functions"][1]["internal_variables"][0] + "(" + scenarios[0]["helper_functions"][1]["internal_variables"][3] + ")"],
                    ["dim(" + str(100-int(scenarios[0]["helper_functions"][1]["dim_value"])) + ")"]     
                ]
            },
            {
                "update": True,
                "correct": 
                    ["0." + scenarios[0]["helper_functions"][1]["dim_value"] + " .* " + scenarios[0]["helper_functions"][1]["internal_variables"][1] + "(" + "~" + scenarios[0]["helper_functions"][1]["internal_variables"][3] + ")"],
                    
                "incorrect": [
                    [scenarios[0]["helper_functions"][1]["dim_value"] + " .* " + scenarios[0]["helper_functions"][1]["internal_variables"][1] + "(" + "~" + scenarios[0]["helper_functions"][1]["internal_variables"][3] + ")"],

                    ["0." + scenarios[0]["helper_functions"][1]["dim_value"] + " .* " + scenarios[0]["helper_functions"][1]["internal_variables"][1] + "(" + scenarios[0]["helper_functions"][1]["internal_variables"][3] + ")"],

                    ["dim(" + scenarios[0]["helper_functions"][1]["dim_value"] + ")"],

                    [str(100-int(scenarios[0]["helper_functions"][1]["dim_value"])) + " .* " + scenarios[0]["helper_functions"][1]["internal_variables"][1] + "(" + "~" + scenarios[0]["helper_functions"][1]["internal_variables"][3] + ")"],

                    ["0." + str(100-int(scenarios[0]["helper_functions"][1]["dim_value"])) + " .* " + scenarios[0]["helper_functions"][1]["internal_variables"][1] + "(" + scenarios[0]["helper_functions"][1]["internal_variables"][3] + ")"],

                    ["dim(" + str(100-int(scenarios[0]["helper_functions"][1]["dim_value"])) + ")"]

                    ]
            },
            {
                "update": True,
                "correct": ["0." + scenarios[0]["helper_functions"][1]["dim_value"] + " .* " + scenarios[0]["helper_functions"][1]["internal_variables"][2] + "(" + "~" + scenarios[0]["helper_functions"][1]["internal_variables"][3] + ")"],
                "incorrect": [
                    [scenarios[0]["helper_functions"][1]["dim_value"] + " .* " + scenarios[0]["helper_functions"][1]["internal_variables"][2] + "(" + "~" + scenarios[0]["helper_functions"][1]["internal_variables"][3] + ")"],
                    ["0." + scenarios[0]["helper_functions"][1]["dim_value"] + " .* " + scenarios[0]["helper_functions"][1]["internal_variables"][2] + "(" + scenarios[0]["helper_functions"][1]["internal_variables"][3] + ")"],
                    ["dim(" + scenarios[0]["helper_functions"][1]["dim_value"] + ")"],
                    [str(100-int(scenarios[0]["helper_functions"][1]["dim_value"])) + " .* " + scenarios[0]["helper_functions"][1]["internal_variables"][2] + "(" + "~" + scenarios[0]["helper_functions"][1]["internal_variables"][3] + ")"],
                    ["0." + str(100-int(scenarios[0]["helper_functions"][1]["dim_value"])) + " .* " + scenarios[0]["helper_functions"][1]["internal_variables"][2] + "(" + scenarios[0]["helper_functions"][1]["internal_variables"][3] + ")"],
                    ["dim(" + str(100-int(scenarios[0]["helper_functions"][1]["dim_value"])) + ")"]
                    ]
            }
        ],
        "channel_values_the_same": False
    }

    data['params']['func2step5description'] = scenarios[0]["helper_functions"][1]["steps"][4]
    answers = set_channels_answers(info,5)
    line_num = 'func2line'+str(5)
    data['params'][line_num] = answers


    # --------------------------------------------------------
    # STEP 6
    # --------------------------------------------------------

    data['params']['func2step6description'] = scenarios[0]["helper_functions"][1]["steps"][5]


    img = scenarios[0]["helper_functions"][1]["parameters"][0]
    channel_vars = [
        scenarios[0]["helper_functions"][1]["internal_variables"][0],
        scenarios[0]["helper_functions"][1]["internal_variables"][1],
        scenarios[0]["helper_functions"][1]["internal_variables"][2]
    ]
    answers = copy_in_channels_answers(img,channel_vars,5)
    line_num = 'func2line'+str(6)
    data['params'][line_num] = answers
