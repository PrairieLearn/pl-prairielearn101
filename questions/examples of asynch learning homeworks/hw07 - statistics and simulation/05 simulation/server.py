
def grade(data):
  
  feedback = "\n"


  if data["partial_scores"]["ex1"]["score"] == 1:
    feedback = feedback + "* Exercise 1: **Correct!** This vector starts at 0, ends at 20, and has 6 elements.   \n"
  else:
    feedback = feedback + "* Exercise 1: Try Again! Remember that the order of the arguments to `linspace` is: start, end, number of elements    \n"


  if data["partial_scores"]["ex2"]["score"] == 1:
    feedback = feedback + "* Exercise 2: **Correct!** This vector starts at 5, ends at -4, and has 10 elements. MATLAB recognized that the start value was more positive than the end value, so it \"counted down\" instead of \"up\".    \n"
  else:
    feedback = feedback + "* Exercise 2: Try Again! Remember that the order of the arguments to `linspace` is: start, end, number of elements   \n"



  feedback = feedback + "\n   \n   "

  # if they haven't answered the question correctly, give them feedback in the submissions box, otherwise, show the feedback in the answer box
  if data["score"] != 1:
    data["params"]["submission-feedback"] = feedback
  else:
    data["params"]["answer-feedback"] = feedback
    data["params"]["submission-feedback"] = ""

