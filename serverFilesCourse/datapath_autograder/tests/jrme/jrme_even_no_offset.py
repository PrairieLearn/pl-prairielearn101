initial_registers = {
    3: 0x40002c,
}

initial_memory = {
    0: 0xcafebabe,
}

instructions = [
    'jrme\t$3, 0($20)',
]

pc_sequence = [
    0x400000,
    0x40002c,
]
