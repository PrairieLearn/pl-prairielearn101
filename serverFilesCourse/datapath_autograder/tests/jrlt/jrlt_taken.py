"""taken jrlt"""

initial_registers = {
    2: 0x40000c,
    3: 0x400200,
}

instructions = [
    "jrlt\t$2, $3",
]

pc_sequence = [
    0x400000,
    0x40000c,
]
