initial_registers = {
    16: 256,
    29: 0x10010004, # $sp
}

instructions = [
    "push\t$16",
]

modified_registers = {
    29: 0x10010000,
}

modified_memory = {
    0: initial_registers[16],
}
