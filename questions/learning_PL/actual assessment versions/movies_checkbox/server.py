import random
import string

def generate(data):


    scenarios = [
        {
            "question": "Which of these movies got Dr. Alford interested in computer programming?",
            "correct": ["Hackers", "The Net"],
            "wrong": [ "The BBC version of Pride and Prejudice ", "Lord of the Rings", "3 Ninjas", "Gosford Park", "Silver Streak", "All the Marvel movies"]
        },
        {
            "question": "Which of these video games did Dr. Alford LOVE LOVE LOVE to play growing up?",
            "correct": ["Earthbound", "Super Mario RPG: Legend of the Seven Stars", "Legend of Zelda: A Link to the Past"],
            "wrong": [ "GoldenEye", "MarioKart 64", "Sonic the Hedgehog 3", "Super Mario World", "TecmoBowl"]
        },
        {
            "question": "What is Dr. Alford's favorite color?",
            "correct": ["yellow"],
            "wrong": [ "blue", "green", "teal", "red", "brown", "orange","purple","black","white","magenta","hot pink"]
        },
        {
            "question": "What did Dr. Alford major in for undergrad?",
            "correct": ["naval architecture & marine engineering (it's the best!!)"],
            "wrong": [ "mechanical engineering", "computer science", "aerospace engineering", "nuclear engineering and radiological science", "civil engineering", "material science and engineering","electrical engineering","computer engineering"]
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
    while i < (6 - len(scenarios[0]["correct"])):
        answers.append({'tag': 'false', 'ans': scenarios[0]["wrong"][i]})
        i += 1

    data['params']['answers'] = answers


