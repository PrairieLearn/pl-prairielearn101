"""negative lwsin"""

initial_memory = {
    1: -89,
}

instructions = [
    "lwsin\t$2, 4($20)",
]

modified_registers = {
    2: initial_memory[1],
}

pc_sequence = [
    0x400000,
    0x400008,
]
