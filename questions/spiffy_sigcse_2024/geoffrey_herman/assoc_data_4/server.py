import random 
import string
import math
from random import choice

DATA_MEM = []
CACHE = []

def generate(data): 
  addr_bits = 4
  addr_hex_size = math.ceil(addr_bits / 4)

  ### CREATE MEMORY TABLE
  mem_table = ''

  for x in range(16):
    addr = '{0:#0{1}x}'.format(x, addr_hex_size + 2)
    DATA_MEM.append(random.randint(0,255))

    mem_table += '<tr><td>' + addr + '</td><td>' + str(DATA_MEM[x]) + '</td></tr>'
    
  data['params']['mem_table'] = mem_table

  ### CREATE CACHE DIAGRAM
  ways = 4
  offset_bits = 1
  tag_bits = addr_bits - offset_bits
  max_tag = 2**tag_bits

  start_cache_table = ''      # starting state of the cache
  input_cache_table = ''      # final state of the cache for input
  tags = random.sample(list(range(0,max_tag)),4)
  way_list = [0,1,2,3]
  lru_list = random.sample(way_list,len(way_list))

  data['params']['lru_list'] = str(lru_list)
  data['params']['lru'] = lru_list[0]
  data['params']['mru'] = lru_list[3]
  
  for x in range(ways):

##################################
### Generate data for each way ###
##################################
    tag = tags[x]
    hex_tag = '{0:#0{1}x}'.format(tag, 3)

    addr = tag * 2**(offset_bits)   # load data from memory
    data0 = str(DATA_MEM[addr])   
    data1 = str(DATA_MEM[addr+1])

################################################
### Create all ways of the cache in the dict ###
################################################

    cache_dict = {"tag": tag, "data0": data0, "data1": data1}
    CACHE.append(cache_dict)

    if x == 2:
      start_cache_table += '''<thead><tr><th colspan="3">Way 2</th><th></th><th colspan="3">Way 3</th></tr><tr>
      <th>Tag</th><th>Off 0</th><th>Off 1</th><th></th><th>Tag</th><th>Off 0</th><th>Off 1</th></tr></thead>'''
      input_cache_table += '''<thead><tr><th colspan="3">Way 2</th><th></th><th colspan="3">Way 3</th></tr><tr>
      <th>Tag</th><th>Off 0</th><th>Off 1</th><th></th><th>Tag</th><th>Off 0</th><th>Off 1</th></tr></thead>'''


    if x == 0 or x == 2:
      start_cache_table += f'<tr><td>{hex_tag}</td>' \
                      f'<td>{data0}</td>' \
                      f'<td>{data1}</td>' \
                      f'<td></td>'

      input_cache_table += f'<tr><td><pl-string-embed answers-name="tag{x}" size="35" placeholder="{hex_tag}" weight=1></pl-string-embed></td>' \
                      f'<td><pl-string-embed answers-name="data{x}_0" size="35" placeholder="{data0}" weight=1></pl-string-embed></td>' \
                      f'<td><pl-string-embed answers-name="data{x}_1" size="35" placeholder="{data1}" weight=1></pl-string-embed></td>' \
                      f'<td></td>'

    else:
      start_cache_table += f'<td>{hex_tag}</td>' \
                      f'<td>{data0}</td>' \
                      f'<td>{data1}</td></tr>'

      input_cache_table += f'<td><pl-string-embed answers-name="tag{x}" size="35" placeholder="{hex_tag}" weight=1></pl-string-embed></td>' \
                      f'<td><pl-string-embed answers-name="data{x}_0" size="35" placeholder="{data0}" weight=1></pl-string-embed></td>' \
                      f'<td><pl-string-embed answers-name="data{x}_1" size="35" placeholder="{data1}" weight=1></pl-string-embed></td></tr>' \


  data['params']['start_cache_table'] = start_cache_table
  data['params']['input_cache_table'] = input_cache_table

###########################################
### Create addresses and simulate cache ###
###########################################
  address_table = ''
  num_addr = 4
  for x in range(num_addr):
    acc_tag = random.randint(0, max_tag-1)
    acc_off = random.randint(0, (2**offset_bits)-1)

    hex_tag = '{0:#0{1}x}'.format(acc_tag, 3)

    # address = acc_tag * 2**(offset_bits + index_bits) + acc_idx * 2**(offset_bits) + acc_off
    address = acc_tag * 2**offset_bits + acc_off
    hex_addr = '{0:#0{1}x}'.format(address, addr_hex_size + 2)
    addr = acc_tag * 2**(offset_bits)

    hit_flag = 0
    hit_way = 0
    for y in range(4):
      if (CACHE[y]['tag'] == acc_tag):
        hit_flag = 1
        hit_way = y

    if hit_flag == 1:
      address_table += f'<tr><td>Load {hex_addr}</td>' \
                      f'<td><pl-multiple-choice answers-name="ac{x}" fixed-order="true" inline="true">' \
                      f'<pl-answer correct="true">Hit</pl-answer>' \
                      f'<pl-answer correct="false">Miss</pl-answer>' \
                      f'</pl-multiple-choice></td></tr>'
      lru_list = update_lru(hit_way, lru_list)
    else:      
      address_table += f'<tr><td>Load {hex_addr}</td>' \
                      f'<td><pl-multiple-choice answers-name="ac{x}" fixed-order="true" inline="true">' \
                      f'<pl-answer correct="false">Hit</pl-answer>' \
                      f'<pl-answer correct="true">Miss</pl-answer>' \
                      f'</pl-multiple-choice></td></tr>'
      ### Update the LRU way if miss
      CACHE[lru_list[0]]['tag'] = acc_tag
      CACHE[lru_list[0]]['data0'] = str(DATA_MEM[addr])
      CACHE[lru_list[0]]['data1'] = str(DATA_MEM[addr+1])
      lru_list = update_lru(lru_list[0], lru_list)

  data['params']['address_table'] = address_table

##############################
### Create correct answers ###
##############################

  for x in range(ways):
    data['correct_answers'][f'tag{x}'] = '{0:#0{1}x}'.format(CACHE[x]['tag'], 3)
    data['correct_answers'][f'data{x}_0'] = CACHE[x]['data0']
    data['correct_answers'][f'data{x}_1'] = CACHE[x]['data1']
    data['correct_answers'][f'lru{x}'] = str(lru_list[x])

  return data

def update_lru(way, lru_list):
  for x in range(len(lru_list)-1):
    if way == lru_list[x]:
      for y in range(x,len(lru_list)-1):
        lru_list[y] = lru_list[y+1]
      lru_list[3] = way
      return lru_list
  return lru_list

def grade(data):
  ways = 4
  num_addr = 4
  
  hit_miss_score = 0
  cache_score = 0
  lru_score = 0
  score = 0

  for x in range(num_addr):
    hit_miss_score += data['partial_scores'][f'ac{x}']['score']

  for x in range(ways):
    cache_score += data['partial_scores'][f'tag{x}']['score']
    cache_score += data['partial_scores'][f'data{x}_0']['score']
    cache_score += data['partial_scores'][f'data{x}_1']['score']
    lru_score += data['partial_scores'][f'lru{x}']['score']

  if cache_score == ways * 3:
    score += 0.5
  if lru_score == ways:
    score += 0.25
  if hit_miss_score == num_addr:
    score += 0.25

  data['score'] = score
