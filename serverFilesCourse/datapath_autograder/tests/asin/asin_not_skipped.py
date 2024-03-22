"""not skipped asin"""

initial_registers = {
    2: 5,
    3: -1,
}

instructions = [
    "asin\t$4, $2, $3",
]

modified_registers = {
    4: initial_registers[2] + initial_registers[3],
}

pc_sequence = [
    0x400000,
    0x400004,
]
