"""jalr given"""

initial_memory = {
    0: 1,
    1: 255,
    2: 1024,
    3: 0x400020,
    4: 0x400028,
}

instructions = [
    "lw\t$2, 0($20)",   # 0x400000
    "lw\t$3, 4($20)",   # 0x400004
    "lw\t$5, 12($20)",  # 0x400008
    "lw\t$6, 16($20)",  # 0x40000C

    "jalr\t$5",         # 0x400010
    "add\t$8, $7, $3",  # 0x400014

    "jalr\t$6",         # 0x400018
    "or\t$10, $9, $3",  # 0x40001C

    "add\t$7, $2, $2",  # 0x400020, f
    "jalr\t$ra",        # 0x400024

    "sub\t$9, $8, $2",  # 0x400028, g
]

pc_sequence = [
    0x400000,
    0x400004,
    0x400008,
    0x40000C,
    0x400010,
    0x400020,
    0x400024,
    0x400014,
    0x400018,
    0x400028,
    0x40002C,
]

modified_registers = {
    2: initial_memory[0],
    3: initial_memory[1],
    5: initial_memory[3],
    6: initial_memory[4],
    7: initial_memory[0] + initial_memory[0],
    8: initial_memory[0] + initial_memory[0] + initial_memory[1],
    9: initial_memory[0] + initial_memory[1],
    31: 0x40001C,
}

