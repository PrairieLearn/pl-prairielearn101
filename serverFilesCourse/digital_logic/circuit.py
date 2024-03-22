from random import randint
from itertools import islice
import digital_logic.lib.schemdraw.logic as logic

class NumberSet():
    '''
    helper class for the circuit class that generates random numbers
    using certain rules and keeps track of what has been used
    code converted to Python from circuitFilescourse/circuit.js
    '''

    def __init__(self, rangemin, rangemax):
        self.rangemin = rangemin
        self.rangemax = rangemax
        self.used = []

    def get(self):
        result = randint(self.rangemin, self.rangemax - 1)

        while result in self.used:
            result = randint(self.rangemin, self.rangemax - 1)

        self.used.append(result)
        return result

# globals for generating verilog
num_set = NumberSet(10,100)

def gen_verilog(ast, verilog_code, wire_names):
    '''
    generate the wires/gates part of the verilog code recursively
    modified from serverFilesCourse/booleanParser.py
    '''
    # if is single variable, then return variable name
    if isinstance(ast, str):
        return ast

    # singular expression -> recursively build verilog
    if len(ast) == 1 and isinstance(ast, list):
        return gen_verilog(ast[0], verilog_code, wire_names)

    # not operation (potential chaining)
    if "'" in ast:
        wire = gen_verilog(ast[0], verilog_code, wire_names)

        for i in islice(ast, 1, len(ast), 1):
            if i == "'":
                out_wire = f'w{num_set.get()}'
                verilog_code.append(f'  not n{num_set.get()}({out_wire},{wire});')
                wire = out_wire
                wire_names.append(out_wire)
            else:
                raise NotImplementedError("Degenerative case that should have been rejected by the parser. Please report this error.")

        return wire

    # case parentheses
    if ast[0] == '(' and ast[2] == ')':
        return gen_verilog(ast[1], verilog_code, wire_names)

    # case or
    if ast[1] == '+':
        assert(len(ast) >= 3)
        assert(len(ast) % 2 == 1)
        
        # break into pre-+ and post-+ sections
        pre = gen_verilog(ast[0], verilog_code, wire_names)
        post = gen_verilog(ast[2:], verilog_code, wire_names)
        out_wire = f'w{num_set.get()}'

        verilog_code.append(f'  or o{num_set.get()}({out_wire}, {pre}, {post});')
        wire_names.append(out_wire)
        return out_wire

    # case mult
    if ast[1] == '*':
        assert(len(ast) >= 3)
        assert(len(ast) % 2 == 1)

        # break into pre-+ and post-+ sections
        pre = gen_verilog(ast[0], verilog_code, wire_names)
        post = gen_verilog(ast[2:], verilog_code, wire_names)
        out_wire = f'w{num_set.get()}'

        verilog_code.append(f'  and a{num_set.get()}({out_wire}, {pre}, {post});')
        wire_names.append(out_wire)
        return out_wire
    
    # no operands found, so treat as multiply case
    pre = gen_verilog(ast[0], verilog_code, wire_names)
    post = gen_verilog(ast[1:], verilog_code, wire_names)
    out_wire = f'w{num_set.get()}'

    verilog_code.append(f'  and a{num_set.get()}({out_wire}, {pre}, {post});')
    wire_names.append(out_wire)
    return out_wire

def gen_circuit_diagram(ast, diagram, level, anchor_position, base_wires):
    '''
    generate the circuit diagram recursively
    modified from serverFilesCourse/booleanParser.py
    '''

    if isinstance(ast, str):
        line = diagram.add(logic.Line('left', xy=anchor_position, l=diagram.unit * 0.25))
        
        if ast not in base_wires.keys():
            base_wires[ast] = []
        base_wires[ast].append(line)

        if level == 0:
            line.add_label('$out$', loc='rgt')

    # singular epression --> recursively build circuit
    elif len(ast) == 1 and isinstance(ast, list):
        gen_circuit_diagram(ast[0], diagram, level, anchor_position, base_wires)

    # not operation (potential chaining):
    elif "'" in ast:
        for element in ast[:0:-1]:
            if element == "'":
                gate = diagram.add(logic.Not('right', anchor='end', xy=anchor_position))
                anchor_position = gate.start

            else:
                raise NotImplementedError("Degenerative case that should have been rejected by the parser. Please report this error.")
    
        gen_circuit_diagram(ast[0], diagram, level + 1, anchor_position, base_wires)

        if level == 0:
            gate.add_label('$out$', loc='rgt')

    # case parentheses
    elif ast[0] == '(' and ast[2] == ')':
        return gen_circuit_diagram(ast[1], diagram, level, anchor_position, base_wires)

    # case or
    elif ast[1] == '+':
        assert(len(ast) >= 3)
        assert(len(ast) % 2 == 1)

        or_gate = diagram.add(logic.Or('right', anchor='out', xy=anchor_position))
        left = diagram.add(logic.Line('up', xy=or_gate.in1, l=diagram.unit * 0.1 * 2 ** (2 - level)))
        right = diagram.add(logic.Line('down', xy=or_gate.in2, l=diagram.unit * 0.1 * 2 ** (2 - level)))
        anchor_left = left.end
        anchor_right = right.end

        # break into pre-+ and post-+ sections
        pre_wire = gen_circuit_diagram(ast[0], diagram, level + 1, anchor_left, base_wires)
        post_wire = gen_circuit_diagram(ast[2:], diagram, level + 1, anchor_right, base_wires)

        if level == 0:
            or_gate.add_label('$out$', loc='rgt')

    # case mult
    elif ast[1] == '*':
        assert(len(ast) >= 3)
        assert(len(ast) % 2 == 1)

        and_gate = diagram.add(logic.And('right', anchor='out', xy=anchor_position))
        left = diagram.add(logic.Line('up', xy=and_gate.in1, l=diagram.unit * 0.1 * 2 ** (2 - level)))
        right = diagram.add(logic.Line('down', xy=and_gate.in2, l=diagram.unit * 0.1 * 2 ** (2 - level)))
        anchor_left = left.end
        anchor_right = right.end

        # break into pre-* and post-* sections
        pre_wire = gen_circuit_diagram(ast[0], diagram, level + 1, anchor_left, base_wires)
        post_wire = gen_circuit_diagram(ast[2:], diagram, level + 1, anchor_right, base_wires)

        if level == 0:
            and_gate.add_label('$out$', loc='rgt')

    # no operands found, so treat as multiply case
    else:
        and_gate = diagram.add(logic.And('right', anchor='out', xy=anchor_position))
        left = diagram.add(logic.Line('up', xy=and_gate.in1, l=diagram.unit * 0.1 * 2 ** (2 - level)))
        right = diagram.add(logic.Line('down', xy=and_gate.in2, l=diagram.unit * 0.1 * 2 ** (2 - level)))
        anchor_left = left.end
        anchor_right = right.end

        # break into first and second sections
        pre_wire = gen_circuit_diagram(ast[0], diagram, level + 1, anchor_left, base_wires)
        post_wire = gen_circuit_diagram(ast[1:], diagram, level + 1, anchor_right, base_wires)

        if level == 0:
            and_gate.add_label('$out$', loc='rgt')