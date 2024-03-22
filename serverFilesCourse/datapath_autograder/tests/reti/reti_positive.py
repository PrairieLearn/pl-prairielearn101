"""reti with positive return value"""

initial_registers = {
    31: 0x400020, # $ra
}

instructions = [
    "reti\t42",
]

modified_registers = {
    2: 42,
}

pc_sequence = [
    0x400000,
    initial_registers[31],
]
