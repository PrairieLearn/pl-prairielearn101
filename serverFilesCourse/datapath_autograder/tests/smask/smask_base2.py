"""smask base case 2 (small register value, sparse mask)"""

def mem_addr(i):
    return 0x10010000 + i * 4

initial_registers = {
    11: 127,
    12: 0xdeadbeef,
    13: mem_addr(2),
    14: mem_addr(3),
}

instructions = [
    "smask\t$11, $13, 0x55",
]

initial_memory = {
    2: 10,
    3: -20,
}

# not modified, but it's the expected behavior
default_value = 0xdeadbeef
modified_memory = {
    2: 0x55,
}
