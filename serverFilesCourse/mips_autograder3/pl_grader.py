from __future__ import division, print_function

import json
import os
import concurrent.futures
import itertools
import subprocess

QTSPIM_CMD = os.getenv("QTSPIM_CMD", "./spim")
INFO_PATH = os.getenv("INFO_PATH", "/grade/data/data.json")

REGULAR_WEIGHT = 100
EVIL_WEIGHT = 100 - REGULAR_WEIGHT
NUM_TESTS = 1
TIMEOUT = 5

EXPECTED = "EXPECTED: {expected}\nGOT: {got}\n"


def format_subp_error(e):
    if isinstance(e, (subprocess.TimeoutExpired, subprocess.CalledProcessError)):
        stdout = e.stdout.rstrip()
        stderr = e.stderr.rstrip()
        return "{}\n--- stdout ---\n{}\n--- stderr ---\n{}".format(e, stdout, stderr)

    return str(e)

def check_regular(expected, got):
    expected = expected.rstrip("\n")
    got = got.rstrip("\n")

    if expected == got:
        return "PASSED", 1.0

    msg = EXPECTED.format(expected=expected, got=got)
    return msg, 0.0


def check_evil(expected, got):
    soln_output = expected.rstrip("\n")
    got = got.rstrip("\n")

    student_lines = got.split("\n")

    if not student_lines:
        return "NO OUTPUT", 0.0

    if len(student_lines) != 3:
        student_lines = [student_lines[0], "", ""]

    student_output = student_lines[0].rstrip("\n")
    student_stack = student_lines[1].rstrip("\n")
    student_saved = student_lines[2].rstrip("\n")

    score = 0
    sub_report = ""
    correct_flag = False
    if soln_output == student_output:
        score += 1
        correct_flag = True
        sub_report += "Correct output\n"
    else:
        sub_report += EXPECTED.format(expected=soln_output, got=student_output)

    if student_stack == "yes-stack":
        if correct_flag:
            score += 1
        sub_report += "Returned the stack pointer\n"
    else:
        sub_report += "Didn't return the stack pointer :(\n"

    if student_saved == "yes-saved":
        if correct_flag:
            score += 3
        sub_report += "Correctly saved $s registers\n"
    else:
        sub_report += "Modified $s registers :(\n"

    return sub_report, score / 5


def grade(soln_path, student_s, test_num, evil, correct, regular_weight, evil_weight, numTests):
    weight = regular_weight if not evil else evil_weight

    output = {
        "name": "Test {}".format(test_num) + (" (evil)" if evil else ""),
        "max_points": weight / numTests,
        "points": 0,
        "output": "",
    }

    if not evil:
        main_file = os.path.join(
            soln_path, "main_{test_num}.s".format(test_num=test_num))
    else:
        main_file = os.path.join(
            soln_path, "main_evil_{test_num}.s".format(test_num=test_num))

    try:
        # subprocess.run is new in Python 3.5, and it's awesome.
        result = subprocess.run(
            QTSPIM_CMD + " -f " + " ".join([student_s, main_file]),
            shell=True, timeout=TIMEOUT, check=True,
            stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            encoding="utf-8", errors="ignore",
        )

    except Exception as e:
        output["output"] = format_subp_error(e).rstrip()
        output["gradable"] = False
        return output

    if not evil:
        message, percentage = check_regular(correct, result.stdout)
    else:
        message, percentage = check_evil(correct, result.stdout)

    output["output"] = message.rstrip()
    output["points"] = round(output["max_points"] * percentage, 4)
    return output

def main():
    with open(INFO_PATH) as fp:
        info = json.load(fp)

    problem = info['params']['problem']

    soln_path = os.path.join("out_soln", problem)
    details_path = os.path.join(soln_path, "details.json")

    with open(details_path) as fp:
        details = json.load(fp)
        student_s = problem + ".s"

    # output_path = os.path.join(soln_path, "output.txt")

    # with open(output_path) as fp:
        # correct = [line.rstrip('\n') for line in fp]
    correct = info['params']['correct']
    numTests = info['params']['numTests']
    regular_weight = info['params']['regular_weight']
    evil_weight = 100 - regular_weight
    evil_tests = info['params']['evilTests']

    if evil_tests:
        with concurrent.futures.ThreadPoolExecutor() as executor:
            args = [
                (soln_path, student_s, i, evil, correct[i], regular_weight, evil_weight, numTests)
                for evil, i in itertools.product([False,True], range(numTests))
            ]

            results = executor.map(lambda p: grade(*p), args)
    else:
        with concurrent.futures.ThreadPoolExecutor() as executor:
            args = [
                (soln_path, student_s, i, evil, correct[i], regular_weight, evil_weight, numTests)
                for evil, i in itertools.product([False], range(numTests))
            ]

            results = executor.map(lambda p: grade(*p), args)


    tests = list(results)

    # Examine tests to decide sucessful grading
    gradable = True
    oneTestWithError = []
    for t in tests:
        if 'gradable' in t.keys():
            if t['gradable'] == False:
                del t['gradable']
                oneTestWithError.append(t)
                gradable = False
                break

    if gradable == False:
        out = {
            "gradable": False,
            "tests": oneTestWithError,
            "score": round(sum(t["points"] for t in tests) / 100, 4),
        }
    else:
        out = {
            "tests": tests,
            "score": round(sum(t["points"] for t in tests) / 100, 4),
        }

    print(json.dumps(out))


if __name__ == "__main__":
    main()
