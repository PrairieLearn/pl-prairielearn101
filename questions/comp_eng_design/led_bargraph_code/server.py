import random, copy, numpy, base64

def generate(data):

    ledMatrixDict = [
            {'color': 'green', 'datasheet': 'DC10GWA-green-kingbright.pdf', 'fv': 2.2, 'current': 25},
            {'color': 'red', 'datasheet': 'DC10EWA-red-kingbright.pdf', 'fv': 1.9, 'current': 30},
            {'color': 'yellow', 'datasheet': '1922datasheet-yellow-luckylight.pdf', 'fv': 2.1, 'current': 25},
            {'color': 'yellow-green', 'datasheet': '1923datasheet-yellowgreen-luckylight.pdf', 'fv': 2.2, 'current': 25},
            {'color': 'red', 'datasheet': '1921datasheet-red-luckylight.pdf', 'fv': 2.0, 'current': 25},
            {'color': 'blue', 'datasheet': 'XGCBDX10D-blue-sunled.pdf', 'fv': 3.0, 'current': 30}
            ]

    ledMatrix = random.choice(ledMatrixDict)

    data['params'] = ledMatrix
    
    data["params"]["names_for_user"] = [
        {"name": "GPIO", "description": "RPi GPIO library", "type": "object"},
        {"name": "PINS", "description": "Array of pin numbers", "type": "list"}
    ]
    data["params"]["names_from_user"] = [
        {"name": "write_bar", "description": "Function to light the LED bar graph", "type": "function"}
    ]

    #def grade(data):
    #print(data['score'])
    #fileAnswer = data['submitted_answers']['_files'][0]['contents']
    #fileDecoded = base64.b64decode(fileAnswer)
    #print(dir(fileDecoded))
    #lines = base64.b64decode(bytes(fileAnswer, encoding='utf8')).split('\n')
    #print(lines[-2])
    #print(fileLines[-1])
