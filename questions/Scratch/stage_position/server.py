import random

def generate(data):
    # Range of (x,y) is [-max, max] (or [-100, 100] to [-500, 500])
    max = random.randint(1, 5) * 100
    # Get (x, y)
    x = random.randint(-1, 1)
    y = random.randint(-1, 1)

    labels = [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']]

    # Set the question variables
    data["params"]["label"] = labels[1 - y][1 + x]
    data["params"]["side"] = max * 2

    # Set the answers
    data["correct_answers"]["x"] = x * max
    data["correct_answers"]["y"] = y * max
