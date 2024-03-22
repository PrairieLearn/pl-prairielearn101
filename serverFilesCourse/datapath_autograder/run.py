from __future__ import division
from __future__ import print_function

import argparse
import importlib
import os

from command import Command
from description import Description
from string_logger import StringLogger


# def main():
#     parser = argparse.ArgumentParser(description='Datapath exam test runner')
#     parser.add_argument('exams', help='The directory containing the exams')
#     parser.add_argument('netid', help='The NetID to grade')
#     parser.add_argument('suite', help='The suite to grade')
#     parser.add_argument(
#         'test', nargs='?',
#         help='The test to grade; grade entire suite if omitted')
#     args = parser.parse_args()

#     log = StringLogger()
#     if args.test:
#         run_test(args.netid, args.suite, args.test, log, args.exams)
#     else:
#         run_suite(args.netid, args.suite, 1, log, args.exams)
#     print(log.get_log(), end='')

class CompilationError(Exception):
    """Raised when we have a Compliation Error ."""
    def __init__(self, message):
        self.message = message


def run_suite(netid, suite_name, suite_weight, log, on_test=None):
    expected_weight = 0.9
    unexpected_weight = 1 - expected_weight

    test_directory = 'tests'
    module_name = '.'.join((test_directory, suite_name))
    suite = importlib.import_module(module_name)
    total = 0
    for test_name, percentage in suite.tests:
        test_log = StringLogger()
        name, expected, unexpected = run_test(netid, suite_name, test_name,
                                              test_log)
        score = expected * expected_weight + unexpected * unexpected_weight
        max_points = suite_weight * percentage
        points = max_points * score
        total += points

        points_rounded = round(points, 4)
        max_points_rounded = round(max_points, 4)
        log.write('\nTesting {}: {}/{}\n'.format(
            name, points_rounded, max_points_rounded))
        log.append(test_log)

        if on_test:
            on_test(name, points_rounded, max_points_rounded, test_log)

    return total


def run_test(netid, suite_name, test_name, log):
    description = Description(suite_name, test_name)
    #log.write('Testing {}\n'.format(description.name))

    bin_path = compile(description, netid, log)
    if bin_path is None:
        return (description.name, 0, 0)

    run_command = Command([bin_path, '+' + description.base_path])
    run_command.run()  # No timeout, PL will do it for us.
    if run_command.timed_out:
        log.write('Execution timed out\n')
        return (description.name, 0, 0)

    try:
        pc_sequence, registers, memory = split_output(run_command.stdout)
        modified_score = grade_modified(
            description, pc_sequence, registers, memory, log)
        unmodified_score = grade_unmodified(
            description, pc_sequence, registers, memory, log)
    except ValueError:
        # student code didn't run successfully
        modified_score = 0
        unmodified_score = 0
    return (description.name, modified_score, unmodified_score)


def compile(description, netid, log):
    """returns compiled bin path, or None on failure"""
    script_path = os.path.dirname(os.path.realpath(__file__))
    base_directory = 'base'
    base_path = os.path.join(script_path, base_directory)

    student_dir = "/grade/run"
    # student_dir = os.path.join(exams_path, netid)
    ours = lambda path: os.path.join(base_path, path)
    theirs = lambda path: os.path.join(student_dir, path)

    ensure_directory_exists(description.bin_path)  # TODO: efficiency
    bin_name = netid + '_' + description.module_name
    bin_path = os.path.join(description.bin_path, bin_name)

    compile_args = [
        'iverilog',
        '-o', bin_path,
        ours('mips_defines.v'),
        ours('modules.v'),
        ours('mux_lib.v'),
        ours('rom.v'),
        theirs('machine.v'),
        description.test_bench_path,
    ]
    compile_command = Command(compile_args)
    compile_command.run()
    if compile_command.return_code != 0:
        log.write('Compilation failed:\n')
        stderr_without_path = compile_command.stderr.replace(
            student_dir + '/', '')
        log.write(stderr_without_path)
        raise CompilationError(stderr_without_path)

    return bin_path


