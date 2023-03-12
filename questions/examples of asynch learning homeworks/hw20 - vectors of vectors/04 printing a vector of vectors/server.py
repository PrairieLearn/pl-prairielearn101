def grade(data):
  


  # if they haven't answered the question correctly, give them feedback in the submissions box, otherwise, show the feedback in the answer box
  if data["score"] != 1:
    data["params"]["submission-feedback"] = "At least one of your answers is incorrect, out of order, or not indented correctly. Look again at your options and trace through what the code will do. "
  else:
    data["params"]["answer-feedback"] = ""
    data["params"]["submission-feedback"] = ""
