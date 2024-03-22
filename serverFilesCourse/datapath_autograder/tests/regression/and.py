initial_registers = {
    2: 0xabcdef,
    3: 0x0f0f0f0f,
    4: 0xf0f0f0f0,
}

instructions = [
    "and\t$5, $2, $3",
    "and\t$6, $2, $4",
]

modified_registers = {
    5: initial_registers[2] & initial_registers[3],
    6: initial_registers[2] & initial_registers[4],
}
