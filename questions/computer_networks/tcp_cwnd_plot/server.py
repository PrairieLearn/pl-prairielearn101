import random, copy, io
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

def file(data):
    
    if data['filename']=='cwnd.png':


        plt.figure(figsize=(8, 4));
        plt.plot(data['params']['cwnd_seq_complete'], linestyle='-', marker='o', color='black');

        intervals = data['params']['intervals']
        for i, interval in enumerate(intervals):
          plt.axvspan(intervals[i]['start'], intervals[i]['end'], facecolor=intervals[i]['color'], label=intervals[i]['i']);

        plt.xlabel("Time (RTTs)");
        plt.ylabel("CWND (MSS)");
        
        # Save the figure and return it as a buffer
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        return buf

def generate(data):


    cwnd_range_min = 19
    cwnd_range_max = 24
    cwnd_n_sawtooth = 5
    cwnd_max = np.random.randint(cwnd_range_min, cwnd_range_max)
    cwnd_offsets = np.concatenate([[np.floor(cwnd_max/3)], np.random.randint(-3, +3, size=(cwnd_n_sawtooth-1,))])
    cwnd_is_ss = np.concatenate([[True], np.random.choice([True, False], replace=True, p=[0.2, 0.8], size=(cwnd_n_sawtooth-1,))])
    # don't go to CA if cwnd is small - it looks weird
    # also, after the initial ss you virtually always go to ss
    correction = np.minimum(cwnd_n_sawtooth-1, np.where(cwnd_max + cwnd_offsets <=  20)[0]+1 )
    cwnd_is_ss[correction] = True
    cwnd_is_ss[1] = True
    
    cwnd_init = 0
    slow_start = True
    ssthresh = None
    cwnd_seq_complete = []
    
    intervals = []
    transitions = []
    
    t_init = 0
    
    for i in range(cwnd_n_sawtooth):
    
      if not cwnd_is_ss[i]: # congestion avoidance
        cwnd_seq = np.arange(ssthresh+3, cwnd_max + cwnd_offsets[i] + 1  ) 
        if len(cwnd_seq) > 1:
          t_end = t_init + len(cwnd_seq)
          intervals.append({'i': i+1, 'start': t_init, 'end': t_end-1, 'name': str(t_init) + '-' + str(t_end-1), 'ss': False, 'ca': True})
          t_init = t_end 
        else:
          cwnd_is_ss[i] = True
    
      if cwnd_is_ss[i]: # slow start
        if ssthresh: # if a ssthresh has been defined
          cwnd_seq_ss = np.minimum(ssthresh, np.power(2, np.arange(cwnd_init, 1+np.ceil(np.log2(ssthresh)))) )
          t_end = t_init + len(cwnd_seq_ss)
          intervals.append({'i': i+1, 'start': t_init, 'end': t_end-1, 'name': str(t_init) + '-' + str(t_end-1), 'ss': True, 'ca': False})
          t_init = t_end 
    
          cwnd_seq_ca = np.arange(cwnd_seq_ss[-1]+1, cwnd_max + cwnd_offsets[i] + 1)
          if len(cwnd_seq_ca) > 1:
            t_end = t_init + len(cwnd_seq_ca)
            intervals.append({'i': i+1, 'start': t_init, 'end': t_end-1, 'name': str(t_init) + '-' + str(t_end-1), 'ss': False, 'ca': True})
            t_init = t_end 
            cwnd_seq = np.concatenate( [cwnd_seq_ss, cwnd_seq_ca ])
          else:
            cwnd_seq = cwnd_seq_ss
        
        else: # in first iteration, ssthresh is a very large number - won't hit it
          cwnd_seq = np.power(2, np.arange(cwnd_init, 1+np.ceil(np.log2(cwnd_max + cwnd_offsets[i]))))
          t_end = t_init + len(cwnd_seq)
          intervals.append({'i': i+1, 'start': t_init, 'end': t_end-1, 'name': str(t_init) + '-' + str(t_end-1), 'ss': True, 'ca': False})
          t_init = t_end 
    
        ssthresh = np.floor(cwnd_seq[-1]/2 )
        
      cwnd_seq_complete.extend(cwnd_seq)
      if i < cwnd_n_sawtooth - 1:
          transitions.append({'i': str(len(cwnd_seq_complete)-1) + '-' + str(len(cwnd_seq_complete)), 'timeout': bool( cwnd_is_ss[i+1]) , 'dupack': bool( not cwnd_is_ss[i+1]) }   )
  
    cmap = matplotlib.cm.get_cmap('Pastel1')
  
    for i, interval in enumerate(intervals):
        intervals[i]['color'] = matplotlib.colors.to_hex(cmap(i), keep_alpha=True)
        
    data['params']['cwnd_seq_complete'] = cwnd_seq_complete
    data['params']['intervals'] = intervals
    data['params']['transitions'] = transitions
    