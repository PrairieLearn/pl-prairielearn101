class StringLogger(object):
    """A simple logger to an internal buffer"""

    def __init__(self):
        self.lines = []

    def write(self, message):
        self.lines.append(message)

    def append(self, other):
        self.lines.extend(other.lines)

    def get_log(self):
        return ''.join(self.lines)
