import random
import copy

def generate(data):

    scenarios = [
        {
            "description": "Prof. Alford really loves tacos. One time, she had tacos for breakfast, lunch, AND dinner -- what a great day! Here is Prof. Alford's process for making a basic taco that she likes:",
            "process": "making tacos",
            "lyrics": [
                "Put a tortilla on a plate",
                "Add some lettuce",
                "Add some tomatoes",
                "Add some seasoned ground beef",
                "Add some thousand island dressing (no joke -- it's good!)",
                "Add lots of hot sauce"
            ]
        },
        {
            "description": "Prof. Alford really loves tacos, including fajitas! Here is Dr. Alford's process for making a basic fajita/taco that she likes",
            "process": "making fajitas",
            "lyrics": [
                "Put a tortilla on a plate",
                "Add some fajita meat",
                "Add some sauteed peppers and onions",
                "Add some guacamole",
                "Add some thousand island dressing (no joke -- it's good!)",
                "Add lots of hot sauce"
            ]
        }
    ]

    random.shuffle(scenarios)

    data['params']['description'] = scenarios[0]["description"]


    ALL_LYRICS = []
    display_lyrics = ""
    i = 0
    while i < len(scenarios[0]["lyrics"]):
        ALL_LYRICS.append({'tag': 'false', 'ans': scenarios[0]["lyrics"][i]})
        display_lyrics += "*" + scenarios[0]["lyrics"][i] + "*\n\n"
        i += 1
    data['params']['lyrics'] = display_lyrics
    data['params']['process'] = scenarios[0]["process"]

    # assemble answers
    i = 0
    while i < len(scenarios[0]["lyrics"]):
        answers = copy.deepcopy(ALL_LYRICS)
        answers[i]['tag'] = 'true'

        #get a random wrong line to remove
        while len(answers) > 6:
            j = random.randrange(0,len(answers)) 
            if answers[j]['tag'] == 'false':
                answers.pop(j)

        line_num = 'line'+str(i+1)
        data['params'][line_num] = answers
        i += 1
    


