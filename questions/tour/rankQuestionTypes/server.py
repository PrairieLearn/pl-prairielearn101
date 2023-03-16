def grade(data):
    
    if len(data['submitted_answers']['questions']) == 5:
        # This will give participants a mark regardless of what answers they select!
        data['score'] = 1

        data["feedback"] = "Great, thank you so much for engaging with this activity!"

    
    elif len(data['submitted_answers']['questions']) < 5:
        data['format_errors']['question'] = "Please select at least 5 choices!"

        data["feedback"] = "Please select at least 5 choices!"
        
    elif len(data['submitted_answers']['questions']) > 5:
        data['format_errors']['question'] = "Oops! You selected too many choices, please select only 5 choices!"

        data["feedback"] = "Oops! You selected too many choices, please select only 5 choices!"

    
