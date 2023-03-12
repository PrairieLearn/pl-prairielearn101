import random
import string

def generate(data):


    scenarios = [
        {
            "question": "Who is Dr. Alford's favorite Avenger?",
            "correct": "Hawkeye",
            "wrong": [ "Black Widow", "Iron Man", "Hulk", "Thor", "Black Panther", "Okoye", "Scarlet Witch", "Ant-Man", "The Wasp", "Captain Marvel", "Spider-Man"]
        },
        {
            "question": "How many times has Dr. Alford watched the BBC version of Pride and Prejudice?",
            "correct": "probably more than 50 times... she's very proud",
            "wrong": [ "1", "4-5", "10ish", "20?", "2-3", "30?"]
        },
        {
            "question": "How many times has Dr. Alford watched the BBC version of Pride and Prejuidice?",
            "correct": "probably more than 50 times... she's very proud",
            "wrong": [ "1", "4-5", "10ish", "20?", "2-3", "30?"]
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

 