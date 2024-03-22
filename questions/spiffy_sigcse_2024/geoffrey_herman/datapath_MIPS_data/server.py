import random
import string

OPCODES = [
{"op": "add",  "type": "r", "alu_op": "010", "opcode": 0, "func": 0x20, "rd_src": '0', "wr_enable": '1', "alu_src2": '00', "control_type": "00", "lui": "0", "slt": "0", "byte_we": "0", "word_we": "0", "mem_read": "0", "byte_load": "x"},
#{"op": "sub",  "type": "r", "alu_op": "011", "opcode": 0, "func": 0x22, "rd_src": '0', "wr_enable": '1', "alu_src2": '00', "control_type": "00", "lui": "0", "slt": "0", "byte_we": "0", "word_we": "0", "mem_read": "0", "byte_load": "x"},
#{"op": "and",  "type": "r", "alu_op": "100", "opcode": 0, "func": 0x24, "rd_src": '0', "wr_enable": '1', "alu_src2": '00', "control_type": "00", "lui": "0", "slt": "0", "byte_we": "0", "word_we": "0", "mem_read": "0", "byte_load": "x"},
#{"op": "or",   "type": "r", "alu_op": "101", "opcode": 0, "func": 0x25, "rd_src": '0', "wr_enable": '1', "alu_src2": '00', "control_type": "00", "lui": "0", "slt": "0", "byte_we": "0", "word_we": "0", "mem_read": "0", "byte_load": "x"},
#{"op": "nor",  "type": "r", "alu_op": "110", "opcode": 0, "func": 0x27, "rd_src": '0', "wr_enable": '1', "alu_src2": '00', "control_type": "00", "lui": "0", "slt": "0", "byte_we": "0", "word_we": "0", "mem_read": "0", "byte_load": "x"},
#{"op": "xor",  "type": "r", "alu_op": "111", "opcode": 0, "func": 0x26, "rd_src": '0', "wr_enable": '1', "alu_src2": '00', "control_type": "00", "lui": "0", "slt": "0", "byte_we": "0", "word_we": "0", "mem_read": "0", "byte_load": "x"},
#{"op": "addi", "type": "i", "alu_op": "010", "opcode": 0x8, "rd_src": '1', "wr_enable": '1', "alu_src2": '01', "control_type": "00", "lui": "0", "slt": "0", "byte_we": "0", "word_we": "0", "mem_read": "0", "byte_load": "x"},
#{"op": "andi", "type": "i", "alu_op": "100", "opcode": 0xc, "rd_src": '1', "wr_enable": '1', "alu_src2": '10', "control_type": "00", "lui": "0", "slt": "0", "byte_we": "0", "word_we": "0", "mem_read": "0", "byte_load": "x"},
{"op": "ori",  "type": "i", "alu_op": "101", "opcode": 0xd, "rd_src": '1', "wr_enable": '1', "alu_src2": '10', "control_type": "00", "lui": "0", "slt": "0", "byte_we": "0", "word_we": "0", "mem_read": "0", "byte_load": "x"},
#{"op": "xori", "type": "i", "alu_op": "111", "opcode": 0xe, "rd_src": '1', "wr_enable": '1', "alu_src2": '10', "control_type": "00", "lui": "0", "slt": "0", "byte_we": "0", "word_we": "0", "mem_read": "0", "byte_load": "x"},
{"op": 'j', 'type': 'j', "alu_op": "xxx", "opcode": 0x2, "rd_src": 'x', "wr_enable": '0', "alu_src2": 'xx', "control_type": "10", "lui": "x", "slt": "x", "byte_we": "0", "word_we": "0", "mem_read": "x", "byte_load": "x"},
#{"op": 'jr', 'type': 'r', "alu_op": "xxx", "opcode": 0, "func": 0x8, "rd_src": 'x', "wr_enable": '0', "alu_src2": 'xx', "control_type": "11", "lui": "x", "slt": "x", "byte_we": "0", "word_we": "0", "mem_read": "0", "byte_load": "x"},
{"op": 'beq', 'type': 'i', "alu_op": "011", "opcode": 0x4, "rd_src": 'x', "wr_enable": '0', "alu_src2": '00', "control_type": "01", "lui": "x", "slt": "x", "byte_we": "0", "word_we": "0", "mem_read": "x", "byte_load": "x"},
#{"op": 'bne', 'type': 'i', "alu_op": "011", "opcode": 0x5, "rd_src": 'x', "wr_enable": '0', "alu_src2": '00', "control_type": "01", "lui": "x", "slt": "x", "byte_we": "0", "word_we": "0", "mem_read": "0", "byte_load": "x"},
#{"op": 'lui', 'type': 'i', "alu_op": "xxx", "opcode": 0xf, "rd_src": '1', "wr_enable": '1', "alu_src2": 'xx', "control_type": "00", "lui": "1", "slt": "x", "byte_we": "0", "word_we": "0", "mem_read": "0", "byte_load": "x"},
{"op": 'slt', 'type': 'r', "alu_op": "011", "opcode": 0, "func": '0x2a', "rd_src": '0', "wr_enable": '1', "alu_src2": '00', "control_type": "00", "lui": "0", "slt": "1", "byte_we": "0", "word_we": "0", "mem_read": "0", "byte_load": "x"},
#{"op": 'slti', 'type': 'i', "alu_op": "011", "opcode": 0xa, "rd_src": '1', "wr_enable": '1', "alu_src2": '01', "control_type": "00", "lui": "0", "slt": "1", "byte_we": "0", "word_we": "0", "mem_read": "0", "byte_load": "x"},
{"op": 'lw', 'type': 'i', "alu_op": "010", "opcode": 0x23, "rd_src": '1', "wr_enable": '1', "alu_src2": '01', "control_type": "00", "lui": "0", "slt": "x", "byte_we": "0", "word_we": "0", "mem_read": "1", "byte_load": "0"},
{"op": 'lbu', 'type': 'i', "alu_op": "010", "opcode": 0x24, "rd_src": '1', "wr_enable": '1', "alu_src2": '01', "control_type": "00", "lui": "0", "slt": "x", "byte_we": "0", "word_we": "0", "mem_read": "1", "byte_load": "1"},
{"op": 'sw', 'type': 'i', "alu_op": "010", "opcode": 0x2b, "rd_src": 'x', "wr_enable": '0', "alu_src2": '01', "control_type": "00", "lui": "x", "slt": "x", "byte_we": "0", "word_we": "1", "mem_read": "x", "byte_load": "x"},
{"op": 'sb', 'type': 'i', "alu_op": "010", "opcode": 0x2b, "rd_src": 'x', "wr_enable": '0', "alu_src2": '01', "control_type": "00", "lui": "x", "slt": "x", "byte_we": "1", "word_we": "0", "mem_read": "x", "byte_load": "x"},
]

