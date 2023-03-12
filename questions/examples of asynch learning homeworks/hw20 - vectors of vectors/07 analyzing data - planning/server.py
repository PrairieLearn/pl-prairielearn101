def generate(data):
  
  # Answer to fill in the blank input
  data["correct_answers"]["ex1_2"] = "Type 1 Rover #test (100%) carrying 100kg."




def grade(data):
  
  feedback = "\n"


  if data["partial_scores"]["ex1"]["score"] == 1:
    feedback = feedback + "* Exercise 1: **Correct!**    \n"
  else:
    feedback = feedback + "* Exercise 1: Try again.    \n"





  feedback = feedback + "\n   \n   "

  # if they haven't answered the question correctly, give them feedback in the submissions box, otherwise, show the feedback in the answer box
  if data["score"] != 1:
    data["params"]["submission-feedback"] = feedback
  else:
    data["params"]["answer-feedback"] = feedback
    data["params"]["submission-feedback"] = ""