def grade(data):
    ## Written question
    
    data["partial_scores"]["answer"] = { 'score': 0 }
    import base64
    import os
    import openai

    base64_message = data["submitted_answers"]['_files'][0]["contents"]
    base64_bytes = base64_message.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    response =  message_bytes.decode('ascii')

    openai.api_key = "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"

    chatgpt_response = openai.Completion.create(
    model="code-davinci-002",
    prompt=f"A student has written the following prompt: {response}.\n\n I want you to first respond to it as if you're their friend. And then, tell them about your day assuming you're from a country outside North America.",
    temperature=0,
    max_tokens=60,
    top_p=1.0,
    frequency_penalty=0.5,
    presence_penalty=0.0,
    #stop=["You:"]
    )

    data['feedback']['manual'] += chatgpt_response
