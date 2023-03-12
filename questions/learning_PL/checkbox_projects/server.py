import random
import string

def generate(data):


    scenarios = [
        {
            "question": "Which projects can you submit late for a small penalty (but still get an A)?",
            "correct": ["Project 1", "Project 2", "Project 3"],
            "wrong": [ "Project 4"]
        },
        {
            "question": "Which of these is good advice for doing well on the projects?",
            "correct": ["Start early", "Spend some time planning your program first, don't just start typing away at your code", "Read the specifications. Then, read them again!", "when you code, test your program as you go; that way, if something goes wrong, you know it's somewhere in the last 5 lines of code you just wrote"],
            "wrong": [ "Just start coding right away -- you'll figure out what's wrong later", "Don't bother planning or designing your program; it's a waste of time", "If you get stuck, just keep trying random things; no one will help you at office hours"]
        }
    ]
  
    random.shuffle(scenarios)


    # -----------------------------------------------------------------------------------------
    # Save all the info to the params data structure so the question variant can be constructed
    # -----------------------------------------------------------------------------------------

    # question
    data['params']['question'] = scenarios[0]["question"]

    # add in correct answers
    answers = []
    i = 0
    while i < len(scenarios[0]["correct"]):
        answers.append({'tag': 'true', 'ans': scenarios[0]["correct"][i]})
        i += 1

    # add in wrong answers
    random.shuffle(scenarios[0]["wrong"])
    i = 0
    while i < (4 - len(scenarios[0]["correct"])):
        answers.append({'tag': 'false', 'ans': scenarios[0]["wrong"][i]})
        i += 1

    data['params']['answers'] = answers


