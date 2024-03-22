"""jalm with zero offset"""

initial_memory = {
    0: 0x400020,
}

instructions = [
    "jalm\t$2, 0($20)",
]

modified_registers = {
    2: 0x400004,
}

pc_sequence = [
    0x400000,
    0x400020,
]
