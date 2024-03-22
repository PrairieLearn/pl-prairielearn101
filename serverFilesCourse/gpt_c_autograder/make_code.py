import json
import traceback
import openai 
import random

# weighted random choice picking the first key more often
openai.api_key = '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'

data_path = '/grade/data/data.json'
results_path = '/grade/results/results.json'

prompt_base = '''
Pretend that you are an introductory computer science student learning C for
the very first time. You have an extremely limited programming knowledge.  You
only know loops, conditionals, nested loops, creating your own functions,
conditionals, arrays, strings, char, and some basic functions from math.h and
stdio.h and string.h.  Additionally, assume you have not learned pointers yet.
Create code that is simple to explain and not the simplest possible code.
Generate some C code according to the following prompt:

Make a C function named `foo` that  <prompt>

Format your code such that it is in mardown format. e.g.,
```
code here
```
Do not include any test cases or additional text. Additionally, you should make
a single function called `foo`. No main function or helper functions. Do not
include any comments. 
'''

try:
    data = json.load(open(data_path))

    prompt = prompt_base.replace("<prompt>", data['submitted_answers']['result'])
    chatgpt_response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-16k", 
            messages=[{"role": "system", "content": prompt}],
            temperature=0.0
            )['choices'][0]['message']['content']

    if "```" in chatgpt_response:
        chatgpt_response = chatgpt_response[chatgpt_response.find("```") + 4:chatgpt_response.rfind("```")]


    with open("/grade/student/foo.c", "w") as outfile:
        outfile.write(chatgpt_response)

except Exception as e:
    # Last-ditch effort to capture meaningful error information
    results = {}
    results['gradable'] = False
    results['message'] = 'Oops, something went wrong, please contact the course staff.'
    results['output'] = traceback.format_exc()

    json.dump(results, open(results_path, 'w'))
