import random
import string
import copy

def generate(data):



    scenarios = [
        {
            "part1": "A great place to ask questions asynchronously in ENGR 101 is",
            "correct1": ["Piazza"],
            "wrong1": [ "The Diag", "The Grove", "Michigan Stadium", "The tennis courts by The Hill"],
            "part2": "which can be found ",
            "correct2": ["at the top of the course website (engr101.org)"],
            "wrong2": ["on Central Campus", "somewhere in Ann Arbor", "on South Campus", "in a parking lot"],
            "part3": "."
        },
        {
            "part1": "Using Piazza is a",
            "correct1": ["great"],
            "wrong1": [ "horrible", "atrocious", "spooky","ghastly", "absolutely ghoulish"],
            "part2": "way to post questions in ENGR 101. But remember that the ENGR 101 staff stop answering Piazza questions after",
            "correct2": ["10pm"],
            "wrong2": [ "they eat too many tacos", "it's time for a nap", "they run out of coffee","they go to the grocery store"],
            "part3": "so you will get answer the next day if you post your question late in the day. Or, perhaps a fellow student will be able to help you out!"
        }
    ]
    

    random.shuffle(scenarios)
    random.shuffle(scenarios[0]["wrong1"])
    random.shuffle(scenarios[0]["wrong2"])
    
    # -----------------------------------------------------------------------------------------
    # Save all the info to the params data structure so the question variant can be constructed
    # -----------------------------------------------------------------------------------------

    answers1  = []
    answers1.append({'tag': 'true', 'ans': scenarios[0]["correct1"][0]})
    i = 0
    while i < 2:
        answers1.append({'tag': 'false', 'ans': scenarios[0]["wrong1"][i]})
        i += 1

    answers2  = []
    answers2.append({'tag': 'true', 'ans': scenarios[0]["correct2"][0]})
    i = 0
    while i < 2:
        answers2.append({'tag': 'false', 'ans': scenarios[0]["wrong2"][i]})
        i += 1

    data['params']['part1'] = scenarios[0]["part1"]
    data['params']['answers1'] = answers1
    data['params']['part2'] = scenarios[0]["part2"]
    data['params']['answers2'] = answers2
    data['params']['part3'] = scenarios[0]["part3"]







