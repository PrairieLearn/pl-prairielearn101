initial_memory = {
    0: 0x12345678,
    1: 0x87654321,
}

instructions = [
    "lw\t$2, 0($20)",
    "lw\t$3, 4($20)",
]

modified_registers = {
    2: initial_memory[0],
    3: initial_memory[1],
}
