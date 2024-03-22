"""swne with non-equal values"""

def mem_addr(i):
    return 0x10010000 + i * 4

initial_registers = {
    11: 123,
    12: -10,
    13: mem_addr(0),
    14: mem_addr(1),
}

instructions = [
    "swne\t$13, $11, -10",
    "swne\t$14, $12, 123",
]

modified_memory = {
    0: initial_registers[11],
    1: initial_registers[12],
}
