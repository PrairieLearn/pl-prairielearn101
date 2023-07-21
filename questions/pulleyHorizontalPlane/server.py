import random


def generate(data):
    g = 10
    ma = random.randint(4, 8)
    while (True):
        mb = random.randint(4, 8)
        if ma != mb:
            break
        
    data["params"]["ma"] = ma
    data["params"]["mb"] = mb
    data["params"]["g"] = g
    
    net_force = (mb - ma) * g
    combined_mass = ma + mb
    acceleration = net_force / combined_mass
    data["correct_answers"]["a"] = acceleration
