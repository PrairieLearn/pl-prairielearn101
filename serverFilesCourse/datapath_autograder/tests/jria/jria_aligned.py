"""jria with aligned address"""

initial_registers = {
    2: 0x400024,
}

instructions = [
    "jria\t$2",
]

pc_sequence = [
    0x400000,
    0x400024,
]
