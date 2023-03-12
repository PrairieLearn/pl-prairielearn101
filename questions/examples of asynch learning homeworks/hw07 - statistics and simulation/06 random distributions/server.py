
def grade(data):
  
  feedback = "\n"


  if data["partial_scores"]["ex1"]["score"] == 1:
    feedback = feedback + "* Exercise 1: **Correct!** This vector has pseudo random values between 1 and 2, so `imax` must be at least 2. There is 1 row and 5 columns.   \n"
  else:
    feedback = feedback + "* Exercise 1: Try Again! Remember that the order of the arguments to randi is: `imax`, number of rows, number of columns.    \n"


  if data["partial_scores"]["ex2"]["score"] == 1:
    feedback = feedback + "* Exercise 2: **Correct!** Correct! This matrix has pseudo random values between 1 and 5, so `imax` must be at least 5. There are 3 rows and 6 columns.    \n"
  else:
    feedback = feedback + "* Exercise 2: Try Again! Remember that the order of the arguments to randi is: `imax`, number of rows, number of columns. Look carefully at all the values in the `x` matrix.   \n"



  feedback = feedback + "\n   \n   "

  # if they haven't answered the question correctly, give them feedback in the submissions box, otherwise, show the feedback in the answer box
  if data["score"] != 1:
    data["params"]["submission-feedback"] = feedback
  else:
    data["params"]["answer-feedback"] = feedback
    data["params"]["submission-feedback"] = ""

