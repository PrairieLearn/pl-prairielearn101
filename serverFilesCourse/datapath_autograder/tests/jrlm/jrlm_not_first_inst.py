"""jrlm not first instruction"""

initial_registers = {
    15: 0x400010,
}

instructions = [
    "add\t$6, $5, $0",
    "jrlm\t$15, 0($20)",
]

pc_sequence = [
    0x400000,
    0x400004,
    0x400010,
]

modified_memory = {
    0: 0x400008,
}

