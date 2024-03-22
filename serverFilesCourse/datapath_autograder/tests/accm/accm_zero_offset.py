"""accm test with zero offset value in accm instruction"""

def mem_addr(i):
    return 0x10010000 + i * 4

initial_registers = {
    11: 123,
    12: 100,
    13: mem_addr(2),
    14: mem_addr(3),
}

instructions = [
    "accm\t$11, 0($13)",
    "accm\t$12, 0($14)",
]

modified_registers = {
    11: 133,
    12: 120,
}

initial_memory = {
    2: 10,
    3: 20,
}
