"""A description of a test"""

import importlib
import os

test_directory = 'tests'
output_directory = 'generated'
bin_directory = 'bin'
test_bench_suffix = '_tb.v'

class Description(object):
    def __init__(self, suite_name, test_name):
        module_name = '.'.join((test_directory, suite_name, test_name))
        description = importlib.import_module(module_name)

        self.module_name = test_name
        self.name = description.__doc__ or test_name
        self.instructions = self._process_instructions(description)
        self.initial_registers = getattr(description, 'initial_registers', {})
        self.initial_memory = getattr(description, 'initial_memory', {})
        self.modified_registers = getattr(
            description, 'modified_registers', {})
        self.modified_memory = getattr(description, 'modified_memory', {})
        self.pc_sequence = self._process_pc_sequence(description)

        script_dir_path = os.path.dirname(os.path.realpath(__file__))
        self.output_path = \
                os.path.join(script_dir_path, output_directory, suite_name)
        self.base_path = os.path.join(self.output_path, test_name)
        self.test_bench_path = self.base_path + test_bench_suffix
        self.bin_path = \
                os.path.join(script_dir_path, bin_directory, suite_name)

    @staticmethod
    def _process_instructions(description):
        def tuplify(instruction):
            if isinstance(instruction, tuple):
                return instruction
            else:
                return (None, instruction)

        return [tuplify(inst) for inst in description.instructions]

    @staticmethod
    def _process_pc_sequence(description):
        if not hasattr(description, 'pc_sequence'):
            return None

        pc_sequence = getattr(description, 'pc_sequence')
        if isinstance(pc_sequence[0], tuple):
            return pc_sequence
        else:
            return [(100, pc_sequence)]
