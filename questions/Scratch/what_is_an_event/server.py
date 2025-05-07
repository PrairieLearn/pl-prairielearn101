import random

def generate(data):
    prompts = ["when [flag] clicked", "when ___ key pressed", "when this sprite clicked", "when backdrop switches to ___", "when ___ > ___"]
    index = random.randint(0, len(prompts) - 1)
    # Set the question variables
    data["params"]["prompt"] = prompts[index]

def grade(data):
    # Get the answer
    answer = data["submitted_answers"]["string_value"].lower()
    data["score"] = 1 if answer == "event" or answer == "events" else 0
