"""accm test where both register specifiers are the same"""

def mem_addr(i):
    return 0x10010000 + i * 4

initial_registers = {
    11: 123,
    12: 100,
    13: mem_addr(2),
    14: mem_addr(3),
}

instructions = [
    "accm\t$13, 4($13)",
    "accm\t$14, -4($14)",
]

modified_registers = {
    13: mem_addr(2) + 20,
    14: mem_addr(3) + 10,
}

initial_memory = {
    2: 10,
    3: 20,
}

