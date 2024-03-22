"""not taken jrlt when registers are equal"""

initial_registers = {
    2: 0x400008,
    3: 0x400008,
}

instructions = [
    "jrlt\t$2, $3",
]

pc_sequence = [
    0x400000,
    0x400004,
]
