"""taken beq"""

instructions = [
    "beq\t$0, $0, skip",
    "beq\t$0, $0, skip",
    ("skip", None),
]

pc_sequence = [
    0x400000,
    0x400008,
]
