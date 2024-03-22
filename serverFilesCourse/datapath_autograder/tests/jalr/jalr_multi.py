"""jalr multi-call"""

initial_registers = {
    2: 0x40000C,
    5: 0x400080,
}

instructions = [
    "jalr\t$2",         # 0x400000
    "add\t$3, $2, $2",  # 0x400004
    "jalr\t$5",         # 0x400008
    "jalr\t$31",        # 0x40000C
]

pc_sequence = [
    0x400000,
    0x40000C,
    0x400004,
    0x400008,
    0x400080,
]

modified_registers = {
    3: initial_registers[2] + initial_registers[2],
    31: 0x40000C,
}

