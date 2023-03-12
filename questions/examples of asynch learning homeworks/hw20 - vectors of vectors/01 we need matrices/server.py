def grade(data):
  
  feedback = "\n"

  
  if data["partial_scores"]["ex1"]["score"] == 1:
    feedback = feedback + "**Correct!** This data is all about the same thing (snowfall), and we will likely want to do some analysis with all the data, so we want to be able to store it in one variable."
  else:
    feedback = feedback + "Try again: there is a better option, even if we don't know how to code it up quite yet!     \n"

  

  feedback = feedback + "\n   \n   "

  # if they haven't answered the question correctly, give them feedback in the submissions box, otherwise, show the feedback in the answer box
  if data["score"] != 1:
    data["params"]["submission-feedback"] = feedback
  else:
    data["params"]["answer-feedback"] = feedback
    data["params"]["submission-feedback"] = ""

