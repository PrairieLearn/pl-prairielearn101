from booleanParser import eval_ast, create_ast
from random import randint
import digital_logic.lib.schemdraw.logic as logic

def shortest_search(node, target=None):
    '''
    Search for the shortest delay path from the input(s) to the output
    @params target (optional): specify if the path should be from a specific input
    @return length of the shortest delay path
    '''

    value = list(node.keys())[0]
    children = node[value]
    terminal = value[0]
    value = int(value[1])

    if len(children) == 0:
        if (target and terminal == target) or not target:
            return value
        # if this terminal isn't the desired target (i.e. we're looking for shortest paths to y but this terminal is z)
        # then output a really large number, so this path should never be shortest
        else: 
            return 100000

    return value + min([shortest_search(child, target) for child in children])

def longest_search(node, target=None):
    '''
    Search for the longest delay path from the input(s) to the output
    @params target (optional): specify if the path should be from a specific input
    @return length of the longest delay path
    '''

    value = list(node.keys())[0]
    children = node[value]
    terminal = value[0]
    value = int(value[1])

    if len(children) == 0:
        if (target and terminal == target) or not target:
            return value
        # if this terminal isn't the desired target (i.e. we're looking for longest paths to y but this terminal is z)
        # then output a really small number, so this path should never be longest
        else:
            return -100000

    return value + max([longest_search(child, target) for child in children])


def create_delays(ast):
    '''
    represent the tree of delays as a nested dict (for serializability purposes)
    where there is only one key and list of values
    key is a composed string with first character being the identifier
    (i.e. 'x', 'y', 'z' for the wires or 'g' for a gate) and the delay value
    values is a list of children

    modified from serverFilesCourse/booleanParser.py
    '''

    if isinstance(ast, str):
        return {ast + str(0):[]}

    # singular epression --> recursively build circuit
    elif len(ast) == 1 and isinstance(ast, list):
        return create_delays(ast[0])

    # not operation (potential chaining):
    elif "'" in ast:
        delays = create_delays(ast[0])

        for element in ast[:0:-1]:
            if element == "'":
                delays = {'g' + str(randint(2,7)): [delays]}

            else:
                raise NotImplementedError("Degenerative case that should have been rejected by the parser. Please report this error.")

        return delays

    # case parentheses
    elif ast[0] == '(' and ast[2] == ')':
        return create_delays(ast[1])

    # case or
    elif ast[1] == '+':
        assert(len(ast) >= 3)
        assert(len(ast) % 2 == 1)

        # break into pre-+ and post-+ sections
        pre_wire = create_delays(ast[0])
        post_wire = create_delays(ast[2:])

        return {'g' + str(randint(2,7)): [pre_wire, post_wire]}

    # case mult
    elif ast[1] == '*':
        assert(len(ast) >= 3)
        assert(len(ast) % 2 == 1)

        # break into pre-* and post-* sections
        pre_wire = create_delays(ast[0])
        post_wire = create_delays(ast[2:])
        
        return {'g' + str(randint(2,7)): [pre_wire, post_wire]}

    # no operands found, so treat as multiply case
    else:
        # break into first and second sections
        pre_wire = create_delays(ast[0])
        post_wire = create_delays(ast[1:])

        return {'g' + str(randint(2,7)): [pre_wire, post_wire]}

def gen_delay_values(expression):
    '''
    generate a tree of delay values based on the AST of the expression
    the tree will be parsed in parallel with the AST in gen_delay_circuit 
    to draw the delay labels onto the diagram
    '''
    ast = create_ast(expression)
    root = create_delays(ast)

    return root

