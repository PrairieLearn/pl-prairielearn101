def grade(data):
    
    if len(dic['questions']) == 5:
        # This will give participants a mark regardless of what answers they select!
        data['score'] = 1
    
    elif len(dic['questions']) < 5:
        data['format_errors'] = "Please select at least 5 choices!"
        
    elif len(dic['questions']) > 5:
        data['format_errors'] = "Oops! You selected too many choices, please select only 5 choices!"

    
