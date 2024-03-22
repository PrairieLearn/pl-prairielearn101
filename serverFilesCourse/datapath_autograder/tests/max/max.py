initial_registers = {
    2: 11,
    3: 45,
    4: -1,
    5: -16,
}

instructions = [
    "max\t$21, $2, $3",
    "max\t$22, $3, $2",
    "max\t$23, $4, $5",
    "max\t$24, $5, $4",
    "max\t$25, $4, $2",
    "max\t$26, $3, $4",
]

modified_registers = {
    21: max(initial_registers[2], initial_registers[3]),
    22: max(initial_registers[2], initial_registers[3]),
    23: max(initial_registers[4], initial_registers[5]),
    24: max(initial_registers[4], initial_registers[5]),
    25: max(initial_registers[2], initial_registers[4]),
    26: max(initial_registers[3], initial_registers[4]),
}
