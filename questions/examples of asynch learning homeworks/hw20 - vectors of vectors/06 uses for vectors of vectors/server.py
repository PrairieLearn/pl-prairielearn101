

def grade(data):
  
  feedback = "\n"


  if data["partial_scores"]["ex1"]["score"] == 1:
    feedback = feedback + "* Exercise 1: **Correct!** In this course, we will have the outer vector represent the rows and the inner vectors represent the columns. This is primarily so that we can mimic the row/column indexing that we did in MATLAB.   \n"
  else:
    feedback = feedback + "* Exercise 1: Oops! It's the other way around. Think back to how we did row/column indexing in MATLAB.    \n"


  if data["partial_scores"]["ex2"]["score"] == 1:
    feedback = feedback + "* Exercise 2: **Correct!** We first index into the \"row\" and then into the \"column\".     \n"
  else:
    feedback = feedback + "* Exercise 2: Try again. Remember to first index into the \"row\" and then into the \"column\". Don't forget that in C++, indexing starts at `0`, not `1`.  \n"



  feedback = feedback + "\n   \n   "

  # if they haven't answered the question correctly, give them feedback in the submissions box, otherwise, show the feedback in the answer box
  if data["score"] != 1:
    data["params"]["submission-feedback"] = feedback
  else:
    data["params"]["answer-feedback"] = feedback
    data["params"]["submission-feedback"] = ""