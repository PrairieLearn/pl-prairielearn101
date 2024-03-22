"""loopr with multiple iterations"""

initial_registers = {
    2: 3,
    3: 0x400000,
}

instructions = [
    "loop\t$2, $3",
]

modified_registers = {
    2: -1,
}

pc_sequence = [
    0x400000,
    0x400000,
    0x400000,
    0x400000,
    0x400004,
]
