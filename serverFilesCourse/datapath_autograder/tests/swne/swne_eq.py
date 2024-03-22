"""swne with equal values"""

def mem_addr(i):
    return 0x10010000 + i * 4

initial_registers = {
    11: 123,
    12: -10,
    13: mem_addr(2),
    14: mem_addr(3),
}

instructions = [
    "swne\t$13, $11, 123",
    "swne\t$14, $12, -10",
]

# not modified, but it's the expected behavior
default_value = 0xdeadbeef
modified_memory = {
    2: default_value,
    3: default_value,
}
