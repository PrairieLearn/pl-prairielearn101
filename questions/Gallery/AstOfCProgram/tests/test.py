#! /usr/bin/python3

import cgrader
import clang.cindex

clang.cindex.Config.set_library_path("/usr/lib/")

def print_ast(node, indent=0):
    print(" " * indent + str(node.spelling) + " (" + str(node.kind) + ")")
    for child in node.get_children():
        print_ast(child, indent + 2)

def find_const_double(node):
    if (
        node.kind == clang.cindex.CursorKind.VAR_DECL
        and "double" in node.type.spelling
        and node.type.is_const_qualified()
    ):
        return node
    for child in node.get_children():
        found = find_const_double(child)
        if found is not None:
            return found
    return None

def var_name_is_valid(node):
    return not any(c.islower() for c in node.spelling)

def find_double_initializer(node):
    child = list(node.get_children())[0]
    return child if child.kind == clang.cindex.CursorKind.FLOATING_LITERAL else None

def initializer_is_scientific_notation(node):
    tokens = list(node.get_tokens())
    if tokens:
        literal = tokens[0].spelling
        return "e" in literal or "E" in literal
    return False

class QuestionGrader(cgrader.CPPGrader):
    def tests(self):
        index = clang.cindex.Index.create()
        translation_unit = index.parse("student.cpp", args=["-x", "c++"])
        # print_ast(translation_unit.cursor) # Uncomment to print the AST (be sure to comment out includes!)
        decl = find_const_double(translation_unit.cursor)
        if decl is None:
            self.add_test_result("const double not found", points=0, max_points=1)
            return
        self.add_test_result("const double found")
        if not var_name_is_valid(decl):
            self.add_test_result("variable name is not using the capitalization expected for a constant variable", points=0, max_points=1)
            return
        self.add_test_result("variable name is valid")
        initializer = find_double_initializer(decl)
        if initializer is None:
            self.add_test_result("variable does not have a double initializer", points=0, max_points=1)
            return
        self.add_test_result("variable has a double initializer")
        if not initializer_is_scientific_notation(initializer):
            self.add_test_result("initializer is not in scientific notation", points=0, max_points=1)
            return
        self.add_test_result("initializer is in scientific notation")
        self.test_compile_file(
            "student.cpp", "student", flags="-Wall -Wextra -pedantic -Werror"
        )
        self.test_run(
            "./student",
            input="65.00\n",
            exp_output="55.25",
            must_match_all_outputs="partial",
        )
        self.test_run(
            "./student",
            input="35.00\n",
            exp_output="29.75",
            must_match_all_outputs="partial",
        )
        self.test_run(
            "./student",
            input="77.00\n",
            exp_output="65.45",
            must_match_all_outputs="partial",
        )
        self.test_run(
            "./student",
            input="48.00\n",
            exp_output="40.8",
            must_match_all_outputs="partial",
        )
        self.add_test_result("code runs correctly")

g = QuestionGrader()
g.start()
