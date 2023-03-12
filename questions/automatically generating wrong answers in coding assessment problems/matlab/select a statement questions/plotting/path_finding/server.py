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
    from generatingAnswers import load_matfile_answers
    from generatingAnswers import store_vector_answers
    from generatingAnswers import clear_workspace_answers
    from generatingAnswers import close_figures_answers


    # ------------------------------------------------------------------------
    # DATA FOR THE PROBLEM -- JUST CHANGE THIS PART TO MAKE A NEW PROBLEM! :)
    # ------------------------------------------------------------------------

    scenarios = [
        {
            "company": {
                "name": "Ascrizzi Safety Solutions, Inc.",
                "specialty": "develops drones that can be deployed for disaster relief after earthquakes, tornadoes, fires, and other natural disasters. The drones are tested at the University of Michigan's M-City, a 32-acre outdoor laboratory designed for testing autonomous vehicles",
                "sensors": "GPS sensors",
                "sensor": "GPS sensor",
                "vehicle": "SOS-5 autonomous drone",
                "vehicleAbbr": "Drone",
                "testArea": "mcity.png"
            },
            "script": {
                "name": "AnalyzeDroneSensors",
                "xaxis_min": "40",
                "xaxis_max": "120",
                "yaxis_min": "0",
                "yaxis_max": "1.2",
                "yaxis_label": "Error (m)",
                "imgVar": "mCityMap"
            },
            "data": {
                "fileID": "droneAnalysis.png",
                "filename": "drone.mat",
                "color":"magenta",
                "var1": "xPosition",
                "var2": "yPosition",
                "var3": "obstacles",
                "var4": "numObstacles",
                "var5": "aSensor",
                "var6": "bSensor",
                "obstacle1": "buildings",
                "obstacle2": "signs"
            }
        }

    ]




    # ----------------------------------------------------------------
    # CREATE THE PROBLEM -- DON'T CHANGE ANYTHING FROM HERE ON DOWN
    # ----------------------------------------------------------------



    random.shuffle(scenarios)

    comments = [
        "clear the workspace and close all figures",
        "load the variables from the .mat file",
        "plot the path taken",
        "load the image of the testing area  \n   " + scenarios[0]["script"]["imgVar"] + " = imread('" + scenarios[0]["company"]["testArea"] + "');\n   [x, y, z] = size(" + scenarios[0]["script"]["imgVar"] + ");\n   h = image([0,y], [x,0], " + scenarios[0]["script"]["imgVar"] + "); \n   uistack(h,'bottom')\n   xlim([0 y])\n   ylim([0 x])",
        "plot obstacles using bar chart",
        "plot error vs. temperature using error bar plot",
        "--------- END OF SCRIPT ---------",
    ]


    # populate the scenario information
    data['params']['company_name'] = scenarios[0]["company"]["name"]
    data['params']['company_specialty'] = scenarios[0]["company"]["specialty"]
    data['params']['company_sensors'] = scenarios[0]["company"]["sensors"]
    data['params']['company_sensor'] = scenarios[0]["company"]["sensor"]
    data['params']['company_vehicle'] = scenarios[0]["company"]["vehicle"]
    data['params']['company_vehicleAbbr'] = scenarios[0]["company"]["vehicleAbbr"]
    data['params']['company_testArea'] = scenarios[0]["company"]["testArea"]

    data['params']['script_name'] = scenarios[0]["script"]["name"]
    data['params']['script_xaxis_min'] = scenarios[0]["script"]["xaxis_min"]
    data['params']['script_xaxis_max'] = scenarios[0]["script"]["xaxis_max"]
    data['params']['script_yaxis_min'] = scenarios[0]["script"]["yaxis_min"]
    data['params']['script_yaxis_max'] = scenarios[0]["script"]["yaxis_max"]
    data['params']['script_yaxis_label'] = scenarios[0]["script"]["yaxis_label"]
    data['params']['script_imgVar'] = scenarios[0]["script"]["imgVar"]

    data['params']['data_fileID'] = scenarios[0]["data"]["fileID"]
    data['params']['data_filename'] = scenarios[0]["data"]["filename"]
    data['params']['data_color'] = scenarios[0]["data"]["color"]
    data['params']['data_var1'] = scenarios[0]["data"]["var1"]
    data['params']['data_var2'] = scenarios[0]["data"]["var2"]
    data['params']['data_var3'] = scenarios[0]["data"]["var3"]
    data['params']['data_var4'] = scenarios[0]["data"]["var4"]
    data['params']['data_var5'] = scenarios[0]["data"]["var5"]
    data['params']['data_var6'] = scenarios[0]["data"]["var6"]
    data['params']['data_obstacle1'] = scenarios[0]["data"]["obstacle1"]
    data['params']['data_obstacle2'] = scenarios[0]["data"]["obstacle2"]









    # --------------------------------------------------------
    # clear workspace
    # --------------------------------------------------------

    data['params']['comment1'] = comments[0]

    # answers = clear_workspace_answers(3)
    # line_num = 'line'+str(1)+"a"
    # data['params'][line_num] = answers

    # answers = close_figures_answers(3)
    # line_num = 'line'+str(1)+"b"
    # data['params'][line_num] = answers

    # --------------------------------------------------------
    # load variables from .mat file
    # --------------------------------------------------------

    data['params']['comment2'] = comments[1]
  
    info =  [
        {
            "filename": scenarios[0]["data"]["filename"],
            "variable": scenarios[0]["data"]["var1"] + ", " + scenarios[0]["data"]["var2"] + ", " + scenarios[0]["data"]["var3"] + ", " + scenarios[0]["data"]["var4"] + ", " + scenarios[0]["data"]["var5"] + ", " + scenarios[0]["data"]["var6"],
        }
    ]

    answers = load_matfile_answers(info,0,3)
    line_num = 'line'+str(2)
    data['params'][line_num] = answers



    # --------------------------------------------------------
    # plot the path taken
    # --------------------------------------------------------

    data['params']['comment3'] = comments[2]
    data['params']['comment4'] = comments[3]

    # set up subplot

    info = {
        "function_name": "subplot", 
        "parameters": [],
        "return_variables": [],
        "arguments": ["3","2","[1:4]"], 
        "assignments": [],
        "distractor_functions": [],
        "distractor_variables":[
            "[1:6]",
            "[5:6]",
            "[1, 4]",
            "6"
            "1",
            "2",
            "3",
            "5"
        ]
    }  
    answers = func_call_answers(info,4)
    line_num = 'line'+str(3)+'a'
    data['params'][line_num] = answers


    # hold on
    correct = {'tag': 'true', 'ans': "hold on"}
    incorrect = [
        {'tag': 'false', 'ans': "hold off"},
        {'tag': 'false', 'ans': "hold"},
        {'tag': 'false', 'ans': "hold figure"},
    ]
    random.shuffle(incorrect)
    answers = [correct, incorrect[0]]
    line_num = 'line'+str(3)+'b'
    data['params'][line_num] = answers


    # plot the path
    info = {
        "function_name": "plot", 
        "parameters": ["x","y","line_options"],
        "return_variables": ["p"],
        "arguments": [ 
            scenarios[0]["data"]["var1"],
            scenarios[0]["data"]["var2"],
            "':'"
        ], 
        "assignments": ["p"],
        "distractor_functions": ["subplot","line","graph"],
        "distractor_variables":[
            "'--'",
            "'x'",
            "'" + scenarios[0]["data"]["color"] + "'",
        ]
    }  
    answers = func_call_answers(info,3)
    line_num = 'line'+str(3)+'c'
    data['params'][line_num] = answers


    # change line width
    correct = {'tag': 'true', 'ans': "p.LineWidth = 15;"}
    incorrect = [
        {'tag': 'false', 'ans': "LineWidth = 15;"},
    ]
    random.shuffle(incorrect)
    answers = [correct, incorrect[0]]
    line_num = 'line'+str(3)+'d'
    data['params'][line_num] = answers

    # change line color
    correct = {'tag': 'true', 'ans': "p.Color = '" + scenarios[0]["data"]["color"] + "';"}
    incorrect = [
        {'tag': 'false', 'ans': "p.Color = " + scenarios[0]["data"]["color"] + ";"},
        {'tag': 'false', 'ans': "p.LineColor = '" + scenarios[0]["data"]["color"] + "';"},
        {'tag': 'false', 'ans': "p.LineColor = " + scenarios[0]["data"]["color"] + ";"},
    
    ]
    random.shuffle(incorrect)
    answers = [correct, incorrect[0]]
    line_num = 'line'+str(3)+'e'
    data['params'][line_num] = answers    


    # hold off
    correct = {'tag': 'true', 'ans': "hold off"}
    incorrect = [
        {'tag': 'false', 'ans': "hold on"},
        {'tag': 'false', 'ans': "hold"},
        {'tag': 'false', 'ans': "release figure"},
    ]
    random.shuffle(incorrect)
    answers = [correct, incorrect[0]]
    line_num = 'line'+str(3)+'f'
    data['params'][line_num] = answers


    # add title
    correct = {'tag': 'true', 'ans': "t = title('Path Taken By " + scenarios[0]["company"]["vehicleAbbr"] + "');\nt.FontSize = 25;"}
    incorrect = [
        {'tag': 'false', 'ans': "t = title('Path Taken By " + scenarios[0]["company"]["vehicleAbbr"] + "');"},
        {'tag': 'false', 'ans': "t = figuretitle('Path Taken By " + scenarios[0]["company"]["vehicleAbbr"] + "');\nt.FontSize = 25;"},
        {'tag': 'false', 'ans': "t = figuretitle('Path Taken By " + scenarios[0]["company"]["vehicleAbbr"] + "');"},
    ]
    random.shuffle(incorrect)
    answers = [correct, incorrect[0]]
    line_num = 'line'+str(3)+'g'
    data['params'][line_num] = answers


    # # --------------------------------------------------------
    # # STEP 4
    # # --------------------------------------------------------

    data['params']['comment5'] = comments[4]

    # set up subplot

    info = {
        "function_name": "subplot", 
        "parameters": [],
        "return_variables": [],
        "arguments": ["3","2","5"], 
        "assignments": [],
        "distractor_functions": [],
        "distractor_variables":[
            "[1:4]",
            "[5:6]",
            "[1, 4]",
            "6"
            "1",
            "2",
            "3"
        ]
    }  
    answers = func_call_answers(info,3)
    line_num = 'line'+str(4)+'a'
    data['params'][line_num] = answers

    # make plot of obstacles

    info = {
        "function_name": "bar", 
        "parameters": ["items"],
        "return_variables": ["b"],
        "arguments": [scenarios[0]["data"]["var4"]], 
        "assignments": ["b"],
        "distractor_functions": ["column","plot"],
        "distractor_variables":[
            scenarios[0]["data"]["var3"],
            scenarios[0]["data"]["obstacle1"],
            scenarios[0]["data"]["obstacle2"],
            scenarios[0]["company"]["vehicleAbbr"]
        ]
    }  
    answers = func_call_answers(info,3)
    line_num = 'line'+str(4)+'b'
    data['params'][line_num] = answers


    # grid on (use xlabel as distractor)
    correct = {'tag': 'true', 'ans': "grid on"}
    incorrect = [
        {'tag': 'false', 'ans': "grid enable"},
        {'tag': 'false', 'ans': "background grid"}
    ]
    random.shuffle(incorrect)
    answers = [correct, incorrect[0],{'tag': 'false', 'ans': "xlabel('Types of Obstacles');"}]
    line_num = 'line'+str(4)+'c'
    data['params'][line_num] = answers

    # add xtick labels
    info = {
        "function_name": "xticklabels", 
        "parameters": ["labels"],
        "return_variables": [],
        "arguments": [scenarios[0]["data"]["var3"]], 
        "assignments": [],
        "distractor_functions": ["labels","axislabels"],
        "distractor_variables":[
            scenarios[0]["data"]["var4"],
            scenarios[0]["data"]["obstacle1"],
            scenarios[0]["data"]["obstacle2"],
            scenarios[0]["company"]["vehicleAbbr"]
        ]
    }  
    answers = func_call_answers(info,2)
    line_num = 'line'+str(4)+'d'
    data['params'][line_num] = answers

    # add yaxis label
    info = {
        "function_name": "ylabel", 
        "parameters": ["label"],
        "return_variables": [],
        "arguments": ["'number of obstacles'"], 
        "assignments": [],
        "distractor_functions": ["title","axistitle"],
        "distractor_variables":[
            "'obstacles'",
            scenarios[0]["data"]["obstacle1"],
            scenarios[0]["data"]["obstacle2"],
            scenarios[0]["company"]["vehicleAbbr"]
        ]
    }  
    answers = func_call_answers(info,2)
    line_num = 'line'+str(4)+'e'
    data['params'][line_num] = answers


    # # --------------------------------------------------------
    # # STEP 5
    # # --------------------------------------------------------

    data['params']['comment6'] = comments[5]

    # set up subplot

    info = {
        "function_name": "subplot", 
        "parameters": [],
        "return_variables": [],
        "arguments": ["3","2","6"], 
        "assignments": [],
        "distractor_functions": [],
        "distractor_variables":[
            "[1:4]",
            "[5:6]",
            "[1, 4]",
            "6"
            "1",
            "2",
            "3"
        ]
    }  
    answers = func_call_answers(info,3)
    line_num = 'line'+str(5)+'a'
    data['params'][line_num] = answers


    # hold on
    correct = {'tag': 'true', 'ans': "hold on"}
    incorrect = [
        {'tag': 'false', 'ans': "hold off"},
        {'tag': 'false', 'ans': "hold"},
        {'tag': 'false', 'ans': "hold figure"},
    ]
    random.shuffle(incorrect)
    answers = [correct, incorrect[0]]
    line_num = 'line'+str(5)+'b'
    data['params'][line_num] = answers


    # make errorbar plot
    correct = {'tag': 'true', 'ans': "errorbar(" + scenarios[0]["data"]["var5"] + "(:,1), " + scenarios[0]["data"]["var5"] + "(:,2), " + scenarios[0]["data"]["var5"] + "(:,3));\nerrorbar(" + scenarios[0]["data"]["var6"] + "(:,1), " + scenarios[0]["data"]["var6"] + "(:,2), " + scenarios[0]["data"]["var6"] + "(:,3));"}
    incorrect = [
        {'tag': 'false', 'ans': "errorbar(" + scenarios[0]["data"]["var5"] + "(1,:), " + scenarios[0]["data"]["var5"] + "(2,:), " + scenarios[0]["data"]["var5"] + "(3,:));\nerrorbar(" + scenarios[0]["data"]["var6"] + "(1,:), " + scenarios[0]["data"]["var6"] + "(2,:), " + scenarios[0]["data"]["var6"] + "(3,:));"},
        {'tag': 'false', 'ans': "bar(" + scenarios[0]["data"]["var5"] + "(:,1), " + scenarios[0]["data"]["var5"] + "(:,2));\nbar(" + scenarios[0]["data"]["var6"] + "(:,1), " + scenarios[0]["data"]["var6"] + "(:,2));"},
        {'tag': 'false', 'ans': "bar(" + scenarios[0]["data"]["var5"] + "(1,:), " + scenarios[0]["data"]["var5"] + "(2,:));\nbar(" + scenarios[0]["data"]["var6"] + "(1,:), " + scenarios[0]["data"]["var6"] + "(2,:));"},
        {'tag': 'false', 'ans': "errorbar(" + scenarios[0]["data"]["var5"] + "(:,1), " + scenarios[0]["data"]["var5"] + "(:,2));\nerrorbar(" + scenarios[0]["data"]["var6"] + "(:,1), " + scenarios[0]["data"]["var6"] + "(:,2));"},
        {'tag': 'false', 'ans': "errorbar(" + scenarios[0]["data"]["var5"] + "(1,:), " + scenarios[0]["data"]["var5"] + "(2,:));\nerrorbar(" + scenarios[0]["data"]["var6"] + "(1,:), " + scenarios[0]["data"]["var6"] + "(2,:));"}
    ]
    random.shuffle(incorrect)
    answers = [correct, incorrect[0]]
    line_num = 'line'+str(5)+'c'
    data['params'][line_num] = answers



    # hold off 
    correct = {'tag': 'true', 'ans': "hold off"}
    incorrect = [
        {'tag': 'false', 'ans': "hold on"},
        {'tag': 'false', 'ans': "hold"},
        {'tag': 'false', 'ans': "release figure"},
    ]
    random.shuffle(incorrect)
    answers = [correct, incorrect[0]]
    line_num = 'line'+str(5)+'d'
    data['params'][line_num] = answers


    # grid on (use title as distractor)
    correct = {'tag': 'true', 'ans': "grid on"}
    incorrect = [
        {'tag': 'false', 'ans': "grid enable"},
        {'tag': 'false', 'ans': "background grid"}
    ]
    random.shuffle(incorrect)
    answers = [correct, incorrect[0],{'tag': 'false', 'ans': "title('error vs. temperature');"}]
    line_num = 'line'+str(5)+'e'
    data['params'][line_num] = answers


    # legend
    correct = {'tag': 'true', 'ans': "legend('Sensor A', 'Sensor B');"}
    incorrect = [
        {'tag': 'false', 'ans': "legend on"},
        {'tag': 'false', 'ans': "legend = ['Sensor A', 'Sensor B'];"}
    ]
    random.shuffle(incorrect)
    answers = [correct, incorrect[0]]
    line_num = 'line'+str(5)+'f'
    data['params'][line_num] = answers

    # get axes object
    correct = {'tag': 'true', 'ans': "ax = gca;"}
    incorrect = [
        {'tag': 'false', 'ans': "gca;"},
        {'tag': 'false', 'ans': "gca = ax;"}
    ]
    random.shuffle(incorrect)
    answers = [correct, incorrect[0]]
    line_num = 'line'+str(5)+'g'
    data['params'][line_num] = answers


    # set axis limits
    correct = {'tag': 'true', 'ans': "ax.XLim = [" + scenarios[0]["script"]["xaxis_min"] + "," + scenarios[0]["script"]["xaxis_max"] + "];\nax.YLim = [" + scenarios[0]["script"]["yaxis_min"] + "," + scenarios[0]["script"]["yaxis_max"] + "];"}
    incorrect = [
        {'tag': 'false', 'ans': "ax.XLim = (" + scenarios[0]["script"]["xaxis_min"] + "," + scenarios[0]["script"]["xaxis_max"] + ");\nax.YLim = (" + scenarios[0]["script"]["yaxis_min"] + "," + scenarios[0]["script"]["yaxis_max"] + ");"},
        {'tag': 'false', 'ans': "XLim = (" + scenarios[0]["script"]["xaxis_min"] + "," + scenarios[0]["script"]["xaxis_max"] + ");\nYLim = (" + scenarios[0]["script"]["yaxis_min"] + "," + scenarios[0]["script"]["yaxis_max"] + ");"},
        {'tag': 'false', 'ans': "XLim = [" + scenarios[0]["script"]["xaxis_min"] + "," + scenarios[0]["script"]["xaxis_max"] + "];\nYLim = [" + scenarios[0]["script"]["yaxis_min"] + "," + scenarios[0]["script"]["yaxis_max"] + "];"}
    ]
    random.shuffle(incorrect)
    answers = [correct, incorrect[0]]
    line_num = 'line'+str(5)+'h'
    data['params'][line_num] = answers



    # label the axes
    correct = {'tag': 'true', 'ans': "xlabel('temperature (deg F)');\nylabel('" + scenarios[0]["script"]["yaxis_label"] + "');"}
    incorrect = [
        {'tag': 'false', 'ans': "xlabel('" + scenarios[0]["script"]["yaxis_label"] + "');\nylabel('temperature (deg F)');"},
        {'tag': 'false', 'ans': "labels('temperature (deg F)', '" + scenarios[0]["script"]["yaxis_label"] + "');"},
        {'tag': 'false', 'ans': "labels('" + scenarios[0]["script"]["yaxis_label"] + "', 'temperature (deg F)');"}
    ]
    random.shuffle(incorrect)
    answers = [correct, incorrect[0]]
    line_num = 'line'+str(5)+'i'
    data['params'][line_num] = answers

    data['params']['comment7'] = comments[6]