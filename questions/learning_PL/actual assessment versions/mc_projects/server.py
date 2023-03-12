import random
import string

def generate(data):


    scenarios = [
        {
            "question": "What day of the week are projects due?",
            "correct": "Tuesdays",
            "wrong": [ "Sundays","Mondays","Wednesdays", "Thursdays","Fridays", "Saturdays"]
        },
        {
            "question": "Should you start projects early?",
            "correct": "YES (please, please start them early)",
            "wrong": [ "no", "only if I'm bored", "maybe", "I don't need to do the projects" ]
        },
        {
            "question": "How many project redos do you get in ENGR 101?",
            "correct": "1",
            "wrong": [ "2", "as many as I want", "5", "6", "10"]
        }
    ]

    random.shuffle(scenarios)

    # -----------------------------------------------------------------------------------------
    # Save all the info to the params data structure so the question variant can be constructed
    # -----------------------------------------------------------------------------------------


    # question
    data['params']['question'] = scenarios[0]["question"]


    answers = []

    # add in correct answers
    answers.append({'tag': 'true', 'ans': scenarios[0]["correct"]})

    # add in wrong answers
    random.shuffle(scenarios[0]["wrong"])
    i = 0
    while i < 4: # have 4 wrong answers
        answers.append({'tag': 'false', 'ans': scenarios[0]["wrong"][i]})
        i += 1

    data['params']['answers'] = answers

 