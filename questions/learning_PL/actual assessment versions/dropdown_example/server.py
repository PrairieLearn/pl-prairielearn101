import random
import string
import copy

def generate(data):



    scenarios = [
        {
            "part1": "A great place to go to get help in ENGR 101 is ",
            "correct1": ["office hours"],
            "wrong1": [ "Panda Express", "Mujo Cafe", "Bursley", "the sand volleyball court"],
            "part2": "which are located in ",
            "correct2": ["B521 Pierpont"],
            "wrong2": ["Pierpont", "The Duderstadt Center (aka The Dude)", "1931 Duffield St.", "in The Grove on North Campus"],
            "part3": "."
        },
        {
            "part1": "Office hours are a",
            "correct1": ["great"],
            "wrong1": [ "terrible", "awful", "dreadful","ghastly", "absolutely ghoulish"],
            "part2": "place to get help in ENGR 101. But beware! Office hours can get really",
            "correct2": ["busy"],
            "wrong2": [ "empty", "quiet", "spookily unattended","strangely idle"],
            "part3": "right before a project is due, and you might have to wait a long time to talk to one of the ENGR staff. So, make sure to start projects early!"
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







