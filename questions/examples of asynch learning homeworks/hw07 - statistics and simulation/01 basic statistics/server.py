def generate(data):
  

  # Answers to fill in the blank input
  data["correct_answers"]["ex1_1"] = 59.9500
  data["correct_answers"]["ex1_2"] = -33.9333
  data["correct_answers"]["ex1_3"] = 22.1584
  data["correct_answers"]["ex1_4"] = 26.9333
  data["correct_answers"]["ex1_5"] = 23.0333



def grade(data):
  
  # if they haven't answered the question correctly, give them feedback in the submissions box, otherwise, show the feedback in the answer box
  if data["score"] != 1:
    data["params"]["submission-feedback"] = "\nAt least one of your answers is incorrect. Double check that you typed your answers correctly. You can watch the walkthrough video, as well, to check your work.\n" 
  else:
    data["params"]["answer-feedback"] = "\n**Correct!** "
    data["params"]["submission-feedback"] = ""
