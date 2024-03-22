"""positive lwinn"""

initial_memory = {
    1: 233,
}

instructions = [
    "lwinn\t$3, 4($20)",
]

modified_registers = {
    3: initial_memory[1],
}
