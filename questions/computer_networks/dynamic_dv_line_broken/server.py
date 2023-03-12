import random, copy

def generate(data):
    cost = random.choice([2,3,4])
    data['params']['cost'] = cost
    data['params']['final'] = 10*cost
    data['params']['finalx'] = 11*cost
    data['correct_answers'] = {
        'i-A-B-B': 1,           # @ A to B via B
        'i-A-C-B': 1 + cost,    # @ A to C via B
        'i-B-A-A': 1,           # @ B to A via A
        'i-B-A-C': 1 + 2*cost,  # @ B to A via C
        'i-B-C-A': 2 + cost,    # @ B to C via A
        'i-B-C-C': cost,        # @ B to C via C
        'i-C-A-B': 1 + cost,    # @ C to A via B
        'i-C-B-B': cost,        # @ C to B via B
        '2-B-A-A': 1000000,     # @ B to A via A after link breaks
        '2-B-A-C': 1 + 2*cost,  # @ B to A via C after link breaks
        '2-B-C-A': 1000000,     # @ B to C via A after link breaks
        '2-B-C-C': cost,        # @ B to C via C after link breaks
        '3-C-A-B': 1 + 3*cost,  # @ C to A via B after update from B
        '3-C-B-B': cost,        # @ C to B via B after update from B
        '4-B-A-A': 1000000,
        '4-B-A-C': 1 + 4*cost,
        '4-B-C-A': 1000000,
        '4-B-C-C': cost
    }