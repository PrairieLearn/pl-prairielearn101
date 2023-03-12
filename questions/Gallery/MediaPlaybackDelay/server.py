import prairielearn as pl
import matplotlib.pyplot as plt
import random, io

def generate(data):

    delays = sorted([0] + [round(x + random.uniform(-0.5, 3), 1)
                           for x in range(1, 10) ])

    data['params']['delays'] = delays

    playout = 0
    for i in range(1, 10):
        playout = max(playout + 1, delays[i])
        data['correct_answers'][f'playout-{i}'] = playout

    data['correct_answers']['initial-delay-smooth'] = playout - 9

def file(data):

    if data['filename'] == 'graph.png':
        plt.figure(figsize=(8, 4))
        plt.xticks(range(0, 27),
                   ['$t_0$', '', ''] +
                   [x for n in range(3, 10, 3)
                    for x in (f'$t_0+{n}\Delta$', '', '')] +
                   ['$t_1$', '', ''] +
                   [x for n in range(3, 13, 3)
                    for x in (f'$t_1+{n}\Delta$', '', '')],
                   rotation=25)
        plt.yticks([x + 0.5 for x in range(10)],
                   [f'Block {n}' for n in range(10)])
        plt.grid(which='major', axis='x',
                 color='g', linestyle='-', linewidth=0.25)
        # plt.tight_layout()
        plt.plot([i   for i in range(10) for x in range(2)],
                 [i+x for i in range(10) for x in range(2)])
        plt.plot([12+d for d in data['params']['delays']
                  for x in range(2)],
                 [i+x for i in range(10) for x in range(2)])
        plt.text(0, 7, 'Server transmission')
        plt.text(12, 7, 'Client reception')
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        return buf
