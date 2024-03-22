initial_registers = {
    2: 13,
    3: 7,
    4: -15,
}

instructions = [
    "add\t$5, $2, $3",
    "add\t$6, $4, $2",
]

modified_registers = {
    5: initial_registers[2] + initial_registers[3],
    6: initial_registers[4] + initial_registers[2],
}