def gen_delay_circuit(ast, diagram, level, anchor_position, base_wires, delays):
    '''
    generate the circuit diagram recursively
    parses the tree of delay values in parallel
    modified from serverFilesCourse/booleanParser.py
    '''
    # parsing the delay tree
    value = list(delays.keys())[0]
    children = delays[value]
    value = value[1]

    if isinstance(ast, str):
        line = diagram.add(logic.Line('left', xy=anchor_position, l=diagram.unit * 0.25))
        
        if ast not in base_wires.keys():
            base_wires[ast] = []
        base_wires[ast].append(line)

        if level == 0:
            line.add_label('$out$', loc='rgt')

    # singular epression --> recursively build circuit
    elif len(ast) == 1 and isinstance(ast, list):
        gen_delay_circuit(ast[0], diagram, level, anchor_position, base_wires, delays)

    # not operation (potential chaining):
    elif "'" in ast:
        for element in ast[:0:-1]:
            if element == "'":
                gate = diagram.add(logic.Not('right', anchor='end', xy=anchor_position, label=value, 
                    lblloc='center', lblofst=(0,-0.05), fontsize=10))
                anchor_position = gate.start
                delays = children[0]

            else:
                raise NotImplementedError("Degenerative case that should have been rejected by the parser. Please report this error.")
    
        gen_delay_circuit(ast[0], diagram, level + 1, anchor_position, base_wires, delays)

        if level == 0:
            gate.add_label('$out$', loc='rgt')

    # case parentheses
    elif ast[0] == '(' and ast[2] == ')':
        return gen_delay_circuit(ast[1], diagram, level, anchor_position, base_wires, delays)

    # case or
    elif ast[1] == '+':
        assert(len(ast) >= 3)
        assert(len(ast) % 2 == 1)

        or_gate = diagram.add(logic.Or('right', anchor='out', xy=anchor_position, label=value, lblloc='center'))
        left = diagram.add(logic.Line('up', xy=or_gate.in1, l=diagram.unit * 0.1 * 2 ** (2 - level)))
        right = diagram.add(logic.Line('down', xy=or_gate.in2, l=diagram.unit * 0.1 * 2 ** (2 - level)))
        anchor_left = left.end
        anchor_right = right.end

        # break into pre-+ and post-+ sections
        pre_wire = gen_delay_circuit(ast[0], diagram, level + 1, anchor_left, base_wires, children[0])
        post_wire = gen_delay_circuit(ast[2:], diagram, level + 1, anchor_right, base_wires, children[1])

        if level == 0:
            or_gate.add_label('$out$', loc='rgt')

    # case mult
    elif ast[1] == '*':
        assert(len(ast) >= 3)
        assert(len(ast) % 2 == 1)

        and_gate = diagram.add(logic.And('right', anchor='out', xy=anchor_position, label=value, lblloc='center'))
        left = diagram.add(logic.Line('up', xy=and_gate.in1, l=diagram.unit * 0.1 * 2 ** (2 - level)))
        right = diagram.add(logic.Line('down', xy=and_gate.in2, l=diagram.unit * 0.1 * 2 ** (2 - level)))
        anchor_left = left.end
        anchor_right = right.end

        # break into pre-* and post-* sections
        pre_wire = gen_delay_circuit(ast[0], diagram, level + 1, anchor_left, base_wires, children[0])
        post_wire = gen_delay_circuit(ast[2:], diagram, level + 1, anchor_right, base_wires, children[1])

        if level == 0:
            and_gate.add_label('$out$', loc='rgt')

    # no operands found, so treat as multiply case
    else:
        and_gate = diagram.add(logic.And('right', anchor='out', xy=anchor_position, label=value, lblloc='center'))
        left = diagram.add(logic.Line('up', xy=and_gate.in1, l=diagram.unit * 0.1 * 2 ** (2 - level)))
        right = diagram.add(logic.Line('down', xy=and_gate.in2, l=diagram.unit * 0.1 * 2 ** (2 - level)))
        anchor_left = left.end
        anchor_right = right.end

        # break into first and second sections
        pre_wire = gen_delay_circuit(ast[0], diagram, level + 1, anchor_left, base_wires, children[0])
        post_wire = gen_delay_circuit(ast[1:], diagram, level + 1, anchor_right, base_wires, children[1])

        if level == 0:
            and_gate.add_label('$out$', loc='rgt')