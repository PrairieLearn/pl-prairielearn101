"""accm test case with: 1) negative accumulator value and 2) with negative memory value"""

def mem_addr(i):
    return 0x10010000 + i * 4

initial_registers = {
    11: 123,
    12: -100,
    13: mem_addr(2),
    14: mem_addr(3),
}

instructions = [
    "accm\t$11, 4($13)",
    "accm\t$12, -4($14)",
]

modified_registers = {
    11: 103,
    12: -90,
}

initial_memory = {
    2: 10,
    3: -20,
}

