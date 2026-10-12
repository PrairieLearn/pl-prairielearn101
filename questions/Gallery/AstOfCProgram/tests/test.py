#! /usr/bin/python3

import cgrader
from clang.cindex import CursorKind, Index


def print_ast(node, indent=0):
    print(" " * indent + str(node.spelling) + " (" + str(node.kind) + ")")
    for child in node.get_children():
        print_ast(child, indent + 2)


def find_node(node, test):
    if node is None:
        return None
    if test(node):
        return node
    for child in node.get_children():
        found = find_node(child, test)
        if found is not None:
            return found
    return None


def find_const_double(node):
    return find_node(
        node,
        lambda n: (n.kind == CursorKind.VAR_DECL
        and "double" in node.type.spelling
        and node.type.is_const_qualified())
    )


def var_name_is_valid(node):
    return not any(c.islower() for c in node.spelling)


def find_double_initializer(node):
    child = list(node.get_children())[0]
    return child if child.kind == CursorKind.FLOATING_LITERAL else None


def initializer_is_scientific_notation(node):
    tokens = list(node.get_tokens())
    if tokens:
        literal = tokens[0].spelling
        return "e" in literal or "E" in literal
    return False


class QuestionGrader(cgrader.CPPGrader):
    def tests(self):
        index = Index.create()
        translation_unit = index.parse("student.cpp", args=["-x", "c++"])

        # Uncomment the following line to print the AST for development/debugging
        # print_ast(translation_unit.cursor)

        decl = find_const_double(translation_unit.cursor)
        self.add_test_result("const double found", points=(decl is not None))

        var_name_result = decl is not None and var_name_is_valid(decl)
        self.add_test_result("variable name is valid",
            points=1 if var_name_result else 0,
            output=None if var_name_result else "variable name is not using the capitalization expected for a constant variable"
        )

        initializer = find_double_initializer(decl)
        self.add_test_result("variable has a double initializer", 
            points=1 if decl is not None and initializer is not None else 0
        )

        self.add_test_result("initializer is in scientific notation",
            points=1 if decl is not None and initializer_is_scientific_notation(initializer) else 0
        )
        
        self.test_compile_file(
            "student.cpp", "student", flags="-Wall -Wextra -pedantic -Werror"
        )
        self.test_run(
            "./student",
            input="65.00\n",
            exp_output="55.25",
        )
        self.test_run(
            "./student",
            input="35.00\n",
            exp_output="29.75",
        )
        self.test_run(
            "./student",
            input="77.00\n",
            exp_output="65.45",
        )
        self.test_run(
            "./student",
            input="48.00\n",
            exp_output="40.8",
        )

g = QuestionGrader()
g.start()
