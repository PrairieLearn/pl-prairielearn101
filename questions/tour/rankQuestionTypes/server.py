def grade(data):
    
    if len(data['submitted_answers']['questions']) == 5:
        # This will give participants a mark regardless of what answers they select!
        data['score'] = 1

        # To get rid of the red 0% badge (since we're marking everything right),
        # We need to over-write the partial_scores dict
        data['partial_scores'] = {}

    elif len(data['submitted_answers']['questions']) < 5:
        data['format_errors']['questions'] = {"invalid":"Please select at least 5 choices!"}
        
    elif len(data['submitted_answers']['questions']) > 5:
        data['format_errors']['questions'] = {"invalid":"Oops! You selected too many choices, please select only 5 choices!"}
