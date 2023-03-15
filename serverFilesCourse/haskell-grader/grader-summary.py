import os
import re
import json
import subprocess
import tempfile

def main():

    grading_result = {}

    # Attempt to compile student code
    try:
        #'stack test' would compile and run tests cases at the same time
        subprocess.check_output(['/home/ag/.local/bin/stack', 'test'], stderr=subprocess.STDOUT, timeout=60)

    except subprocess.CalledProcessError as e:
        # Compilation failed :(
        if re.search("tests failed",e.output.decode('utf-8')):
            grading_result['succeeded'] = True
            # we're okay, the exit code is from a test failure
        else:
            grading_result['succeeded'] = False
            grading_result['score'] = 0.0
            grading_result['message'] = 'Compilation failed; \'stack test\' exited with error code {}'.format(e.returncode)
            grading_result['output'] = e.output.decode('utf-8')
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
        grading_result['message'] = 'Unspecified error; contact course staff'
    # Student code compiled successfully!

    #read the output of terminal
    #Citation: fix the bug of subprocess.Popen for large output https://stackoverflow.com/questions/4408377/how-can-i-get-terminal-output-in-python
    with tempfile.TemporaryFile() as tempf:
        proc = subprocess.Popen(['/home/ag/.local/bin/stack', 'test'], stdout=tempf)
        proc.wait(timeout=60)
        tempf.seek(0)
        tests_results_raw = tempf.read().decode().split('\n')

    #reorganized the raw test results: clean the empty strings and generate a well-organized dictionary

    # States
    # 0 = Normal
    # 1 = Reading an error (stop on =G= or =P=)

    state = 0

    tests_results_itmd = list(filter(lambda s : s != '', tests_results_raw))
    tests_results_dict = {'Pass':{}, 'Fail':{}}

    groupName = ""
    message = ""
    points = 0

    for line in tests_results_itmd:
        # print(state, line)

        wereDone = re.match('Score: ([0-9]+) / ([0-9]+)',line)

        propPass = re.match("Pass:.*=P= (.*) \(([0-9]+) points\)",line)
        propFail = re.match("Fail \[.*\]:.*=P= (.*) \(([0-9]+) points\)",line)
        groupStart = re.match(" *=G= (.*)",line)

        if propPass:
            if state==1:
                tests_results_dict['Fail'][testName] = (message,points)
                message = ""
                state= 0
            testName = groupName + " / " + propPass.group(1)
            points = int(propPass.group(2))
            state = 0
            tests_results_dict['Pass'][testName] = points
        elif propFail:
            if state==1:
                tests_results_dict['Fail'][testName] = (message,points)
                message = ""
                state= 0
            testName = groupName + " / " + propFail.group(1)
            points = int(propFail.group(2))
            state = 1
        elif groupStart:
            if state==1:
                tests_results_dict['Fail'][testName] = (message,points)
                message = ""
                state= 0
            groupName = groupStart.group(1)
        elif wereDone:
            if state==1:
                tests_results_dict['Fail'][testName] = (message,points)
                message = ""
                state= 0
            break
        elif state == 1:
            message = message + line

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

    grading_result['succeeded'] = True
    tscore = float(earned_points) / float(total_points)
    grading_result['score'] = tscore

    # Write the grading results to stdout
    print(json.dumps(grading_result))

if __name__ == '__main__':
    main()