def ensure_directory_exists(path):
    if not os.path.isdir(path):
        os.makedirs(path)


def split_output(output):
    lines = output.split('\n')
#     for line in lines:
#          print(line)

    pc_start = lines.index('PC values')
    pc_end = lines.index('', pc_start)
    pc_sequence = lines[pc_start + 1:pc_end]

    registers_start = lines.index('Registers')
    registers_end = lines.index('', registers_start)
    registers = lines[registers_start + 1:registers_end]

    memory_start = lines.index('Memory')
    memory_end = lines.index('', memory_start)
    memory = lines[memory_start + 1:memory_end]

    return pc_sequence, registers, memory


def grade_modified(description, pc_sequence, registers, memory, log):
    total = (len(description.modified_registers) +
             len(description.modified_memory) +
             int(description.pc_sequence is not None))
    correct = 0

    for register, value in sorted(description.modified_registers.items()):
        value = hexify(value)
        if registers[register] == value:
            log.write('Register {} had correct value {}\n'.format(
                register, registers[register]))
            correct += 1
        else:
            log.write('Register {} should have been {} but was {}\n'.format(
                register, value, registers[register]))

    for location, value in sorted(description.modified_memory.items()):
        address = hexify(0x10010000 + location * 4)
        value = hexify(value)
        if memory[location] == value:
            log.write('Address {} had correct value {}\n'.format(
                address, value))
            correct += 1
        else:
            log.write('Address {} should have been {} but was {}\n'.format(
                address, value, memory[location]))

    if description.pc_sequence is not None:
        expected_sequences = [x[1] for x in description.pc_sequence]
        expected_sequences = [[hexify(pc) for pc in s]
                              for s in expected_sequences]
        pc_sequence_str = ', '.join(pc_sequence)
        if pc_sequence in expected_sequences:
            index = expected_sequences.index(pc_sequence)
            instance = description.pc_sequence[index]
            percentage = instance[0]
            correct += percentage / 100
            if percentage == 100:
                log.write('PC sequence {} was correct\n'.format(
                    pc_sequence_str))
            else:
                explanation = instance[2]
                log.write('PC sequence {} was partially correct: {}\n'.format(
                    pc_sequence_str, explanation))
        else:
            log.write('PC sequence {} was incorrect\n'.format(pc_sequence_str))

    return correct / total


def grade_unmodified(description, pc_sequence, registers, memory, log):
    unmodified_registers = get_unmodified_registers(description)
    unmodified_memory = get_unmodified_memory(description)
    total = len(unmodified_registers) + len(unmodified_memory)
    correct = 0

    for register, value in sorted(unmodified_registers.items()):
        value = hexify(value)
        if registers[register] == value:
            correct += 1
        else:
            log.write('Register {} was unexpectedly modified from {} to {}\n'.
                      format(register, value, registers[register]))

    for location, value in sorted(unmodified_memory.items()):
        address = hexify(0x10010000 + location * 4)
        value = hexify(value)
        if memory[location] == value:
            correct += 1
        else:
            log.write('Address {} was unexpectedly modified from {} to {}\n'.
                      format(address, value, memory[location]))

    if correct == total:
        log.write('No registers or memory were unexpectedly modified\n')

    return correct / total


def get_unmodified_registers(description):
    default_value = 0x10010000
    unmodified_registers = {0: 0}
    for i in range(1, 32):
        if i not in description.modified_registers:
            unmodified_registers[i] = description.initial_registers.get(
                i, default_value)

    return unmodified_registers


def get_unmodified_memory(description):
    default_value = 0xdeadbeef
    unmodified_memory = {}
    for i in range(4):
        if i not in description.modified_memory:
            unmodified_memory[i] = description.initial_memory.get(
                i, default_value)

    return unmodified_memory


def hexify(value):
    if value < 0:
        value += 1 << 32

    return '0x{:08x}'.format(value)


# if __name__ == '__main__':
#     main()
