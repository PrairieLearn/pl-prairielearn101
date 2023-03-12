import re

def grade(data):
  

  score = 0

  feedback = "\n"

  # parse what they entered and compare to correct answers

  feedback = feedback + "**Exercise 1**   \n\n "

  feedback = feedback + "* Part 1: "
  correctAnswerPattern = re.compile(r'[^0-9]*42[^0-9]*42[^0-9]*')
  foundAnswer = correctAnswerPattern.search(data["submitted_answers"]["ex1_1"])
  if (foundAnswer):
    score = score + 1
    feedback = feedback + "**Correct!**   \n\n"
  else:
    feedback = feedback + "Incorrect, try again.   \n\n"

  feedback = feedback + "* Part 2: "
  correctAnswerPattern = re.compile(r'[^0-9]*5[^0-9]*2[^0-9]*23[^0-9]*8[^0-9]*')
  foundAnswer = correctAnswerPattern.search(data["submitted_answers"]["ex1_2"])
  if (foundAnswer):
    score = score + 1
    feedback = feedback + "**Correct!**   \n\n"
  else:
    feedback = feedback + "Incorrect, try again.   \n\n"
  

  feedback = feedback + "* Part 3: "
  correctAnswerPattern = re.compile(r'[^0-9]*2[^0-9]*')
  foundAnswer = correctAnswerPattern.search(data["submitted_answers"]["ex1_3"])
  if (foundAnswer):
    score = score + 1
    feedback = feedback + "**Correct!**   \n\n"
  else:
    feedback = feedback + "Incorrect, try again.   \n\n"



  feedback = feedback + "* Part 4: "
  correctAnswerPattern = re.compile(r'[^0-9]*13[^0-9]*')
  foundAnswer = correctAnswerPattern.search(data["submitted_answers"]["ex1_4"])
  if (foundAnswer):
    score = score + 1
    feedback = feedback + "**Correct!**   \n\n"
  else:
    feedback = feedback + "Incorrect, try again.   \n\n"

  # update total score
  if (score / 4 > 0.9): # there are 4 questions
    data["score"] = 1
  else:
    data["score"] = score / 4
  

  if data["score"] == 1:
    data["params"]["answer-feedback"] = feedback
    data["params"]["submission-feedback"] = ""
  else: 
    data["params"]["submission-feedback"] = feedback