

def grade(data):
  
  feedback = "\n"

  feedback = feedback + "**Exercise 1:**   \n\n"

  feedback = feedback + "* Part 1: "
  if data["partial_scores"]["ex1_1"]["score"] == 1:
    feedback = feedback + "**Correct!**    \n\n"
  else:
    feedback = feedback + "Incorrect. Look again at the type of data stored in the inner vectors.     \n\n"

  feedback = feedback + "* Part 2: "
  if data["partial_scores"]["ex1_2"]["score"] == 1:
    feedback = feedback + "**Correct!**    \n\n"
  else:
    feedback = feedback + "Incorrect. Try again.     \n\n"

  feedback = feedback + "* Part 3: "
  if data["partial_scores"]["ex1_3"]["score"] == 1:
    feedback = feedback + "**Correct!**    \n\n"
  else:
    feedback = feedback + "Incorrect. Try again.     \n\n"



  feedback = feedback + "\n\n**Exercise 2:**   \n\n"

  feedback = feedback + "* Part 1: "
  if data["partial_scores"]["ex2_1"]["score"] == 1:
    feedback = feedback + "**Correct!**    \n\n"
  else:
    feedback = feedback + "Incorrect. Look again at the type of data stored in the inner vectors.     \n\n"

  feedback = feedback + "* Part 2: "
  if data["partial_scores"]["ex2_2"]["score"] == 1:
    feedback = feedback + "**Correct!**    \n\n"
  else:
    feedback = feedback + "Incorrect. Try again.     \n\n"

  feedback = feedback + "* Part 3: "
  if data["partial_scores"]["ex2_3"]["score"] == 1:
    feedback = feedback + "**Correct!**    \n\n"
  else:
    feedback = feedback + "Incorrect. Try again.     \n\n"


  feedback = feedback + "\n   \n   "



  # if they haven't answered the question correctly, give them feedback in the submissions box, otherwise, show the feedback in the answer box
  if data["score"] != 1:
    data["params"]["submission-feedback"] = feedback
  else:
    data["params"]["answer-feedback"] = feedback
    data["params"]["submission-feedback"] = ""