initial_registers = {
    2: 21,
    3: 8,
    4: -10,
}

instructions = [
    "sub\t$5, $3, $2",
    "sub\t$6, $2, $4",
]

modified_registers = {
    5: initial_registers[3] - initial_registers[2],
    6: initial_registers[2] - initial_registers[4],
}
