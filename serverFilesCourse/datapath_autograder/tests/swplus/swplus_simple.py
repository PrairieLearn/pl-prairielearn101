"""swplus simple"""


instructions = [
    "swplus\t$2, 0($20)",
]

pc_sequence = [
    0x400000,
    0x400004,
]

modified_registers = {
    20: 0x10010004,
}

modified_memory = {
    0: 0x10010000,
}
