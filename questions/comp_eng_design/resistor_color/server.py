import random, copy

def generate(data):
    valueDict = {"brown": 1, "black": 0, "red": 2, "orange":3,
            "yellow": 4, "green": 5, "blue": 6, "purple": 7, "gray": 8}
    colorDict = {"brown": "603813", "black": "231f20",
            "red": "bf1e2e", "orange": "f7941e", "yellow": "fff200",
            "green": "39b54a", "blue": "0e379a", "purple": "662d91",
            "gray": "666666"}
    multDict = {"black": 1, "brown": 10, "red": 100, "orange": 1000, "yellow": 10000}
    resPairs = [ ["brown", "black"], ["red", "red"], ["yellow", "purple"], 
            ["orange", "orange"], ["blue", "gray"]]
    pair = random.choice(resPairs)
    mult = random.choice(list(multDict.items()))

    data['params']['color1'] = colorDict[pair[0]]
    data['params']['color2'] = colorDict[pair[1]]
    data['params']['color3'] = colorDict[mult[0]]

    data['correct_answers']['R'] = mult[1]*(valueDict[pair[0]]*10 + valueDict[pair[1]])



def file(data):

    with open('resistor.svg', 'r') as file :
        filedata = file.read()
    
    # Replace the target string
    filedata = filedata.replace('COLOR1', data['params']['color1'])
    filedata = filedata.replace('COLOR2', data['params']['color2'])
    filedata = filedata.replace('COLOR3', data['params']['color3'])
    filedata = filedata.replace('COLORTOL', random.choice(["c68401", "939598"]))

    return filedata
