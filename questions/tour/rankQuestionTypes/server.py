def grade(data):
    
    if len(data['submitted_answers']['questions']) == 5:
        # This will give participants a mark regardless of what answers they select!
        data['score'] = 1

    elif len(data['submitted_answers']['questions']) < 5:
        data['format_errors']['questions'] = "Please select at least 5 choices!"
        
    elif len(data['submitted_answers']['questions']) > 5:
        data['format_errors']['questions'] = {"Oops! You selected too many choices, please select only 5 choices!"}

    # if data["score"] == 1:

