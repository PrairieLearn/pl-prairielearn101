"""movz with non-zero rt"""

initial_registers = {
    2: -3,
    3: 33,
}

instructions = [
    "movz\t$14, $3, $2",
    "movz\t$16, $2, $3",
]

default_value = 0x10010000

# these aren't really modified, but it's the expected behavior
modified_registers = {
    14: default_value,
    16: default_value,
}
