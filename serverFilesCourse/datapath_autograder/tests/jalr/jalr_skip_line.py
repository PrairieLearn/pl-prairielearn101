"""jalr skip line"""

initial_registers = {
    2: 0x400008,
}

instructions = [
    "jalr\t$2",         # 0x400000
    "add\t$3, $2, $2",  # 0x400004
]

pc_sequence = [
    0x400000,
    0x400008,
]

modified_registers = {
    31: 0x400004,
}
