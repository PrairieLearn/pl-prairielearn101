

def grade(data):
  
  feedback = "\n"


  if data["partial_scores"]["ex1"]["score"] == 1:
    feedback = feedback + "* Exercise 1: **Correct!** The inner vector, `v`, adds an element each time through the loop, and that version of the inner vector is added as an element to the outer vector.   \n"
  else:
    feedback = feedback + "* Exercise 1: Try again. Look again at how `v`, the inner vector, changes each time through the loop... and what its value is when it is added as an element of the outer vector using `push_back`.    \n"

  if data["partial_scores"]["ex2_1"]["score"] == 1:
    feedback = feedback + "* Exercise 2 - Stage 1 to Stage 2: **Correct!** We want to assign the value of the last element in `v2` to the first element in `v2`. We also want to remove the last element in the vector in the second element in `v2`. (Note: There are many different ways to take `v2` from Stage 1 to Stage 2, but this is the only way that works with our available set of statements.)   \n"
  else:
    feedback = feedback + "* Exercise 2 - Stage 1 to Stage 2: Try again. We want to assign the value of the last element in `v2` to the first element in `v2`. We also want to remove the last element in the vector in the second element in `v2`. (Note: There are many different ways to take `v2` from Stage 1 to Stage 2, but this is the only way that works with our available set of statements.)    \n"

  if data["partial_scores"]["ex2_2"]["score"] == 1:
    feedback = feedback + "* Exercise 2 - Stage 2 to Stage 3: **Correct!** We want to assign the value of the second element in `v2` to the first element in `v2` and then add a `4` to the vector in the second element. We also want to add an element to `v2` and put a vector of `{0 0}` in that element. (Note: There are many different ways to take `v2` from Stage 2 to Stage 3, but this is the only way that works with our available set of statements.)   \n"
  else:
    feedback = feedback + "* Exercise 2 - Stage 2 to Stage 3: Try again. We want to assign the value of the second element in `v2` to the first element in `v2` and then add a `4` to the vector in the second element. We also want to add an element to `v2` and put a vector of `{0 0}` in that element. (Note: There are many different ways to take `v2` from Stage 2 to Stage 3, but this is the only way that works with our available set of statements.)    \n"



  feedback = feedback + "\n   \n   "

  # if they haven't answered the question correctly, give them feedback in the submissions box, otherwise, show the feedback in the answer box
  if data["score"] != 1:
    data["params"]["submission-feedback"] = feedback
  else:
    data["params"]["answer-feedback"] = feedback
    data["params"]["submission-feedback"] = ""