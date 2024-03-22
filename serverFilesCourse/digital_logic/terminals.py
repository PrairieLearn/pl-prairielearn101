from digital_logic.constants import *
from random import choice

class Terminals():
    '''
    helper class for generating boolean expressions
    code converted to Python from clientFilesCourse/expression.js
    relies on the expression templates from the constants.py file
    '''

    def __init__(self, num_terminals):
        # list of terminals still available
        # complement is stored as capital numbers
        # supports up to 6 terminals
        self.terminal_names = VAR_NAMES[:num_terminals]
        self.available_terminals = VAR_NAMES[:num_terminals] + [c.upper() for c in VAR_NAMES[:num_terminals]]

    def get_random_terminal(self):
        return choice(self.available_terminals)

    def remove_terminal(self, term):
        if term in self.available_terminals:
            self.available_terminals.remove(term)

    def output_terminal(self, term):
        if term.isupper():
            return term.lower() + "'"

        return term

    def complement_terminal(self, term):
        if term.isupper():
            return term.lower()

        return term.upper()

    def get_random_has_complement_terminal(self):
        options = []

        for terminal in self.terminal_names:
            if terminal in self.available_terminals and self.complement_terminal(terminal) in self.available_terminals:
                options.append(terminal)
                options.append(self.complement_terminal(terminal))

        if len(options) == 0:
            print("couldn't find a terminal")
            return 'g'

        else:
            return choice(options)

    def remove_complement(self):
        term = choice(self.available_terminals)
        self.available_terminals.remove(self.complement_terminal(term))

        return term

    def get_complement_terminal(self):
        term = choice(self.available_terminals)

        return term.upper() 