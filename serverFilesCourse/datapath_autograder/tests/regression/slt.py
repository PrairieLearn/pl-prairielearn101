initial_registers = {
    15: -1,
    16: 127,
    17: 0x7fffffff,
}

instructions = [
    "slt\t$3, $15, $16",
    "slt\t$4, $16, $15",
    "slt\t$5, $16, $16",
    "slt\t$6, $16, $17",
    "slt\t$7, $17, $16",
    "slt\t$8, $17, $15",
    "slt\t$9, $15, $17",
]

modified_registers = {
    3: int(initial_registers[15] < initial_registers[16]),
    4: int(initial_registers[16] < initial_registers[15]),
    5: int(initial_registers[16] < initial_registers[16]),
    6: int(initial_registers[16] < initial_registers[17]),
    7: int(initial_registers[17] < initial_registers[16]),
    8: int(initial_registers[17] < initial_registers[15]),
    9: int(initial_registers[15] < initial_registers[17]),
}
