"""non skipped asin when sum is 0"""

instructions = [
    "asin\t$2, $0, $0",
]

modified_registers = {
    2: 0,
}

pc_sequence = [
    0x400000,
    0x400004,
]
