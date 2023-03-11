import os
import json
import subprocess
import tempfile

def main():

    grading_result = {}

    # Attempt to compile student code
    try:
        #'stack test' would compile and run tests cases at the same time
        subprocess.check_output(['/home/ag/.local/bin/stack', 'test'], timeout=60, stderr=subprocess.STDOUT)

    except subprocess.CalledProcessError as e:
        # Compilation failed :(
        grading_result['succeeded'] = False
        grading_result['score'] = 0.0
        grading_result['message'] = 'Compilation failed; \'stack test\' exited with error code {}'.format(e.returncode)
        grading_result['output'] = e.output.decode('utf-8')
        print(json.dumps(grading_result))
        return
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
    tests_results_itmd = list(filter(lambda s : s != '', tests_results_raw))
    tests_results_dict = {'Pass':[], 'Fail':{}}

    for elem in tests_results_itmd:
        temp = elem.split(': ')
        #if passed, temp  = elem.split(': ') would be like: ['Pass': 'checkLength']
        if temp[0] == 'Pass':
            tests_results_dict['Pass'].append(temp[1])
        #if failed, temp  = elem.split(': ') would be like: ['Fail [False,True,True,True,False,True,True]': 'checkLength']
        elif 'Fail' in temp[0]:
            tests_results_dict['Fail'][temp[1]] = temp[0]

    #The final structure of tests_results_dict:
    # {'Pass': ['checkLength', 'checkEqual'],
    #  'Fail': {'checkType': 'Fail [True,False,False,False,True]',
    #           'checkContent': 'Fail [True,False,False,False,True]'
    #          }
    # }

    #Final score calculation
    test_results = []
    total_points = 0
    earned_points = 0

    #Count the passed tests
    for test_passed in tests_results_dict['Pass']:
        results = {}
        results['name'] = test_passed
        results['max_points'] = 1
        total_points += 1

        results['points'] = 1
        earned_points += 1

        test_results.append(results)

    #Count the failed tests, and output the error message
    for key in tests_results_dict['Fail']:
        results = {}
        results['name'] = key
        results['max_points'] = 1
        total_points += 1

        results['points'] = 0
        results['message'] = tests_results_dict['Fail'][key] + '\n' + "Check the 'Tests.hs' file in 'test' directory for individual test"

        test_results.append(results)


    grading_result['tests'] = test_results

    grading_result['succeeded'] = True
    tscore = float(earned_points) / float(total_points)
    grading_result['score'] = tscore

    # Write the grading results to stdout
    print(json.dumps(grading_result))

if __name__ == '__main__':
    main()
