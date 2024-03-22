"""smask base case 1 (large register value, sparse mask)"""

def mem_addr(i):
    return 0x10010000 + i * 4

initial_registers = {
    11: 127,
    12: 0xdeadbeef,
    13: mem_addr(2),
    14: mem_addr(3),
}

instructions = [
    "smask\t$12, $14, 0x0f0f",
]

initial_memory = {
    2: 10,
    3: -20,
}

# not modified, but it's the expected behavior
default_value = 0xdeadbeef
modified_memory = {
    3: 0xe0f,
}
