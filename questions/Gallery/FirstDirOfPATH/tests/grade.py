import subprocess, shlex, random, os, json, shutil, re, traceback

with open('/grade/data/data.json') as raw_data:
    data = json.load(raw_data)
    correct_answer = data['correct_answers']['command']
    student_answer = data['submitted_answers']['command']

tests = [
    '/cs/home/jonatanstu/bin:/usr/share/Modules/bin:/usr/bin:/bin:/usr/sbin:/sbin:/xsys/bin:/usr/local/sbin',
    '/home/jonatan/.local/bin:/home/jonatan/bin:/home/jonatan/node_modules/.bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/usr/lib/wsl/lib:/mnt/c/Python310/Scripts/:/mnt/c/Python310/:/mnt/c/Windows/system32:/mnt/c/Windows:/mnt/c/Windows/System32/Wbem:/mnt/c/Windows/System32/WindowsPowerShell/v1.0/:/mnt/c/Windows/System32/OpenSSH/:/mnt/c/Program Files/NVIDIA Corporation/NVIDIA NvDLISR:/mnt/c/Program Files (x86)/NetSarang/Xmanager 7/:/mnt/c/Program Files (x86)/NetSarang/Xshell 7/:/mnt/c/Program Files (x86)/NetSarang/Xftp 7/:/mnt/c/Program Files (x86)/NetSarang/Xlpd 7/:/mnt/c/Android:/mnt/c/WINDOWS/system32:/mnt/c/WINDOWS:/mnt/c/WINDOWS/System32/Wbem:/mnt/c/WINDOWS/System32/WindowsPowerShell/v1.0/:/mnt/c/WINDOWS/System32/OpenSSH/:/mnt/c/Program Files/nodejs/:/mnt/c/ProgramData/chocolatey/bin:/mnt/c/Program Files (x86)/Pulse Secure/VC142.CRT/X64/:/mnt/c/Program Files (x86)/Pulse Secure/VC142.CRT/X86/:/mnt/c/Program Files (x86)/NVIDIA Corporation/PhysX/Common:/mnt/c/WINDOWS/system32:/mnt/c/WINDOWS:/mnt/c/WINDOWS/System32/Wbem:/mnt/c/WINDOWS/System32/WindowsPowerShell/v1.0/:/mnt/c/WINDOWS/System32/OpenSSH/:/mnt/c/Program Files/Docker/Docker/resources/bin:/mnt/c/Users/jonat/AppData/Local/Microsoft/WindowsApps:/mnt/c/Program Files/Emacs/x86_64/bin:/mnt/c/Users/jonat/AppData/Roaming/npm:/mnt/c/Program Files (x86)/Nmap:/snap/bin:/home/jonatan/.local/bin',
    '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
]

results = {
    'points': 0,
    'max_points': 0,
    'gradable': True,
    'tests': []
}

subprocess.run(['useradd', 'sbuser'])
shutil.copyfile('/etc/passwd', '/etc/passwd_backup')

for index, path in enumerate(tests):
    correct = student = ''
    try:
        correct_result = subprocess.run(['/bin/bash', '-c', f'export PATH="{path}"; {correct_answer}'],
                                        stderr=subprocess.STDOUT, stdout=subprocess.PIPE)
        correct = correct_result.stdout.decode()
        student_result = subprocess.run(
            ['su', 'sbuser', '-s', '/bin/bash', '-c', f'export PATH="{path}"; {student_answer}'],
            stderr=subprocess.STDOUT, stdout=subprocess.PIPE, timeout=1)
        student = student_result.stdout.decode()
    except subprocess.TimeoutExpired as e:
        print(e)
        student = '(process timed out)'
    except Exception as e:
        print(e)
        student = '(error attempting to run command)'
    points = 1 if re.sub('\\s+', ' ', correct.strip()) == re.sub('\\s+', ' ', student.strip()) else 0
    results['points'] += points
    results['max_points'] += 1
    results['tests'].append({
        'name': f'Test {index}',
        'description': path,
        'output': student,
        'message': f'Expected:\n{correct}',
        'points': points,
        'max_points': 1
    })

results['score'] = results['points'] / results['max_points']
if not os.path.exists('/grade/results'): os.makedirs('/grade/results')
with open('/grade/results/results.json', 'w') as result_file:
    json.dump(results, result_file)
