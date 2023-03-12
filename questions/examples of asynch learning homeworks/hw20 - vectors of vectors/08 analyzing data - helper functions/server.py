
def grade(data):


  if data["score"] == 1:
    data["params"]["answer-feedback"] = "**Correct!**"
    data["params"]["submission-feedback"] = ""
  else: 
    data["params"]["submission-feedback"] = "This isn't quite correct. Review the pseudocode for the helper functions and make sure you have correctly implemented the functions. Run the test script on your computer and make sure you can re-create what it is supposed to print out."