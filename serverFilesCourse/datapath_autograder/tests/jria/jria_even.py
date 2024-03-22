"""jria with even unaligned address"""

initial_registers = {
    2: 0x400022,
}

instructions = [
    "jria\t$2",
]

pc_sequence = [
    0x400000,
    0x400004,
]
