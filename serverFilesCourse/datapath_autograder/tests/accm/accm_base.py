"""accm base case (rt != rs, imm != 0, all values positive)"""

def mem_addr(i):
    return 0x10010000 + i * 4

initial_registers = {
    11: 123,
    12: 100,
    13: mem_addr(2),
    14: mem_addr(3),
}

instructions = [
    "accm\t$11, 4($13)",
    "accm\t$12, -4($14)",
]

modified_registers = {
    11: 143,
    12: 110,
}

default_value = 0xdeadbeef

initial_memory = {
    2: 10,
    3: 20,
}

# not modified, but it's the expected behavior
default_value = 0xdeadbeef
modified_memory = {
    2: 10
}

