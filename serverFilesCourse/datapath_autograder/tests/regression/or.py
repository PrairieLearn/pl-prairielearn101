initial_registers = {
    7: 0xfaceb001,
    8: 0xa0b0c0d0,
    9: 0x9630fc,
}

instructions = [
    "or\t$10, $7, $8",
    "or\t$11, $7, $9",
]

modified_registers = {
    10: initial_registers[7] | initial_registers[8],
    11: initial_registers[7] | initial_registers[9],
}
