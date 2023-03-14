import random, copy
import matplotlib.pyplot as plt
import numpy as np
import io, string

def file(data):
    
    def my_lines(ax, pos, *args, **kwargs):
        if ax == 'x':
            for p in pos:
                plt.axvline(p, *args, **kwargs)
        else:
            for p in pos:
                plt.axhline(p, *args, **kwargs)
    
    def msb_first(c):
      bits = [int(b) for b in format(ord(c), '08b')]
      return bits
  
    c = data['params']['msg']
    
    fourBit = np.array(msb_first(c)).reshape((2,4))
    fourBit[:,0] # column 1 - bits send over d7
    
    tick_freq = 1
    clk = [0, 1, 1, 0, 0, 1, 1, 0, 0]
    
    fig = plt.figure(figsize=(6,8));
    
    for i in range(4):
      dbits = np.repeat(fourBit[:, i], 4)
      dbits = np.append(dbits, dbits[-1])
      plt.subplot(7, 1 ,i+1)
      plt.yticks([]);
      plt.ylim([-0.1,1.2])
      plt.xticks([]);
      my_lines('x', np.arange(0, len(clk), tick_freq), color='.5', linewidth=.25)
    
      plt.step(np.arange(0, 9), dbits, linewidth = 2, c='red', where='post', label='D%d' % (7-i));
      plt.legend(loc=6);
    
    plt.subplot(7, 1 ,5)
    my_lines('x', np.arange(0, len(clk), tick_freq), color='.5', linewidth=.25)
    plt.ylim([-0.1,1.2])
    rs = np.repeat([0], 9) # 0 for data, 1 for command
    plt.step(np.arange(0, 9), rs, linewidth = 2, c='blue', where='post', label='R/W');
    plt.legend(loc=6);
    plt.yticks([]);
    plt.xticks([]);
    
    plt.subplot(7, 1 ,6)
    my_lines('x', np.arange(0, len(clk), tick_freq), color='.5', linewidth=.25)
    plt.ylim([-0.1,1.2])
    rs = np.repeat([1], 9) # 0 for data, 1 for command
    plt.step(np.arange(0, 9), rs, linewidth = 2, c='blue', where='post', label='RS');
    plt.legend(loc=6);
    plt.yticks([]);
    plt.xticks([]);
    
    
    plt.subplot(7, 1 ,7)
    my_lines('x', np.arange(0, len(clk), tick_freq), color='.5', linewidth=.25)
    plt.step(np.arange(0, 9), clk, linewidth = 2, c='green', where='post', label='E');
    
    plt.ylim([-0.1,1.2])
    plt.legend(loc=6);
    plt.yticks([]);
    plt.xticks([]);

    plt.tight_layout()

    buf = io.BytesIO()

    plt.savefig(buf,format='png')

    return buf

def generate(data):
    
    msg = random.choice(string.ascii_letters)
    
    data['params']['msg'] = msg

    # Put the answer into data['correct_answers']
    data['correct_answers']['msg'] = msg