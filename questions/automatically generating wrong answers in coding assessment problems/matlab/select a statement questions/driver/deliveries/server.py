import random
import copy




# ----------------------------------------------------------------
# PROBLEM DESCRIPTION
# ----------------------------------------------------------------

# This is a driver program that primarily analyzes data and makes a plot. 
# There are 6 steps to this driver program:
#   1. clear the workspace and close existing figures
#   2. load data from a file to a MATLAB table
#   3. analyze data using a helper function
#   4. simulate data (includes generating starter data and using meshgrid)
#   5. make a plot and save the plot
#   6. make a table and write the table



# This problem is about donut delivery. The original question was in the W21 MATLAB exam.






def generate(data):

    # ----------------------------------------------------------------
    # IMPORT FUNCTIONS FOR GENERATING ANSWERS
    # ----------------------------------------------------------------


    import sys
    sys.path.append(data["options"]["server_files_course_path"])
    from generatingAnswers import func_call_answers
    from generatingAnswers import make_return_variables
    from generatingAnswers import make_parameters
    from generatingAnswers import load_table_answers
    from generatingAnswers import store_vector_answers
    from generatingAnswers import write_table_answers
    from generatingAnswers import clear_workspace_answers
    from generatingAnswers import close_figures_answers


    # ------------------------------------------------------------------------
    # DATA FOR THE PROBLEM -- JUST CHANGE THIS PART TO MAKE A NEW PROBLEM! :)
    # ------------------------------------------------------------------------

    initialInfo = {
            "company_name": "Donut Delivery",
            "specialty": "delivering fresh, hot donuts to any location on Proxima B",
            "options": ["bicycle","scooter","motorcycle"],
            "script_name": "AnalyzeDonutDelivery",
            "data_description": "delivery",
            "sim_data_description": "rates",
            "task": "analyze the shipping rates for these delivery options based on the distance from the pick-up location to the drop-off location and the time from when the delivery order was placed to when the package was delivered",


            "input_images": [
                # { 
                #     "filename": "",
                #     "variable": "",
                #     "caption": "",
                #     "description": "",
                # },
            ],
            "output_images": [
                { 
                    "filename": "deliveryRates.png",
                    "variable": "",
                    "caption": "",
                },
                { 
                    "filename": "",
                    "variable": "",
                    "caption": "",
                }
            ],
            "data_input": [
                { 
                    "filename": "donutDeliveries.csv",
                    "variable": "data",
                    "description": "delivery data from the past month; includes the distance the item was shipped (in miles), the time it took to deliver the item (in minutes), and the cost for the delivery (in $PB -- Proxima b dollars)",
                    "image": "deliveriesSnapshot.png",

                    "distCol": "Distance",
                    "timeCol": "TravelTime",
                    "costCol": "Cost"
                },
            ],
            "plot_output": [
                { 
                    "filename": "deliveryRates.png",
                    "flag": "'-dpng'",
                    "variable": "",
                    "description": "a plot showing the relationship between distance, time, and estimated shipping cost",
                    "image": "deliveryRates.png",
                    
                    "cTicks_step": "10",
                    "cLabel": "cost to ship package ($PB)",
                    
                },
            ],
            "data_output": [
                { 
                    "filename": "deliveryRates.csv",
                    "variable": "rateTable",
                    "description": "a file that can be used as a \"look up table\" to see the estimated shipping costs for different combinations of distance and time",
                    "image": "deliveryRatesTable.png",


                },
            ],
            "starter_data": [
                {
                    "name": "distances",
                    "description": "distance",
                    "description_plural": "distances",
                    "values": [],
                    "start_range": "0",
                    "end_range": "80",
                    "step_size": "2",
                    "num_elements": "",
                    "type": "range_notation",
                    "units": "miles"
                },
                {
                    "name": "times",
                    "description": "time",
                    "description_plural": "times",
                    "values": [],
                    "start_range": "0",
                    "end_range": "35",
                    "step_size": "0.5",
                    "num_elements": "",
                    "type": "range_notation",
                    "units": "mins"
                }
            ],
            "meshgrid_data": [
                { 
                    "x_range" : "distances", # match above
                    "y_range" : "times", # match above
                    "x_mesh" : "D",
                    "y_mesh" : "T",
                }
            ],
        }


    # assemble information about helper functions

    # start with an empty list of helper functions
    helperfunctions = []

    # here's a helper function
    helper = {
        "function_name": "coefs",
        "description": "analyzes a vector of data and returns a vector of coefficients to be used in the simulation",
        "parameters": ["d", "t", "cost"],
        "parameter_descriptions": ["a vector of numerical values representing " + initialInfo["starter_data"][0]["description_plural"],"a vector of numerical values representing " + initialInfo["starter_data"][1]["description_plural"],"a vector of numerical values representing costs"],
        "return_variables": ["c"],
        "return_variable_descriptions": ["a vector of numerical values representing the coefficients needed for the simulation helper function"],
        "arguments": [ 
            initialInfo["data_input"][0]["variable"] + "." + initialInfo["data_input"][0]["distCol"], 
            initialInfo["data_input"][0]["variable"] + "." + initialInfo["data_input"][0]["timeCol"],
            initialInfo["data_input"][0]["variable"] + "." + initialInfo["data_input"][0]["costCol"]
        ],
        "assignments": ["c"],
        "example_call": ">> c = coefs([1 2 3], [2.8 9.5 1.2], [6.1 4.4 6.8])  \nc =  \n     0.903     0.207     -9.124     8.910  \n>> x = [30.0   16.5   22.5   30.0    9.0]  \n>> y = [ 3.0    6.0    1.5    9.0    6.0];  \n>> z = [ 7.2   24.0   12.0    6.0    8.4];  \n>> c = coefs(x,y,z)  \nc =  \n     5.932     -4.887     0.003     1.672"
    }
    helperfunctions.append(helper) # add this helper function to the list

    # here's a helper function
    helper = {
        "function_name": "simulateRates",
        "description": "analyzes a set of distances and times and returns a vector of estimated shipping rates",
        "parameters": [ initialInfo["meshgrid_data"][0]["x_mesh"], initialInfo["meshgrid_data"][0]["y_mesh"], helperfunctions[0]["assignments"][0]],
        "parameter_descriptions": ["a matrix of numerical values representing " + initialInfo["starter_data"][0]["description_plural"],"a matrix of numerical values representing " + initialInfo["starter_data"][1]["description_plural"],"a vector of numerical values representing the coefficients returned from the `" + helperfunctions[0]["function_name"] + "` function"],
        "return_variables": ["rates"],
        "return_variable_descriptions": ["a matrix of shipping rates that represents the estimated shipping rates for each " + initialInfo["starter_data"][0]["description"] + " and " + initialInfo["starter_data"][1]["description"] + " combination in the matrices that are passed in to each of the first two parameters"],
        "arguments": [ 
            initialInfo["meshgrid_data"][0]["x_mesh"], 
            initialInfo["meshgrid_data"][0]["y_mesh"],
            helperfunctions[0]["assignments"][0] 
        ],
        "assignments": ["deliveryRates"],
        "example_call": "% omitted: code that creates the X, Y, and c variables.  \n% They now have these values:  \nX =  \n   11.5200    1.2800   11.5200  \n    1.2800    6.4000    2.5600  \n    3.8400    1.2800    1.2800  \nY =  \n    9.5900   27.4000    2.7400  \n   13.7000    9.5900    8.2200  \n    4.1100    8.2200    1.3700  \nc =  \n     6.187     0.871     -3.334     -1.087  \n>> r = simulateRates(X,Y,c)  \nr =  \n    3.9800    4.6100    5.3800  \n    4.0100    4.6600    5.4400  \n    4.0300    4.6800    5.4700"
    }
    helperfunctions.append(helper) # add this helper function to the list

    # here's a helper function
    helper = {
        "function_name": "getLabels",
        "description": "adds a unit label to each numerical value in a vector",
        "parameters": ["v","units"],
        "parameter_descriptions": ["a vector of numerical values", "a string representing the units for those values"],
        "return_variables": ["labels"],
        "return_variable_descriptions": ["a cell array containing strings consisting of the numerical value with its units"],
        "arguments1": [initialInfo["starter_data"][0]["name"],"'" + initialInfo["starter_data"][0]["units"] + "'" ], # this gets called twice, so handle this separately
        "assignments1": [initialInfo["starter_data"][0]["description"] + "Labels" ], # this gets called twice, so handle this separately,
        "arguments2": [initialInfo["starter_data"][1]["name"],"'" + initialInfo["starter_data"][1]["units"] + "'" ], # this gets called twice, so handle this separately
        "assignments2": [initialInfo["starter_data"][1]["description"] + "Labels" ], # this gets called twice, so handle this separately,
        "example_call": ">> x = [ 1 2 3 ];  \n>> y = getLabels(x', 'Newtons')  \ny =  \n  3×1 cell array  \n    {'1 Newtons'}  \n    {'2 Newtons'}  \n    {'3 Newtons'}  \n>> z = getLabels(x','cats')  \nz =  \n  3×1 cell array  \n    {'1 cats'}  \n    {'2 cats'}  \n    {'3 cats'}",
    }

    helperfunctions.append(helper) # add this helper function to the list

    outline = {
        "steps": [
            "Clear workspace and close figures",
            "Read in data",
            "Analyze Data",
            "Simulate Data",
            "Display Plot",
            "Create Table",
        ],
        "additional_comments": [
            "create starter data vectors",
            "create matrices to represent all combinations of " + initialInfo["starter_data"][0]["description"] + " and " + initialInfo["starter_data"][1]["description"],
            "call " + helperfunctions[1]["function_name"] + " function to simulate rates",
            "round the rates to nearest hundredth",
            "make plot",
            "annotate plot",
            "access the colorbar graphic object so we can \n   % change some of its properties \n   c = colorbar;",
            "(more annotations to make the plot look nice;\n   % these lines not shown for the sake of brevity and \n   % because there's a different question on plotting \n   % so we don't need to do more of that plotting stuff here)",
            "save the plot as " + initialInfo["plot_output"][0]["filename"],
            "use the " + helperfunctions[2]["function_name"] + " function to generate labels for the rate table",
            "create the first column (with the time labels) \n   % and the rest of the columns (with the rates) \n   firstColumn = table(timeLabels,'VariableNames',{'Rates ($PB)'}); \n   colRates = array2table(" + helperfunctions[0]["assignments"][0] + "); \n   colRates.Properties.VariableNames = distLabels;",
            "combine the first column with the rest of the columns \n   % to create the rate table",
            "save the rate table as a .csv file",
            "%----------------- END OF SCRIPT -----------------"
        ],
        "algorithm": [
            "Clear the workspace of any existing variables and close all figures that may be open. This way, there will be no existing information that might interfere with this script. ",
            "Load the " + initialInfo["data_description"] + " data from the `" + initialInfo["data_input"][0]["filename"]+ "` file.", 
            "Call the `" + helperfunctions[0]["function_name"] + "` helper function to determine the coefficients needed for the simulation; pass in table columns `" + initialInfo["data_input"][0]["distCol"] + "`, `" + initialInfo["data_input"][0]["timeCol"] + "`, and `" + initialInfo["data_input"][0]["costCol"] + "`.",
            "Create starter data vectors for " + initialInfo["starter_data"][0]["description"] + " and " + initialInfo["starter_data"][1]["description"] + ":  \n* " + initialInfo["starter_data"][0]["description"] + " should be from " + initialInfo["starter_data"][0]["start_range"] + " to " + initialInfo["starter_data"][0]["end_range"] + " with a step size of " + initialInfo["starter_data"][0]["step_size"] + "  \n* " + initialInfo["starter_data"][1]["description"] + " should be from " + initialInfo["starter_data"][1]["start_range"] + " to " + initialInfo["starter_data"][1]["end_range"] + " with a step size of " + initialInfo["starter_data"][1]["step_size"] + "  \n\nCreate matrices that represent all the combinations of "+ initialInfo["starter_data"][0]["description"] + " and "+ initialInfo["starter_data"][1]["description"] + " in the starter data vectors.  \n\nCall the `" + helperfunctions[1]["function_name"] + "` helper function to simulate " + initialInfo["sim_data_description"] + " using the coefficients and the starter data matrices representing all combinations of " + initialInfo["starter_data"][0]["description"] + " and " + initialInfo["starter_data"][1]["description"] + ".  \nRound the simulated " + initialInfo["sim_data_description"] + " to the nearest hundredth.",
            "Plot the simulated data as shown in the sample figure.  \n\nAnnotate the plot as shown in the sample figure; for the color bar, use tick marks that are every " + initialInfo["plot_output"][0]["cTicks_step"] + " $PB.  \n\nSave the plot as a `.png` file.",
            "Use the `" + helperfunctions[2]["function_name"] + "` helper function to create labels for the simulated data; include information about the units for both " + initialInfo["starter_data"][0]["description"] + " and " + initialInfo["starter_data"][1]["description"] + ".  \n\nCreate a table that has one column: the " + initialInfo["starter_data"][1]["description"] + " labels; create another table that has the simulated data with " + initialInfo["starter_data"][0]["description"] + " labels as column names ***(this step is done for you)***  \n\nCombine these two tables into one table that can be used as a reference table for the employees at *" + initialInfo["company_name"] + "*  \n\nSave the reference table as a `.csv` file."
        ],
    }

    # make an empty scenarios list
    scenarios = []

    # start a scenario with the initial info
    scenario = initialInfo

    # add items to the dictionary
    scenario["helper_functions"] = helperfunctions
    scenario["steps"] = outline["steps"]
    scenario["additional_comments"] = outline["additional_comments"]
    scenario["algorithm"] = outline["algorithm"]

    # add the dictionary to the scenarios vector
    scenarios.append(scenario)


    # ----------------------------------------------------------------
    # CREATE THE PROBLEM -- DON'T CHANGE ANYTHING FROM HERE ON DOWN
    # ----------------------------------------------------------------



    random.shuffle(scenarios)




    # populate the scenario information
    data['params']['company_name'] = scenarios[0]["company_name"]
    # data['params']['image_in'] = scenarios[0]["input_images"][0]["filename"]
    data['params']['task'] = scenarios[0]["task"]
    data['params']['specialty'] = scenarios[0]["specialty"]
    # data['params']['intro'] = scenarios[0]["intro"]
    for j in range(len(scenarios[0]["options"])):
        paramName = 'option'+str(j+1)
        data['params'][paramName] = scenarios[0]["options"][j]


    data['params']['plot_x_units'] = scenarios[0]["starter_data"][0]["units"]
    data['params']['plot_y_units'] = scenarios[0]["starter_data"][1]["units"]

    data['params']['data_in_filename'] = scenarios[0]["data_input"][0]["filename"]
    data['params']['data_in_image'] = scenarios[0]["data_input"][0]["image"]
    data['params']['data_in_caption'] = scenarios[0]["data_input"][0]["description"]

    data['params']['data_out_filename'] = scenarios[0]["data_output"][0]["filename"]
    data['params']['data_out_image'] = scenarios[0]["data_output"][0]["image"]
    data['params']['data_out_caption'] = scenarios[0]["data_output"][0]["description"]

    data['params']['plot_out_image'] = scenarios[0]["plot_output"][0]["image"]
    data['params']['plot_out_caption'] = scenarios[0]["plot_output"][0]["description"]

    data['params']['data_description'] = scenarios[0]["data_description"],
    
    data['params']['image_out_1'] = scenarios[0]["output_images"][0]["filename"]
    data['params']['image_out_2'] = scenarios[0]["output_images"][1]["filename"]
    data['params']['image_out_1_caption'] = scenarios[0]["output_images"][0]["caption"]
    data['params']['image_out_2_caption'] = scenarios[0]["output_images"][1]["caption"]

    data['params']['additional_comments'] = scenarios[0]["additional_comments"]



    # create the algorithm for the question file
    script_steps = []
    for j in range(len(scenarios[0]["steps"])):
        # make a set of ALL CAPS steps for the script outline
        script_steps.append(copy.deepcopy(scenarios[0]["steps"][j]))
        script_steps[j] = script_steps[j].upper()

    algorithm = ""
    for j in range(len(scenarios[0]["algorithm"])):
        algorithm += "**" + script_steps[j] + "**  \n"
        algorithm += scenarios[0]["algorithm"][j] + "  \n\n"

    data['params']['script_algorithm'] = algorithm


    # save all the intermediate comments
    for j in range(len(scenarios[0]["additional_comments"])):
        paramName = 'comment'+str(j+1)
        data['params'][paramName] = scenarios[0]["additional_comments"][j]

    # save all the information about the helper functions


    # helper function #1 

    info = scenarios[0]["helper_functions"][0]
    data['params']['func1name'] = info["function_name"]
    data['params']['func1description'] = info["description"]
    data['params']['func1example'] = info["example_call"]

    # create the parameter list of descriptions and the code to declare the arguments
    parameterList = ""
    for j in range(len(info["parameters"])):
        parameterList += str(j+1) + ". " + info["parameter_descriptions"][j] + " \r\n"

    # create the return value list of descriptions
    returnVarList = ""
    for j in range(len(info["return_variables"])):
        returnVarList += str(j+1) + ". " + info["return_variable_descriptions"][j] + " \r\n"

    # create the function header
    header = "function "
    header += make_return_variables(info["return_variables"],info["parameters"],True)
    header += " = " + info["function_name"]
    header += make_parameters(info["return_variables"],info["parameters"],True)

    data['params']['func1parameterList'] = parameterList
    data['params']['func1returnVarList'] = returnVarList
    data['params']['func1header'] = header



    # helper function #2 

    info = scenarios[0]["helper_functions"][1]

    data['params']['func2name'] = info["function_name"]
    data['params']['func2description'] = info["description"]
    data['params']['func2example'] = info["example_call"]

    # create the parameter list of descriptions and the code to declare the arguments
    parameterList = ""
    for j in range(len(info["parameters"])):
        parameterList += str(j+1) + ". " + info["parameter_descriptions"][j] + " \r\n"

    # create the return value list of descriptions
    returnVarList = ""
    for j in range(len(info["return_variables"])):
        returnVarList += str(j+1) + ". " + info["return_variable_descriptions"][j] + " \r\n"

    # create the function header
    header = "function "
    header += make_return_variables(info["return_variables"],info["parameters"],True)
    header += " = " + info["function_name"]
    header += make_parameters(info["return_variables"],info["parameters"],True)

    data['params']['func2parameterList'] = parameterList
    data['params']['func2returnVarList'] = returnVarList
    data['params']['func2header'] = header





    # helper function #3 

    info = scenarios[0]["helper_functions"][2]

    data['params']['func3name'] = scenarios[0]["helper_functions"][2]["function_name"]
    data['params']['func3description'] = scenarios[0]["helper_functions"][2]["description"]
    data['params']['func3example'] = info["example_call"]

    # create the parameter list of descriptions and the code to declare the arguments
    parameterList = ""
    for j in range(len(scenarios[0]["helper_functions"][2]["parameters"])):
        parameterList += str(j+1) + ". " + scenarios[0]["helper_functions"][2]["parameter_descriptions"][j] + " \r\n"

    # create the return value list of descriptions
    returnVarList = ""
    for j in range(len(scenarios[0]["helper_functions"][2]["return_variables"])):
        returnVarList += str(j+1) + ". " + scenarios[0]["helper_functions"][2]["return_variable_descriptions"][j] + " \r\n"

    # create the function header
    header = "function "
    header += make_return_variables(info["return_variables"],info["parameters"],True)
    header += " = " + info["function_name"]
    header += make_parameters(info["return_variables"],info["parameters"],True)

    data['params']['func3parameterList'] = parameterList
    data['params']['func3returnVarList'] = returnVarList
    data['params']['func3header'] = header






    # make helper function list
    helperFunctionList = ""
    for j in range(len(scenarios[0]["helper_functions"])):
        helperFunctionList += "* `" + scenarios[0]["helper_functions"][j]["function_name"] + "()` \r\n"
    data['params']['helperFunctionList'] = helperFunctionList



    # make input files list
    inputFilesList = ""
    for j in range(len(scenarios[0]["input_images"])):
        inputFilesList += "* `" + scenarios[0]["input_images"][j]["filename"] + "` -- " + scenarios[0]["input_images"][j]["description"] + " \r\n"
    for j in range(len(scenarios[0]["data_input"])):
        inputFilesList += "* `" + scenarios[0]["data_input"][j]["filename"] + "` -- " + scenarios[0]["data_input"][j]["description"] + " \r\n"
    data['params']['inputFilesList'] = inputFilesList




    # --------------------------------------------------------
    # STEP 1
    # --------------------------------------------------------

    data['params']['step1description'] = scenarios[0]["steps"][0]
    answers = clear_workspace_answers(3)
    line_num = 'line'+str(1)+"a"
    data['params'][line_num] = answers

    answers = close_figures_answers(3)
    line_num = 'line'+str(1)+"b"
    data['params'][line_num] = answers

    # --------------------------------------------------------
    # STEP 2
    # --------------------------------------------------------

    data['params']['step2description'] = scenarios[0]["steps"][1]

    info = scenarios[0]["data_input"]
    answers = load_table_answers(info,0,3)
    line_num = 'line'+str(2)
    data['params'][line_num] = answers



    # --------------------------------------------------------
    # STEP 3
    # --------------------------------------------------------

    data['params']['step3description'] = scenarios[0]["steps"][2]


    helper_function_info = scenarios[0]["helper_functions"][0]

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


    answers = func_call_answers(helper_function_info,3)
    line_num = 'line'+str(3)
    data['params'][line_num] = answers





    # --------------------------------------------------------
    # STEP 4
    # --------------------------------------------------------

    data['params']['step4description'] = scenarios[0]["steps"][3]


    info = scenarios[0]["starter_data"][0]
    answers = store_vector_answers(info,"range_notation",3)
    line_num = 'line'+str(4)+'a'
    data['params'][line_num] = answers

    info = scenarios[0]["starter_data"][1]
    answers = store_vector_answers(info,"range_notation",3)
    line_num = 'line'+str(4)+'b'
    data['params'][line_num] = answers

    info = {
    "function_name": "meshgrid", 
    "parameters": [scenarios[0]["meshgrid_data"][0]["x_range"],scenarios[0]["meshgrid_data"][0]["y_range"]],
    "return_variables": [scenarios[0]["meshgrid_data"][0]["x_mesh"],scenarios[0]["meshgrid_data"][0]["y_mesh"]],
    "arguments": [scenarios[0]["meshgrid_data"][0]["x_range"],scenarios[0]["meshgrid_data"][0]["y_range"]], 
    "assignments": [scenarios[0]["meshgrid_data"][0]["x_mesh"],scenarios[0]["meshgrid_data"][0]["y_mesh"]],
    "distractor_functions": ["mesh", "combinations"],
    "distractor_variables":[
        scenarios[0]["helper_functions"][0]["arguments"][0],
        scenarios[0]["helper_functions"][0]["arguments"][1],
    ]
    }  
    answers = func_call_answers(info,3)
    line_num = 'line'+str(4)+'c'
    data['params'][line_num] = answers



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

    answers = func_call_answers(helper_function_info,4)
    line_num = 'line'+str(4)+'d'
    data['params'][line_num] = answers




    info = {
    "function_name": "round", 
    "parameters": [scenarios[0]["helper_functions"][1]["assignments"][0],"2"],
    "return_variables": [scenarios[0]["helper_functions"][1]["assignments"][0]],
    "arguments": [scenarios[0]["helper_functions"][1]["assignments"][0],"2"], 
    "assignments": [scenarios[0]["helper_functions"][1]["assignments"][0]],
    "distractor_functions": ["floor", "ceiling"],
    "distractor_variables":[
        "'hundredths'",
    ]
    }  
    answers = func_call_answers(info,3)
    line_num = 'line'+str(4)+'e'
    data['params'][line_num] = answers





    # --------------------------------------------------------
    # STEP 5
    # --------------------------------------------------------

    data['params']['step5description'] = scenarios[0]["steps"][4]

    info = {
    "function_name": "contourf", 
    "parameters": ["X", "Y", "Z"],
    "return_variables": ["plot"],
    "arguments": [scenarios[0]["meshgrid_data"][0]["x_mesh"],scenarios[0]["meshgrid_data"][0]["y_mesh"],scenarios[0]["helper_functions"][1]["assignments"][0]], 
    "assignments": [],
    "distractor_functions": ["contour", "plot", "mesh"],
    "distractor_variables":[
        scenarios[0]["meshgrid_data"][0]["x_range"],
        scenarios[0]["meshgrid_data"][0]["y_range"],
        scenarios[0]["helper_functions"][0]["assignments"][0]
    ]
    }  
    answers = func_call_answers(info,3)
    line_num = 'line'+str(5)+'a'
    data['params'][line_num] = answers


    # these next steps are just labeling the axes, and there's not many ways to mess that up, so just list the two options for each step
    answers = [
    {
        "tag": "true", 
        "ans": "xlabel('" + scenarios[0]["starter_data"][0]["description"] + " (" + scenarios[0]["starter_data"][0]["units"] + ")');\nylabel('" + scenarios[0]["starter_data"][1]["description"] + " (" + scenarios[0]["starter_data"][1]["units"] + ")');"
    },
    {
        "tag": "false", 
        "ans": "xlabel = '" + scenarios[0]["starter_data"][0]["description"] + " (" + scenarios[0]["starter_data"][0]["units"] + ")';\nylabel = '" + scenarios[0]["starter_data"][1]["description"] + " (" + scenarios[0]["starter_data"][1]["units"] + ")';"
    }
    ]
    line_num = 'line'+str(5)+'b'
    data['params'][line_num] = answers


    answers = [
    {
        "tag": "true", 
        "ans": "c.Label.String = '" + scenarios[0]["plot_output"][0]["cLabel"] + "'; "
    },
    {
        "tag": "false", 
        "ans": "c.Label.String = " + scenarios[0]["plot_output"][0]["cLabel"] + "; "
    }
    ]
    line_num = 'line'+str(5)+'c'
    data['params'][line_num] = answers

    answers = [
    {
        "tag": "true", 
        "ans": "c.Ticks = ([min(" + scenarios[0]["helper_functions"][1]["assignments"][0] + "(:)) : " + scenarios[0]["plot_output"][0]["cTicks_step"] + " : max(" + scenarios[0]["helper_functions"][1]["assignments"][0] + "(:))]); "
    },
    {
        "tag": "false", 
        "ans": "c.Ticks = ([min(" + scenarios[0]["helper_functions"][1]["assignments"][0] + "(:)) : max(" + scenarios[0]["helper_functions"][1]["assignments"][0] + "(:))]); "
    }
    ]
    line_num = 'line'+str(5)+'d'
    data['params'][line_num] = answers



    info = {
    "function_name": "print", 
    "parameters": ["filename", "setting"],
    "return_variables": [],
    "arguments": [scenarios[0]["plot_output"][0]["filename"],scenarios[0]["plot_output"][0]["flag"]], 
    "assignments": [],
    "distractor_functions": ["save", "imwrite", "figwrite"],
    "distractor_variables":[
        scenarios[0]["meshgrid_data"][0]["x_range"],
        scenarios[0]["meshgrid_data"][0]["y_range"],
        scenarios[0]["helper_functions"][0]["assignments"][0]
    ]
    }  

    answers = func_call_answers(info,3)
    line_num = 'line'+str(5)+'e'
    data['params'][line_num] = answers

    # --------------------------------------------------------
    # STEP 6
    # --------------------------------------------------------

    data['params']['step6description'] = scenarios[0]["steps"][5]


    helper_function_info = scenarios[0]["helper_functions"][2]

    # grab the first set of arguments/assignments
    helper_function_info["arguments"] = helper_function_info["arguments1"]
    helper_function_info["assignments"] = helper_function_info["assignments1"]


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


    answers = func_call_answers(helper_function_info,3)
    line_num = 'line'+str(6)+'a'
    data['params'][line_num] = answers


    # grab the second set of arguments/assignments
    helper_function_info["arguments"] = helper_function_info["arguments2"]
    helper_function_info["assignments"] = helper_function_info["assignments2"]


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


    answers = func_call_answers(helper_function_info,3)
    line_num = 'line'+str(6)+'b'
    data['params'][line_num] = answers






    
    info = {
        "name": scenarios[0]["data_output"][0]["variable"] ,
        "values": ["firstColumn","colRates"],
    }

    answers = store_vector_answers(info,"by_value",2)
    line_num = 'line'+str(6)+'c'
    data['params'][line_num] = answers

    info = {
        "filename": scenarios[0]["data_output"][0]["filename"],
        "variable": scenarios[0]["data_output"][0]["variable"]
    }

    answers = write_table_answers(info,3)
    line_num = 'line'+str(6)+'d'
    data['params'][line_num] = answers

