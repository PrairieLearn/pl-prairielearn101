import random, copy
import matplotlib.pyplot as plt
import numpy as np
import io

def file(data):

    def pwm(period=20, duty_cycle=0.5, step_size=0.5, cycles=2):
        t = np.arange(0, period*cycles, step_size)
        n_ones = int(1/step_size*duty_cycle*period)
        n_zeros = int(len(t)/cycles) - n_ones
        s = np.ones(n_ones)
        s = np.pad(s, (0, n_zeros))
        sig = np.tile(s, cycles)
        return (t, sig)

    def my_lines(ax, pos, *args, **kwargs):
        if ax == 'x':
            for p in pos:
                plt.axvline(p, *args, **kwargs)
        else:
            for p in pos:
                plt.axhline(p, *args, **kwargs)


    duty_cycle = data['correct_answers']['duty_cycle']/100.0
    period = data['correct_answers']['period']

    tick_freq = int(period/10)

    t, s = pwm(period=period, duty_cycle=duty_cycle)

    fig = plt.figure(figsize=(8,2));
    plt.yticks([]);
    plt.ylim([-0.1,1.2])
    plt.xticks(np.arange(0, np.max(t)+tick_freq, tick_freq))
    my_lines('x', np.arange(0, np.max(t)+tick_freq, tick_freq), color='.5', linewidth=.25)
    plt.xlabel("Time (ms)");
    plt.xlim([0, np.max(t)])
    plt.step(t, s, linewidth = 2, c='red', where='post' );
    plt.tight_layout()
    
    buf = io.BytesIO()

    plt.savefig(buf,format='png')

    return buf


def generate(data):
    
    duty_cycle = random.choice(np.arange(0.1, 1, 0.1))
    period = random.choice(np.arange(10, 90, 10))

    data['correct_answers']['duty_cycle'] = float(round(100*duty_cycle, 9))
    data['correct_answers']['period'] = float(round(period, 9))
    data['correct_answers']['frequency'] = float(round(1/(period*0.001), 9))

