from math import dist
import random
import string
import copy



def remove_element_code(a):
  # find the end of the <pl-code> tag
  closetag = a.find(">")
  
  # keep just the part of the code that is AFTER that tag
  a = a[closetag+1:]
  
  # remove the closing tag
  a = a.replace("</pl-code>", "")

  # convert the HTML "escape characters" to their correct code counterparts
  a = a.replace("&lt;", "<")
  a = a.replace("&gt;", ">")
  a = a.replace("&amp;","&")
  a = a.replace("&quot;","\"")

  # return just the code part of the answer
  return a


def create_student_answer_code_file(data):
    # open a file with the appropriate name, as specified by the question's server.py file    
    f = open(data["options"]["client_files_question_path"] + "/"+ data['params']['answer-filename'], "w") 


    # for each of the submitted answers, get the line of code, clean it using the remove_element_code helper function, and write it out to the file
    # print(data["submitted_answers"])

    # for x in thisdict:
  	#     for y in range(len(thisdict[x])):
	  # 	    print(thisdict[x][y]['inner_html'])

    for x in data["submitted_answers"]:
      for y in range(len(data["submitted_answers"][x])):

        # get how many indents there are for this answer
        numIndents = data["submitted_answers"][x][y]["indent"]

        # get the lines of code
        statement = data["submitted_answers"][x][y]['inner_html'] 

        # remove the <pl-code> parts and convert HTML back to regular characters
        statement = remove_element_code(statement) 

        # replace newlines with newline plus correct number of tabs
        newline = "\n"
        for i in range(numIndents):
          newline = newline + "\t"
        statement = statement.replace("\n", newline)

        # start the statement at the correct indentation level
        for i in range(numIndents):
          f.write("\t")

        # add the statement to the file
        f.write(statement)
        f.write("\n\n")

    # close the file
    f.close()



def create_student_answer_code_file_V2(data):

  # this is based on the rich text file PL element
  file_name = data['params']['answer-filename']


  # for each of the submitted answers, get the line of code, clean it using the remove_element_code helper function, and write it out to the file
  # print(data["submitted_answers"])

  # for x in thisdict:
  #     for y in range(len(thisdict[x])):
  # 	    print(thisdict[x][y]['inner_html'])

  file_contents = "";

  for x in data["submitted_answers"]:
    for y in range(len(data["submitted_answers"][x])):

      # skip this answer if it doesn't have a 'tag' field for pl-order-blocks
      if data["submitted_answers"][x][y].get('tag') == None:
        continue

      #print(data["submitted_answers"][x][y])

      # get how many indents there are for this answer
      numIndents = data["submitted_answers"][x][y]["indent"]

      # get the lines of code
      statement = data["submitted_answers"][x][y]['inner_html'] 

      # remove the <pl-code> parts and convert HTML back to regular characters
      statement = remove_element_code(statement) 

      # replace newlines with newline plus correct number of tabs
      newline = "\n"
      for i in range(numIndents):
        newline = newline + "\t"
      statement = statement.replace("\n", newline)

      # start the statement at the correct indentation level
      for i in range(numIndents):
        file_contents = file_contents + "\t"

      # add the statement to the file
      file_contents = file_contents + statement
      file_contents = file_contents + "\n\n"


  # We will store the files in the submitted_answer["_files"] key,
  # so delete the original submitted answer format to avoid
  # duplication
  if data["submitted_answers"].get("_files", None) is None:
      data["submitted_answers"]["_files"] = []
      data["submitted_answers"]["_files"].append(
          {"name": file_name, "contents": file_contents}
      )
  elif isinstance(data["submitted_answers"].get("_files", None), list):
      data["submitted_answers"]["_files"].append(
          {"name": file_name, "contents": file_contents}
      )

  # return file_contents



def includeHTML(filename):
  
    # open the file
    f = open(filename, "r")

    # read in the entire file and save it to a variable
    from_file = f.read()

    # return the variable (which might not be the most efficient thing ever, but hey it works for now
    return from_file