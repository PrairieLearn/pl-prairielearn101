
def grade(data):
  
  feedback = "\n"


  feedback = feedback + "* Claim 1: "
  if data["partial_scores"]["ex1"]["score"] == 1:
    feedback = feedback + "**Correct!** The mean of the battery lifetimes at 0 years of use is greater than 3 hours, and the lower end of the error bar is also above 3 hours.   \n"
  else:
    feedback = feedback + "Incorrect. Incorrect. Look again at the graph, especially when the battery is new (0 years of use).   \n"

  feedback = feedback + "* Claim 2: "
  if data["partial_scores"]["ex2"]["score"] == 1:
    feedback = feedback + "**Correct!** The mean of the battery lifetimes at 2 years of use is greater than 2 hours, and the lower end of the error bar is also above 2 hours.   \n"
  else:
    feedback = feedback + "Incorrect. Look again at the graph, especially when the battery is at 2 years of use.   \n"

  feedback = feedback + "\n   \n   "

  # if they haven't answered the question correctly, give them feedback in the submissions box, otherwise, show the feedback in the answer box
  if data["score"] != 1:
    data["params"]["submission-feedback"] = feedback
  else:
    data["params"]["answer-feedback"] = feedback
    data["params"]["submission-feedback"] = ""



