"""smask with immediate that gets sign extended, but low bits not set"""

def mem_addr(i):
    return 0x10010000 + i * 4

initial_registers = {
    11: 0xcafebabe,
    12: 0xdeadbeef,
    13: mem_addr(2),
    14: mem_addr(3),
}

instructions = [
    "smask\t$11, $13, -32768",		# 0x8000
    "smask\t$12, $14, -4096",		# 0xf000
]

initial_memory = {
    2: 10,
    3: -20,
}

# not modified, but it's the expected behavior
default_value = 0xdeadbeef
modified_memory = {
    2: 0xcafe8000,
    3: 0xdeadb000,
}
