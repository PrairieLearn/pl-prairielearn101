"""jrlm with non-zero offset"""

initial_registers = {
    3: 0x400200,
    15: 0x400008,
}

instructions = [
    "jrlm\t$15, 8($20)",
]

pc_sequence = [
    0x400000,
    0x400008,
]

modified_memory = {
    2: 0x400004,
}

