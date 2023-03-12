

def grade(data):
  
  # if they haven't answered the question correctly, give them feedback in the submissions box, otherwise, show the feedback in the answer box
  if data["score"] != 1:
    data["params"]["submission-feedback"] = "Incorrect. \n\nFor Exercise 1, use at least 100,000 rolls in your simulation (1,000,000 would be better!), and then carefully watch the results as you run the script multiple times. If you don't want to run the simulation with even more rolls (to help with convergence), what's your best guess on the probability based on the results that you've gotten so far? \n\nFor Exercise 2, check your selections carefully and refer back to the `RollingTwoRegularDice.m` script for examples of what you're doing. "
  else:
    data["params"]["answer-feedback"] = "**Correct!**  "
    data["params"]["submission-feedback"] = ""