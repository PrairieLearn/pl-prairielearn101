"""swplus given"""

initial_memory = {
    0: 1,
}

instructions = [
    "lw\t$3, 0($20)",
    "add\t$2, $0, $0",
    "swplus\t$2, 0($20)",
    "add\t$2, $2, $3",
    "swplus\t$2, 0($20)",
    "add\t$2, $2, $3",
    "swplus\t$2, 0($20)",
    "add\t$2, $2, $3",
    "swplus\t$2, 0($20)",
    "lw\t$4, 0($21)",
    "lw\t$5, 4($21)",
    "lw\t$6, 8($21)",
    "lw\t$7, 12($21)",
]

pc_sequence = [
    0x400000 + i*4
    for i in range(len(instructions)+1)
]

modified_registers = {
    3: 1,
    2: 3,
    4: 0,
    5: 1,
    6: 2,
    7: 3,
    20: 0x10010010,
}

modified_memory = {
    0: 0,
    1: 1,
    2: 2,
    3: 3,
}