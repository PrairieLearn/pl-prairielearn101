"""jalm with non-zero offset"""

initial_memory = {
    2: 0x400020,
}

instructions = [
    "jalm\t$4, 8($20)",
]

modified_registers = {
    4: 0x400004,
}

pc_sequence = [
    0x400000,
    0x400020,
]
