initial_registers = {
    3: 0x40002c,
}

initial_memory = {
    0: 0xcafebabe,
    3: 0xbaadf00d,
}

instructions = [
    'jrme\t$3, 12($20)',
]

pc_sequence = [
    0x400000,
    0x400004,
]
