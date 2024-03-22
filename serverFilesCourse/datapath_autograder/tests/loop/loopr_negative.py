"""loopr with initial negative count"""

initial_registers = {
    2: -1,
    3: 0x400000,
}

instructions = [
    "loop\t$2, $3",
]

modified_registers = {
    2: -2,
}

pc_sequence = [
    0x400000,
    0x400004,
]
