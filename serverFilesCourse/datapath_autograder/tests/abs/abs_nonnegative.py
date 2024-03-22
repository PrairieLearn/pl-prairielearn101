"""abs with non-negative values"""

initial_registers = {
    5: 0,
    6: 5,
    7: 0x7fffffff,
}

instructions = [
    "abs\t$15, $5",
    "abs\t$16, $6",
    "abs\t$17, $7",
]

modified_registers = {
    15: abs(initial_registers[5]),
    16: abs(initial_registers[6]),
    17: abs(initial_registers[7]),
}
