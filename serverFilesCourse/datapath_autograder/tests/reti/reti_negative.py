"""reti with negative return value"""

initial_registers = {
    31: 0x40002c, # $ra
}

instructions = [
    "reti\t-10",
]

modified_registers = {
    2: -10,
}

pc_sequence = [
    0x400000,
    initial_registers[31],
]
