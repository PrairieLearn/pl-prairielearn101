"""smask case with a full 0xffffffff mask"""

def mem_addr(i):
    return 0x10010000 + i * 4

initial_registers = {
    11: 0xcafebabe,
    12: 0xbeefdead,
    13: mem_addr(2),
    14: mem_addr(3),
}

instructions = [
    "smask\t$11, $13, -1",	# 0xffff
    "smask\t$12, $14, -1",      # 0xffff
]

initial_memory = {
    2: 10,
    3: -20,
}

# not modified, but it's the expected behavior
default_value = 0xdeadbeef
modified_memory = {
    2: 0xcafebabe,
    3: 0xbeefdead,
}
