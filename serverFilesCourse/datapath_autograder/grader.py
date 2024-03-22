from __future__ import print_function

import json

from command import Command
from run import run_suite, CompilationError
from string_logger import StringLogger


INFO_PATH = "/grade/data/data.json"

def remove_comments(lines):
    # Removing Multi Line Comments
    after_removing_multiline_comments = []
    in_comment = False
    for l in lines:
        line = l
        retained_line = ''
        if not in_comment:
            start_loc = l[:l.find('//')].find('/*')
            if start_loc != -1:
                retained_line = l[:start_loc]
                line = l[start_loc:]
                in_comment = True
            else:
                after_removing_multiline_comments.append(l)

        if in_comment:
            end_loc = line.find('*/')
            if end_loc != -1:
                rest_of_line = line[end_loc + 2:]
                in_comment = False
                if retained_line != '':
                    after_removing_multiline_comments.append(retained_line + ' ' + rest_of_line)
                else:
                    after_removing_multiline_comments.append(rest_of_line)

    # Removing Single Line Comments
    after_removing_single_line_comments = []
    for l in after_removing_multiline_comments:
        after_removing_single_line_comments.append(l[:l.find('//')])

    # Changing To One Statement Per Line
    one_statment_per_line = []
    broken_on_semi_colon = ' '.join(after_removing_single_line_comments).split(';')
    for l in broken_on_semi_colon:
        if l != '':
            one_statment_per_line.append(l.strip() + ';')

    # Removing Empty Spaces
    without_spaces = []
    for l in one_statment_per_line:
        if l.strip() != '':
            without_spaces.append((' '.join(l.split())).strip())

    return without_spaces

def find_args_in_module_def(moduleName, file):
    for l in file:
        if ('module' in l) and (moduleName in l):
            moduledef = l[l.find(moduleName):]
            break

    args = moduledef[(moduledef.find('(') + 1): moduledef.find(')')].split(',')
    return set(map(lambda x : x.strip(), args))

def mips_decode_changed(submission, original):
    moduleName = 'mips_decode'
    sub = find_args_in_module_def(moduleName, submission)
    orig = find_args_in_module_def(moduleName, original)
    diff = (sub - orig) | (orig - sub)
    if len(diff) != 0:
        return True
    else:
        return False

def wire_new_inst_changed(submission, original):
    def find_wire(lines):
        for l in lines:
            if 'new_inst' in l and '=' in l:
                return l
        return ''

    def get_expression(l):
        return l.split('=')[-1].strip()[:-1]

    return get_expression(find_wire(submission)) != get_expression(find_wire(original))

def modules_changed(submission, original):
    def module_instantiated(l):
        keywords = ['module', 'output', 'input', 'wire', 'endmodule', 'assign']
        return l.split()[0] not in keywords

    def get_module_info(l):
            argStart = l.rfind('(')
            argEnd = l.rfind(')')
            args = set(map(lambda x: x.strip(), l[argStart + 1:argEnd].split(',')))
            rest = l[:argStart].split()
            name = rest[-1]
            type = ''.join(rest[:-1]).replace(' ', '')
            return {'type' : type, 'name' : name, 'args' : args}

    submission_modules = list(map(get_module_info, filter(module_instantiated, submission)))
    original_modules = list(map(get_module_info, filter(module_instantiated, original)))

    # Check 1: There should be atleast 1 new module
    if len(submission_modules) > len(original_modules):
        return True

    # Check 2: Or current modules are modified:
    matching_count = 0
    for m in original_modules:
        for ms in submission_modules:
            if m['type'] == ms['type'] and m['name'] == ms['name']:
                matching_count += 1
                diff = (ms['args'] - m['args']) | (m['args'] - ms['args'])
                if len(diff) != 0:
                    return True

    if matching_count != len(original_modules):
        return True

    return False

def too_similar():
    grading_result = {}
    grading_result['gradable'] = False
    grading_result['message'] = "machine.v was not sufficiently edited to warrant grading."
    print(json.dumps(grading_result))

def print_Compilation_Error(error):
    tests = []

    tests.append({
        "name": "Compilation Check",
        "max_points": 1,
        "points": 0,
        "message": error.message,
    })

    out = {
        "tests": tests,
        "gradable": False
    }

    print(json.dumps(out))

def main():
    with open(INFO_PATH) as fp:
        info = json.load(fp)

    inst = info['params']['inst']

    inst_max_points = 95
    inst_weight = inst_max_points / 100
    reg_max_points = 100 - inst_max_points
    reg_weight = reg_max_points / 100

    netid = "student"  # To avoid a buttload of changes.

    with open('machine.v', 'r') as submission:
        with open('base/machine.v', 'r') as original:
            submission = remove_comments(submission)
            original = remove_comments(original)

    sub = set(submission)
    orig = set(original)
    difference = (sub - orig) | (orig - sub)
    difference.discard('\n')

    if not ( #mips_decode_changed(submission, original) and
      wire_new_inst_changed(submission, original) and
      modules_changed(submission, original) and
      len(difference) >= 5):
        too_similar()
        return

    tests = []

    regression_log = StringLogger()
    try:
        regression_total = run_suite(
            netid, 'regression', reg_weight, regression_log)
    except CompilationError as E:
        print_Compilation_Error(E)
        return


    tests.append({
        "name": "regression",
        "max_points": reg_max_points,
        "points": round(regression_total, 4),
        "output": regression_log.get_log().strip(),
        "succeeded": True,
    })

    instruction_log = StringLogger()

    def append_inst_test(name, points_rounded, max_points_rounded, test_log):
        tests.append({
            "name": name,
            "max_points": max_points_rounded,
            "points": points_rounded,
            "output": test_log.get_log().strip(),
            "succeeded": True,
        })

    try:
        instruction_total = run_suite(
            netid, inst, inst_weight, instruction_log, on_test=append_inst_test)
    except CompilationError as E:
        print_Compilation_Error(E)
        return

    total = regression_total + instruction_total

    out = {
        "tests": tests,
        "succeeded": True,
        "score": total / 100.0,
    }

    print(json.dumps(out))


if __name__ == "__main__":
    main()
