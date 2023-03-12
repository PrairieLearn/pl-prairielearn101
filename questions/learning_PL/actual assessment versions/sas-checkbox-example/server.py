import random
import copy

def generate(data):

    scenarios = [
        {
            "description": "Here is a portion of the lyrics to the University of Michigan Fight Song, The Victors:",
            "song": "The Victors",
            "lyrics": [
                "Hail! to the victors valiant",
                "Hail! to the conquering heroes",
                "Hail! Hail! to Michigan",
                "The leaders and best!"
            ]
        },
        {
            "description": "Here is a portion of the lyrics to the University of Michigan Alma Mater, The Yellow and Blue:",
            "song": "The Yellow and Blue",
            "lyrics": [
                "Sing to the colors that float in the light;",
                "Hurrah for the Yellow and Blue!",
                "Yellow the stars as they ride through the night",
                "And reel in a rollicking crew;",
                "Yellow the field where ripens the grain",
                "And yellow the moon on the harvest wain;",
                "-Hail!"
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
    data['params']['song'] = scenarios[0]["song"]

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
    


