"""cpmp which perform copies with some register values re-used"""

def mem_addr(i):
    return 0x10010000 + i * 4

initial_registers = {
    11: 123,
    12: 100,
    13: mem_addr(2),
    14: mem_addr(3),
}

instructions = [
    "cpmp\t$11, $13, $13",
    "cpmp\t$12, $14, $12",
]

modified_registers = {
    11: mem_addr(2),
    12: 100,
}

initial_memory = {
    2: 10,
    3: 20,
}
