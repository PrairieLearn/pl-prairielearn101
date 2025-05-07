import random


def generate(data):
    options = [
        ["Warn when pointer is near cat", "forever"],
        ["Print ten rows", "repeat"],
        ["Read each line of a file", "repeat-until"],
    ]
    types = {option[1] for option in options}
    
    index = random.randint(1, len(options))
    option = options[index - 1]

    # Set the question variables
    data["params"]["description"] = option[0]
    data["params"]["correct"] = option[1]
    types.remove(option[1])
    distractors = list(types)
    data["params"]["wrong_1"] = distractors[0]
    data["params"]["wrong_2"] = distractors[1]
    