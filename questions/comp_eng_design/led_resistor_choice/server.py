import random, numpy

def generate(data):

    ledDict = [ {'datasheet': 'WP7113SRD-D.pdf', 'current': 30, 'fv': 1.85},
            {'datasheet': '334-15T1C1-4WYA.pdf', 'current': 30, 'fv': 3.0},
            {'datasheet': 'TLUR640.pdf', 'current': 20, 'fv': 2.0},
            {'datasheet': '1254-10SYGD.pdf', 'current': 25, 'fv': 2.0},
            {'datasheet': 'IR333_A_datasheet.pdf', 'current': 100, 'fv': 1.2},
            {'datasheet': 'Red-10mm.pdf', 'current': 80, 'fv': 2.1}]
    l = random.choice(ledDict)
    V = 3.30
    R1 = random.choice([100, 220, 330, 470, 560, 680])
    R2 = random.choice([1000, 2200, 3300, 4700, 5600])
    R3 = random.choice([10, 22, 33, 47, 56])
    r = numpy.array([R1, R2, R3])
    numpy.random.shuffle(r)
    i = 1000.0*(V-l['fv'])/r
    max_current = numpy.min([15, l['current']])
    i_ok = i[numpy.where(i <= max_current)]
    r_ok = r[numpy.where(i <= max_current)]

    r_best = r_ok[numpy.argmax(i_ok)]

    # Put these into data['params']
    data['params']['V'] = V
    data['params']['datasheet'] = l['datasheet']
    data['params']['r1'] = int(r[0])
    data['params']['r2'] = int(r[1])
    data['params']['r3'] = int(r[2])
    data['correct_answers']['r'] = int(r_best)