MEM_INSTRUCTIONS = ['lbu', 'lhu', 'lh', 'lb', 'll', 'lw', 'sb', 'sc', 'sh', 'sw']

def generate(data):
  idx = random.randint(0,len(OPCODES) - 1)

  rs = random.randint(0,31)
  rt = random.randint(0,31)
  rd = random.randint(1,31)
  imm = random.randint(-2**4,2**4)
  addr = random.randint(0, 2**25)

  if OPCODES[idx]["type"] == 'r':
    if OPCODES[idx]["op"] == 'jr':
      inst_str = OPCODES[idx]["op"] + ' $' + str(rs)
    else:
      inst_str = OPCODES[idx]["op"] + ' $' + str(rd) + ', $' + str(rs) + ', $' + str(rt)
  elif OPCODES[idx]["type"] == 'i':
    if OPCODES[idx]["op"] == 'lui':
      inst_str = OPCODES[idx]["op"] + ' $' + str(rt) + ', ' + str(imm)
    elif OPCODES[idx]["op"] in MEM_INSTRUCTIONS:
      inst_str = OPCODES[idx]["op"] + ' $' + str(rt) + ', ' + str(imm) + '($' + str(rs) + ')'
    else:
      inst_str = OPCODES[idx]["op"] + ' $' + str(rt) + ', $' + str(rs) + ', ' + str(imm)
  elif OPCODES[idx]["type"] == 'j':
    inst_str = OPCODES[idx]["op"] + ' ' + hex(addr)
    data["correct_answers"]["rdest"] = "{0:05b}".format(rt)

  data["params"]["inst"] = inst_str

  for key in OPCODES[idx]:
    data["correct_answers"][key] = OPCODES[idx][key]

  return data