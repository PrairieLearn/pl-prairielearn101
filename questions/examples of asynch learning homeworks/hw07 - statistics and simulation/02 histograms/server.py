def grade(data):
  
  

  # if they haven't answered the question correctly, give them feedback in the submissions box, otherwise, show the feedback in the answer box
  if data["score"] != 1:
    data["params"]["submission-feedback"] = "Incorrect. Check your selections again to make sure you did everything correct. You can also watch the walkthrough video to check your work."
  else:
    data["params"]["answer-feedback"] = "**Correct!**"
    data["params"]["submission-feedback"] = ""

