"""zero lwinn"""

initial_memory = {
    2: 0,
}

instructions = [
    "lwinn\t$4, 8($20)",
]

modified_registers = {
    4: initial_memory[2],
}
