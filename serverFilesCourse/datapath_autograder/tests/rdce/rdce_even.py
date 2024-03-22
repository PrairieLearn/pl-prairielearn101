"""even rdce"""

initial_registers = {
    2: 42,
}

instructions = [
    "rdce\t$12, $2, $13",
]

# some of these aren't modified, but it's the expected behavior
default_value = 0x10010000
modified_registers = {
    12: default_value,
    13: initial_registers[2],
}
