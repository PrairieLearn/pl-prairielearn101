#! /usr/bin/python3
import cgrader
import json

class DemoGrader(cgrader.CGrader):
    def tests(self):


        self.test_compile_file(
            "foo.c",
            "main",
            add_c_file="/grade/tests/main.c",
            # The following must be included if compiling a Check test
            pkg_config_flags="check",
        )
        self.run_check_suite("./main")

g = DemoGrader()
g.start()
