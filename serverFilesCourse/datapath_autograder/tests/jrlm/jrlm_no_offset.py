"""jrlm no offset"""

initial_registers = {
    2: 0x40000c,
    3: 0x400200,
}

instructions = [
    "jrlm\t$2, 0($20)",
]

pc_sequence = [
    0x400000,
    0x40000c,
]

modified_memory = {
    0: 0x400004,
}

