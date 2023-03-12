
def grade(data):


  if data["score"] == 1:
    data["params"]["answer-feedback"] = "Correct!"
    data["params"]["submission-feedback"] = ""
  else: 
    data["params"]["submission-feedback"] = "At least one of your answers is incorrect. For Exercise 1, double check your answers and refer back to the algorithm to make sure you didn't miss anything. You can also watch the walkthrough video to check your work. For Exercise 2, try typing each of the options in MATLAB and then check the Workspace window to see what starter data was created."