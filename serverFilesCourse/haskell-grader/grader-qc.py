import os
import re
import json
import subprocess
import tempfile

PER_TEST_TIMEOUT_SECS = 2
STACK_RUN_COMMAND = [
    '/usr/local/bin/stack', 
    'test', 
    f'--test-arguments="--timeout={PER_TEST_TIMEOUT_SECS}"'
]

def main():

    grading_result = {}

    # Attempt to compile student code
    try:
        #'stack test' would compile and run tests cases at the same time
        subprocess.check_output(STACK_RUN_COMMAND, stderr=subprocess.STDOUT, timeout=60)

    except subprocess.CalledProcessError as e:
        # Compilation failed :(
        if re.search("=G=",e.output.decode('utf-8')):
            grading_result['succeeded'] = True
            # we're okay, the exit code is from a test failure
        else:
            grading_result['succeeded'] = False
            grading_result['score'] = 0.0
            grading_result['message'] = 'Compilation failed; \'stack test\' exited with error code {}. Check the code for infinite recursion or syntax errors.'.format(e.returncode)
            grading_result['output'] = re.sub('^.*/lib64/libtinfo.so.5: no version information available.*$','', e.output.decode('utf-8'), 0, re.M)

            print(json.dumps(grading_result))
            return
        # Stack test returns error code always.  Hm....
    except subprocess.TimeoutExpired:
        grading_result['succeeded'] = False
        grading_result['score'] = 0.0
        grading_result['message'] = 'Your code timed out.'
    except Exception as e:
        grading_result['succeeded'] = False
        grading_result['score'] = 0.0
        grading_result['message'] = 'Unspecified error; contact course staff: ' + str(e)
    # Student code compiled successfully!

    #read the output of terminal
    #Citation: fix the bug of subprocess.Popen for large output https://stackoverflow.com/questions/4408377/how-can-i-get-terminal-output-in-python
    with tempfile.TemporaryFile() as tempf:
        proc = subprocess.Popen(STACK_RUN_COMMAND, stdout=tempf)
        proc.wait(timeout=60)
        tempf.seek(0)
        tests_results_raw = tempf.read().decode().split('\n')

    #reorganized the raw test results: clean the empty strings and generate a well-organized dictionary

    # States
    # 0 = Normal
    # 1 = Reading an error (back to 0 on next =*= flag)
    # 2 = Reading an error on a =E= test (stop on next =*= flag)

    state = 0

    tests_results_itmd = list(filter(lambda s : s != '', tests_results_raw))
    tests_results_dict = {'Pass':{}, 'Fail':{}}

    groupName = ""
    message = ""
    points = 0
    allFail = False
    debug = False

    for line in tests_results_itmd:
        if debug:
           print(state, line)

        propPass = re.match(" *=[RPE]= (.*) \(([0-9]+) points\): .*OK.*",line)
        propFail = re.match(" *=P= (.*) \(([0-9]+) points\): .*(FAIL|Failed).*",line)
        reqFail = re.match(" *=R= (.*) \(([0-9]+) points\): .*(FAIL|Failed).*",line)
        errFail = re.match(" *=E= (.*) \(([0-9]+) points\): .*(FAIL|Failed).*",line)
        groupStart = re.match("=G= (.*)",line)
        wereDone = re.match("( *Properties *Total|[0-9]+ out of [0-9]+ tests)",line)

        if propPass:
            if debug:
               print("propPass")
            if state>=1:
                tests_results_dict['Fail'][testName] = (message,points)
                message = ""
                if state == 2:
                    break
                state= 0
            testName = groupName + " / " + propPass.group(1)
            points = int(propPass.group(2))
            state = 0
            tests_results_dict['Pass'][testName] = points
        elif propFail:
            if debug:
               print("propFail")
            if state>=1:
                tests_results_dict['Fail'][testName] = (message,points)
                message = ""
                if state == 2:
                    break
                state= 0
            testName = groupName + " / " + propFail.group(1)
            points = int(propFail.group(2))
            state = 1
        elif reqFail:
            if debug:
               print("reqFail")
            if state>=1:
                tests_results_dict['Fail'][testName] = (message,points)
                message = ""
                if state == 2:
                    break
                state= 0
            testName = groupName + " / All Or Nothing: " + reqFail.group(1)
            points = int(reqFail.group(2))
            state = 1
            allFail = True
        elif errFail:
            if debug:
               print("errFail")
            if state>=1:
                tests_results_dict['Fail'][testName] = (message,points)
                message = ""
                if state == 2:
                    break
                state= 0
            testName = groupName + " / Required to Proceed: " + errFail.group(1)
            points = int(reqFail.group(2))
            state = 2
            allFail = True
        elif groupStart:
            if debug:
               print("groupStart")
            if state>=1:
                tests_results_dict['Fail'][testName] = (message,points)
                message = ""
                if state == 2:
                    break
                state= 0
            groupName = groupStart.group(1)
        elif wereDone:
            if debug:
               print("wereDone")
            break
        elif state >= 1:
            message = message + "\n" + line

    if state>=1:
        tests_results_dict['Fail'][testName] = (message,points)
        message = ""

    #The final structure of tests_results_dict:
    #      {'Pass': {'Name1':Points1,'Name2':Points2},
    #       'Fail': {'Name3': ('Message3',Points3),
    #                'Name4': ('Message4',Points4)}
    #Final score calculation
    test_results = []
    total_points = 0
    earned_points = 0

    #Count the passed tests
    for (key,points) in tests_results_dict['Pass'].items():
        results = {}
        results['name'] = key
        results['max_points'] = points
        results['points'] = points

        total_points += points
        earned_points += points

        test_results.append(results)

    #Count the failed tests, and output the error message
    for (key,(message,points)) in tests_results_dict['Fail'].items():
        results = {}
        results['name'] = key
        results['max_points'] = points
        results['points'] = 0
        total_points += points

        results['message'] = message # + '\n' + "Check the 'Tests.hs' file in 'test' directory for individual test"

        test_results.append(results)


    grading_result['tests'] = test_results

    grading_result['succeeded'] = state < 2
    if total_points > 0:
        tscore = float(earned_points) / float(total_points)
    else:
        tscore = 0
    grading_result['score'] = tscore

    if allFail:
        grading_result['score'] = 0

    # Write the grading results to stdout
    print(json.dumps(grading_result))

if __name__ == '__main__':
    main()
