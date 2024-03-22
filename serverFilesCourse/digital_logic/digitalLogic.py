from digital_logic.constants import *
from digital_logic.terminals import Terminals
from digital_logic.circuit import gen_verilog, gen_circuit_diagram
import digital_logic.lib.schemdraw as schemdraw
from digital_logic.delay import *

from booleanParser import eval_ast, create_ast
from random import choice, randint
import io
from collections import OrderedDict

def get_truth_table(expression, num_vars):
    table = {}

    # generate all possible combination of number of variables
    for var_vals in range(2 ** num_vars):
        # set the boolean variables to evaluate with
        bin_form = "{0:b}".format(var_vals).zfill(num_vars)
        variable_assignments = {}

        for i in range(num_vars):
            variable_assignments[VAR_NAMES[i]] = (bin_form[i] == '1')

        table[bin_form] = 1 if eval_ast(create_ast(expression), variable_assignments) else 0

    return table

def gen_expression(num_vars, level):
    '''
    code converted to Python from clientFilesCourse/expression.js

    template option legend:
    1 -- remove the terminal
    2 -- remove the terminal and complement
    3 -- select terminal whose complement is still in the pool
    4 -- select terminal whose complement is still in the pool and remove term
    5 -- select any terminal
    6 -- remove the complement of the terminal
    7 -- select a negated terminal
    '''
    
    terminals = Terminals(num_vars)
    
    # populate one of the expression templates with terminals
    template_choices = equation_templates[0]
    template_set = template_choices[num_vars-2][level]
    template = choice(template_set)

    output = ""

    for item in template:
        if item == '1' or item == '2':
            term = terminals.get_random_terminal()
            terminals.remove_terminal(term)

            if item == '2':
                terminals.remove_terminal(terminals.complement_terminal(term))

            output += terminals.output_terminal(term)

        elif item == '3' or item == '4':
            term = terminals.get_random_has_complement_terminal()

            if item == '4':
                terminals.remove_terminal(term)

            output += terminals.output_terminal(term)

        elif item == '5':
            output += terminals.output_terminal(terminals.get_random_terminal())
        
        elif item == '6':
            term = terminals.remove_complement()
            output += terminals.output_terminal(term)

        elif item == '7':
            output += terminals.output_terminal(terminals.get_complement_terminal())
        
        else:
            output += item
    
    return output

def gen_verilog_code(expression, num_vars):
    '''
    takes an expression and converts it to verilog
    '''
    ast = create_ast(expression)

    # generate the main part of the verilog code
    verilog = []
    wires = []
    last_wire = gen_verilog(ast, verilog, wires)
    
    if last_wire in wires:
        wires.remove(last_wire)

        # replace all instances of the last_wire (should only be one)
        # with the wire named 'out'
        for i in range(len(verilog)):
            if last_wire in verilog[i]:
                verilog[i] = verilog[i].replace(last_wire, 'out')

    else:
        # if the expression only has one element (i.e. 'x', 'y', 'z')
        # need to add a buffer to the verilog code, otherwise it won't generate
        verilog.append(f'  buf b{randint(10,99)}(out, {expression});')

    # post-process the verilog code
    
    # build module definition
    variable_names = ', '.join(['x','y','z'][:num_vars])
    verilog_code = f'module circuit(out, {variable_names});\n'
    verilog_code += '  output out;\n'
    verilog_code += f'  input {variable_names};\n'
    
    if len(wires) > 0:
        verilog_code += f'  wire {", ".join(wires)};\n'
    
    verilog_code += '\n'

    verilog_code += '\n'.join(verilog[::-1])

    verilog_code += '\nendmodule // circuit'
    
    return verilog_code

def gen_circuit(expression, num_vars, delay=None):
    '''
    takes an expression and generate the corresponding circuit diagram

    added 5/9/2021: delays is a tree of delay values, which is None
    if delays aren't supposed to be shown (e.g. for digital logic questions), 
    but has value for the delay problems
    '''
    ast = create_ast(expression)

    diagram = schemdraw.Drawing()
    base_wires = {}
    
    if delay:
        gen_delay_circuit(ast, diagram, 0, (5,10), base_wires, delay)
    else:
        gen_circuit_diagram(ast, diagram, 0, (5,10), base_wires)

    # sort base_wires dict by number of elements in the value
    # reference: https://stackoverflow.com/questions/16868457/python-sorting-dictionary-by-length-of-values
    base_wires_sorted = OrderedDict()
    for var in sorted(base_wires, key=lambda var: len(base_wires[var])):
        base_wires_sorted[var] = base_wires[var]
        
    bounds = diagram.get_bbox()

    # dynamically generate where the wires will come together in the top left
    bases = {}
    xcoord = bounds.xmin - 3
    orig_x = xcoord - 0.5
    ycoord = bounds.ymax
    used_ycoords = []

    for var in base_wires_sorted.keys():
        # draw the dot and calculate a fixed base position
        # only if there is more than one wire for this variable
        if len(base_wires_sorted[var]) > 1:
            while ycoord in used_ycoords:
                ycoord -= 1

            diagram.add(schemdraw.logic.Dot(xy=(xcoord, ycoord)))

            line = diagram.add(schemdraw.logic.Line('left', xy=(xcoord, ycoord), tox=orig_x))
            line.add_label(f'${var}$', loc='lft')

            bases[var] = (xcoord, ycoord)

            used_ycoords.append(ycoord)
            ycoord -= 1

        else:
            only_wire = base_wires_sorted[var][0]
            line = diagram.add(schemdraw.logic.Line('left', xy=only_wire.end, tox=orig_x))
            line.add_label(f'${var}$', loc='lft')

            bases[var] = only_wire.end

            used_ycoords.append(only_wire.end[1])
        
        xcoord += diagram.unit * 0.25

    # connect all wires to this base point

    for var in base_wires_sorted.keys():
        if len(base_wires_sorted[var]) == 1:
            pass

        runup_distance = diagram.unit * 0.25

        for i in range(len(base_wires_sorted[var])):
            if i == 0:
                # vertical first, then horizontal
                direction = 'up' if base_wires_sorted[var][i].end[1] < bases[var][1] else 'down'
                vertical = diagram.add(schemdraw.logic.Line(direction, xy=base_wires_sorted[var][i].end, toy=bases[var][1]))
                
                direction = 'left' if vertical.end[0] > bases[var][0] else 'right'
                horizontal = diagram.add(schemdraw.logic.Line(direction, xy=vertical.end, tox=bases[var][0]))

            else: # this assumes that each variable will only be used up to twice
                # horizontal first, then vertical
                direction = 'left' if base_wires_sorted[var][i].end[0] > bases[var][0] else 'right'
                horizontal = diagram.add(schemdraw.logic.Line(direction, xy=base_wires_sorted[var][i].end, tox=bases[var][0]))
                
                direction = 'up' if horizontal.end[1] < bases[var][1] else 'down'
                vertical = diagram.add(schemdraw.logic.Line(direction, xy=horizontal.end, toy=bases[var][1]))

    buffer = io.BytesIO()
    figure = diagram.draw()

    # reference: https://stackoverflow.com/questions/21288062/second-y-axis-label-getting-cut-off/21288063
    figure.fig.savefig(buffer, format='png', bbox_inches='tight')

    return buffer