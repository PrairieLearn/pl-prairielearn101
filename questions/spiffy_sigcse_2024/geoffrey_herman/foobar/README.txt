Instructions on how to modify and create new inbrowser MIPS questions.

***********************
*****question.html*****
***********************
You will need to modify at least four things.
1) Modify the instructions to tell the student which function to implement
2) Modify the C code that you wish for the student to implement. You will find this code between the <PRE></PRE> tags.
3) In the pl-file-editor tag, make sure you change the name of the *.s file to the name of your function.
4) In the starter assembly code, make sure you change the .globl and the label to match the name of your function.

*******************
*****server.py*****
*******************
In server.py, you are setting the grading parameters for the autograder and creating the desired outputs that the autograder will use to compare the students' answers. 
1) data['params']['problem'] should be the name of the function
2) data['params']['numTests'] is the number of test cases you want to run
3) data['params']['evilTests'] determines whether you check whether calling conventions for s registers were followed
4) data['params']['regular_weight'] determines the relative weighting of non-evil and evil tests. This should be 100 if evilTests is False.
5) correct[] is a list of test cases that you will create. There should be one entry in the list per test case. The desired output of your test cases should be strings. If you are printing an array of integers, the format should be a pattern of int space int space (e.g., "4 5 2 5 "). Note the extra space after the last 5. If you are printing a string, the format can just be a string (e.g., "string"). We have created helper MIPS functions that can help create correspondingly formatted outputs for you.

*******************
*****info.json*****
*******************
Make sure you change the following
1) UUID
2) title

**************************
*****sum_array_soln.s*****
**************************
sum_array_soln.s is just an example solution for course staff. It is not strictly needed, but it is recommended that you change the file name to match your function and that you put a working solution here.

*************************
*****tests directory*****
*************************
1) Change the sum_array directory to match the name of your function
2) In details.json, change all references to sum_array to match the name of your function
3) In details.json, the field "tests" is required but is not required to change the test case fields to match your actual tests. It can help with documentation for you to change the tests to match what you actually have in your server.py.
4) You need one main_[].s per test case in your server.py. Most everything in main_[].s are helper functions . The comments above the helper functions should tell you what they do and how to use them. The helper functions are there primarily to help you print the outputs from the student's code as a string that can be compared with "correct" from server.py
5) For each main_[].s, modify the .data segment to give you the data you need when calling the student's function. 
6) For each main_[].s, modify the main: function. Only change the code after "# Code for calling test case goes here" and "# Print result to the terminal and compare with "correct" from server.py". Everything else is there to protect the autograder from the student doing bad things.
7) If evilTests is True, you will need one main_evil_[].s per test case. Same basic principles as main_[].s

