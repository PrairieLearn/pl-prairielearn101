import random, copy
import matplotlib.pyplot as plt
import numpy as np
import io, string

def file(data):
    
    def msb_first(c):
      bits = [int(b) for b in format(ord(c), '08b')]
      return bits
    
    def lsb_first(c):
      return msb_first(c)[::-1]
    
    def clock_signal(cycles, idle=1):
    
      if idle:
        clocks = np.arange(cycles) % 2
      else:
        clocks = 1 - np.arange(cycles) % 2
    
      clocks = np.append(clocks, [idle, idle, idle])
      clocks = np.insert(clocks, 0, [idle, idle, idle])
      return clocks
    
    def cs_signal(cycles):
      cs =  np.repeat(0, cycles)
      cs = np.append(cs, [0,1,1])
      cs = np.insert(cs, 0, [1,1,0])
      return cs
    
    def data_signal(c, mode='LSB'):
      if mode=="LSB":
        bits = lsb_first(c)
      else:
        bits = msb_first(c)
      
      data = np.repeat(bits, 2)
    
      data = np.append(data, [0,0,0])
      data = np.insert(data, 0, [0,0,0])
      return data

    
    def my_lines(ax, pos, *args, **kwargs):
        if ax == 'x':
            for p in pos:
                plt.axvline(p, *args, **kwargs)
        else:
            for p in pos:
                plt.axhline(p, *args, **kwargs)


    cycles = 16
    dataOut = data_signal(data['params']['charOut'], mode='MSB')
    dataIn = data_signal(data['params']['charIn'], mode='MSB')
    sck = clock_signal(cycles, idle=data['params']['cpol'])
    t = 0.5 * np.arange(len(sck))
    cs = cs_signal(cycles)

    plt.figure(figsize=(9,4));

    my_lines('x', np.arange(0, 12, 0.5), color='.5', linewidth=.2)
    my_lines('x', np.arange(0.5, 11.5, 1), color='.5', linewidth=.5)
    my_lines('y', [0, 2, 4, 6], color='.5', linewidth=2)
    plt.step(t, sck + 6, 'r', linewidth = 2, where='post', label='SCK')
    plt.step(t, dataOut + 4, 'b', linewidth = 2, where='post', label='SDO')
    plt.step(t, dataIn + 2, 'm', linewidth = 2, where='post', label='SDI')
    plt.step(t, cs, 'g', linewidth = 2, where='post', label='CS')
    plt.legend()
    plt.ylim([-1,8])
    plt.xticks([]);
    plt.yticks([]);



    plt.tight_layout()

    buf = io.BytesIO()

    plt.savefig(buf,format='png')

    return buf

def generate(data):

    charOut = random.choice(string.ascii_letters)
    charIn = random.choice(string.ascii_letters)

    data['params']['charOut'] = charOut
    data['params']['charIn'] = charIn
    
    data['params']['cpol'] = random.choice([0,1])

    # Put the answer into data['correct_answers']
    data['correct_answers']['charOut'] = charOut
    data['correct_answers']['charIn'] = charIn