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
            "question": "Can I submit projects late?",
            "correct": "Yes, and there will be a small penalty, but I can still earn an A! Except for Project 4 -- Project 4 is not eligible for late submission becuase it is due at the end of the semester.",
            "wrong": [ "Yes, and there is no penalty, so that's nice!", "No, unfortunately you cannot submit projects late.", "No, but you can ask for a project redo.", "No, so you should make sure to copy someone else's code to make sure that you get an A."]
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

 