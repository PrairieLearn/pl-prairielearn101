def grade(data):
    ## Written question
    
    data["partial_scores"]["answer"] = { 'score': 0 }
    import base64
    
    base64_message = data["submitted_answers"]['_files'][0]["contents"]
    base64_bytes = base64_message.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    response =  message_bytes.decode('ascii')
    
    if len(response) > 650:
        data["partial_scores"]["answer"]['score'] = 1
        data['score'] = 1
        data['feedback']['manual'] = "Thank you for your response here, I appreciate the time you took to consider the question and provide your response"
    elif len(response) > 450:
        data["partial_scores"]["answer"]['score'] = 0.75
        data['score'] = 0.75
        data['feedback']['manual'] = "Thank you for this reflection, we were looking for a slightly more thorough answer. Thank you for your response though!"
    elif len(response) > 250:
        data["partial_scores"]["answer"]['score'] = 0.50
        data['score'] = 0.5
        data['feedback']['manual'] = "Thank you for this reflection, this is short of our expectations and we were hoping for a bit more consideration. Perhaps next time you could spend a bit more time and effort thinking about this."
    elif len(response) > 150:
        data["partial_scores"]["answer"]['score'] = 0.25
        data['score'] = 0.25
        data['feedback']['manual'] = "I encourage you to take this a bit more seriously and provide a more comprehensive response."
    else:
        data["partial_scores"]["answer"]['score'] = 0
        data['score'] = 0
        data['feedback']['manual'] = "This response was left blank, or was barely answered. Unfortunately we can't give you any credit for this."

    if "branch" not in response:
        branch_msg = "Hmm, it doesn't seem like you used the word 'branch' anywhere in your answer - are you sure you are able to explain what the merge and the switch commands do?"
    else:
        branch_msg = ""

    explanation = f"""\n\n\nThank you - I hope this was valuable to you to reflect on ! 

**{branch_msg}**

Here is a sample answer:

- git commit, takes a snapshot of the current repository and add a comment so it is "versioned" and can be referred back to at any time. You can only go back to see previous versions when they're committed to the repository.

- git switch, change the branch they currently have checked out. This command can also be used to switch to a particular commit, and also be used to create a new branch if it doesn't already exist with the -c flag.

- git push, pushes the commits that have been made to a local repository into a remote repository, for example like GitHub.

- git pull, pulls the commits from a remote repository to your local repository so any changes are integrated onto your local machine.

- git merge, allows you to take any commits you have been made from a branch, and integrate them into the main branch.

- git rebase, allows the user to take all the commits they've made on a branch and act as if they were done on another branch. It's another way to integrate changes from a branch onto another one.
"""

    data['feedback']['manual'] += explanation
