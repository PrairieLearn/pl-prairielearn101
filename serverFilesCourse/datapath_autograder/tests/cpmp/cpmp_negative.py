"""cpmp which does nothing because memory values are negative"""

def mem_addr(i):
    return 0x10010000 + i * 4

initial_registers = {
    11: 123,
    12: 100,
    13: mem_addr(2),
    14: mem_addr(3),
    15: 100000,
}

instructions = [
    "cpmp\t$11, $13, $12",
    "cpmp\t$15, $14, $12",
]

modified_registers = {
    11: 123,
    15: 100000,
}

initial_memory = {
    2: -1,
    3: -10234,
}
