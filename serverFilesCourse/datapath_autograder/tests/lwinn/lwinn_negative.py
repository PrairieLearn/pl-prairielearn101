"""negative lwinn"""

initial_memory = {
    0: -55,
}

instructions = [
    "lwinn\t$2, 0($20)",
]

# not modified, but it's the expected behavior
default_value = 0x10010000
modified_registers = {
    2: default_value,
}
