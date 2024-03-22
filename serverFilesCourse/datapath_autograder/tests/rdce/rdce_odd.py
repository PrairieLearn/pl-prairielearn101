"""odd rdce"""

initial_registers = {
    4: -11,
}

instructions = [
    "rdce\t$14, $4, $15",
]

# some of these aren't modified, but it's the expected behavior
default_value = 0x10010000
modified_registers = {
    14: initial_registers[4],
    15: default_value,
}
