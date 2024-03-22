import subprocess
import threading


class Command(object):
    """A subprocess wrapper supporting timeouts.

    After execution, members return_code, stdout, stderr and timed_out
    contain information about the executed process.
    """

    def __init__(self, args):
        """args is passed to the Popen constructor"""
        self.args = args
        self.process = None
        self.return_code = None
        self.stdout = None
        self.stderr = None
        self.timed_out = False

    def run(self, timeout=None):
        """timeout is in seconds and passed to thread.join"""
        def target():
            self.process = subprocess.Popen(
                self.args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            self.stdout, self.stderr = self.process.communicate()
            self.stdout = self.stdout.decode()
            self.stderr = self.stderr.decode()
            self.return_code = self.process.returncode

        thread = threading.Thread(target=target)
        thread.start()
        thread.join(timeout)
        if thread.is_alive():
            self.timed_out = True
            self.process.kill()
            thread.join()