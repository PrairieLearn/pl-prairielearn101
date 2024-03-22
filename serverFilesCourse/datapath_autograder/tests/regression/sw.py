initial_registers = {
    10: 42,
    11: 0xcafebabe,
}

instructions = [
    "sw\t$10, 0($20)",
    "sw\t$11, 12($20)",
]

modified_memory = {
    0: initial_registers[10],
    3: initial_registers[11],
}
