"""movz with zero rt"""

initial_registers = {
    2: -3,
    3: 33,
    4: 0,
}

instructions = [
    "movz\t$13, $3, $4",
    "movz\t$15, $4, $4",
    "movz\t$17, $2, $4",
]

modified_registers = {
    13: initial_registers[3],
    15: initial_registers[4],
    17: initial_registers[2],
}
