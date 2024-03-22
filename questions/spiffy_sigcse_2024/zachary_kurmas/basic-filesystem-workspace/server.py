import random 
import re
import string

def generate(data):
    data['params']['names_for_user'] = []
    data["params"]["names_from_user"] = []

    correct_answers = data["correct_answers"]

    num_existing_courses = 3
    courses = [f"CIS{c}" for c in ['501', '511', '512', '654', '655', '658', '660', '671', '672', '678', '685', '693', '699']]
    all_course_choices = random.sample(courses, k=num_existing_courses + 1)
    course_choices = all_course_choices[0:num_existing_courses]
    p_course_to_copy_instructions = random.choice(course_choices)
    p_full_path_course = random.choice(course_choices)
   
    p_new_course = all_course_choices[num_existing_courses -1]
   
    all_directories_in_home = ['Music', 'Desktop', 'Downloads', 'Documents', 'Contacts', "Movies", 'Library' ]
    all_directories_content = {
        'Music': 'songXX.mp3',
        'Documents': 'reportXX.docx',
        'Contacts': 'contactsXX.xml',
        'Movies': 'movieXX.mp4',
        'Library': 'libXX.lib'
    }
    num_dirs_in_home = random.randint(2,6)
    directories_in_home = random.sample(all_directories_in_home, k=num_dirs_in_home)

    picture_types = ['jpeg', 'png', 'gif', 'pbm', 'bmp', 'tiff', 'eps']

    new_directories_in_home = ['Budget', 'Taxes', 'Personal', 'Games', 'Recipes', 'Contacts']
    p_new_directory_in_home = random.choice(new_directories_in_home)

    hidden_files = ['.android', '.bash_history', '.bash_profile', '.bashrc', '.bundle', 
                    '.cache', '.config', '.cups', '.docker', '.gem', '.emacs.d', '.macports', '.npm', 
                    '.nvm', '.profile', '.ssh', '.zlogin', '.zshrc']

    p_num_hidden = random.randint(3, 7)
    chosen_hidden = random.sample(hidden_files, k=p_num_hidden)
    correct_answers["num_hidden"] = p_num_hidden + 2
    correct_answers["last_hidden"] = sorted(chosen_hidden)[-1]

    project_files = ['my_game.py', 'analysis1.py', 'demo1.py', 'simulate.py']
    p_project_file = random.choice(project_files)


    ws_files = []
    for course in course_choices:
        ws_files.append({"name": f"Courses/{course}/Projects/p1/instructions.txt", "contents": "Do something cool"})
        ws_files.append({"name": f"Courses/{course}/Projects/p1/{p_project_file}", "contents": "# A cool python game"})
        ws_files.append({"name": f"Courses/{course}/Projects/p1/a_cool_library.py", "contents": "# A cool python library game"})
        ws_files.append({"name": f"Courses/{course}/Projects/p2/instructions.txt", "contents": "Do more cool stuff"})
        ws_files.append({"name": f"Courses/{course}/Notes/lecture1.txt", "contents": "Yadda, yadda, yadda"})
        ws_files.append({"name": f"Courses/{course}/Notes/lecture2.txt", "contents": "Blah, Blah, Blah"})
        ws_files.append({"name": f"Courses/{course}/Notes/lecture3.txt", "contents": "Yap, Yap, Yap"})

    for hf in chosen_hidden:
        ws_files.append({"name": hf, "contents": f"Just some random content. Nothing special"})

    added_files = []
    for d in directories_in_home:
        num_files = random.randint(2, 7)
        for i in range(1,num_files):           
            raw_filename = all_directories_content.get(d, random.choice(list(all_directories_content.values())))
            filename = raw_filename.replace('XX', str(i)) 
            ws_files.append({"name": f"{d}/{filename}", "contents": "Stuff!!"})
            added_files.append({"dir": d, "name": filename})

    p_pict_type_for_size = random.choice(picture_types)
    p_largest = 0
    for pt in picture_types:
        num_of_type = random.randint(5, 10)
        for i in range(0, num_of_type):
            index = random.randint(0,9999)
            content = ''.join(random.choice(string.ascii_letters) for i in range(random.randint(5000,15000)))
            ws_files.append({"name": f"Pictures/IMG{index:04d}.{pt}", "contents": content})
            if pt == p_pict_type_for_size and (len(content) > p_largest):
                p_largest = len(content)
    correct_answers["largest_size"] = p_largest

    [to_move, to_copy] = random.sample(added_files, k=2)
    p_file_to_move = to_move["name"]
    p_dir_to_move = to_move["dir"]
    p_dest_dir = random.choice([x for x in directories_in_home if x != p_dir_to_move])

    p_file_to_copy = to_copy["name"]
    p_dir_to_copy = to_copy["dir"]

    p_pict_type_to_copy = random.choice(picture_types)


    if random.randint(0, 1) == 0:
        p_full_path_dir = 'project 1'
        p_full_path_file = p_project_file
        correct_answers['full_path'] = f'/home/jovyan/Courses/{p_full_path_course}/Projects/p1/{p_full_path_file}'
    else:
        p_full_path_dir = 'Notes'
        index = random.randint(1,3)
        p_full_path_file = f"lecture{index}.txt"
        correct_answers['full_path'] = f'/home/jovyan/Courses/{p_full_path_course}/Notes/{p_full_path_file}'

    #  
    # Final setup
    #
    params = data["params"]                        
    params['_workspace_files'] = ws_files
    params["course_to_copy_instructions"] = p_course_to_copy_instructions
    params["new_course"] = p_new_course
    params["num_hidden"] = p_num_hidden
    params["new_directory_in_home"] = p_new_directory_in_home
    params["project_file"] = p_project_file
    params["file_to_move"] = p_file_to_move
    params["dir_to_move"] = p_dir_to_move
    params["dest_dir"] = p_dest_dir
    params["file_to_copy"] = p_file_to_copy
    params["dir_to_copy"] = p_dir_to_copy
    params["pict_type_to_copy"] = p_pict_type_to_copy
    params["pict_type_for_size"] = p_pict_type_for_size
    params["full_path_course"] = p_full_path_course
    params["full_path_dir"] = p_full_path_dir
    params["full_path_file"] = p_full_path_file


def grade(data):

    # setattr(data, 'set_partial_score', set_partial_score)

    # mk_in_home (Q1)
    to_make = data["params"]["new_directory_in_home"]
    observed = data["submitted_answers"]["mk_in_home"].strip()
    expected = re.compile(f'^mkdir\\s+{to_make}(/*)$')
    if (expected.match(observed)): 
        data["partial_scores"]["mk_in_home"] = {"score": 1.0}
    elif "mkdir" in observed:
        data["partial_scores"]["mk_in_home"] = {"score": 0.25}
    else:
        data["partial_scores"]["mk_in_home"] = {"score": 0.0}


    # mk_in_courses (Q2)
    to_make = data["params"]["new_course"]
    observed = data["submitted_answers"]["mk_in_courses"].strip()
    expected = re.compile(f'^mkdir\\s+(-p\\s+)?(/home/jovyan/)?Courses/{to_make}(/*)$')
    if (expected.match(observed)): 
        data["partial_scores"]["mk_in_courses"] = {"score": 1.0}
    elif "mkdir" in observed:
        data["partial_scores"]["mk_in_courses"] = {"score": 0.25}
    else:
        data["partial_scores"]["mk_in_courses"] = {"score": 0.0}


    # cd_before_copy (Q4a)
    target_course = data["params"]["course_to_copy_instructions"]
    observed = data["submitted_answers"]["cd_before_copy"].strip()
    expected = re.compile(f'^cd\\s+(/home/jovyan/)?Courses/{target_course}/Projects/p1(/)?$')
    if (expected.match(observed)): 
        data["partial_scores"]["cd_before_copy"] = {"score": 1.0}
    elif "cd" in observed and target_course in observed and "Projects" in observed and "p1" in observed:
        data["partial_scores"]["cd_before_copy"] = {"score": 0.5}
    elif "cd" in observed:
         data["partial_scores"]["cd_before_copy"] = {"score": 0.25}
    else:
        data["partial_scores"]["cd_before_copy"] = {"score": 0.0}

    # copy_to_sibling (Q4b)
    file_to_copy = data["params"]["project_file"]
    observed = data["submitted_answers"]['copy_to_sibling'].strip()
    expected = re.compile(f'^cp\\s+{file_to_copy}\\s+\\.\\./p2(/{file_to_copy})?$')
    if (expected.match(observed)):
        data["partial_scores"]["copy_to_sibling"] = {"score": 1.0}
    elif 'cp' in observed and file_to_copy in observed and '..' in observed:
        data["partial_scores"]["copy_to_sibling"] = {"score": 0.5}
    elif 'cp' in observed and (file_to_copy in observed or '..' in observed):
        data["partial_scores"]["copy_to_sibling"] = {"score": 0.25}
    else:
        data["partial_scores"]["copy_to_sibling"] = {"score": 0.0}

    # return_home (Q5)
    observed = data["submitted_answers"]['return_home'].strip()
    parts = re.search("^cd\\s+(.*)$", observed)
    if not parts:
        data["partial_scores"]["return_home"] = {"score": 0.1}
    elif parts.group(1) == '/home/jovyan' or parts.group(1) == '../../../..' or parts.group(1) == '~' or parts.group(1) == '~jovyan':
        data["partial_scores"]["return_home"] = {"score": 1.0}
    else:
        data["partial_scores"]["return_home"] = {"score": 0.0}
    
    # move_file (Q6)
    source_dir = data["params"]["dir_to_move"]
    source_file = data["params"]["file_to_move"]
    dest_dir = data["params"]["dest_dir"]
    observed = data["submitted_answers"]['move_file'].strip()  
    expected = re.compile(f'^mv\\s+{source_dir}/{source_file}\\s+{dest_dir}(/|/{source_file})?$')
    if (expected.match(observed)):
        data["partial_scores"]["move_file"] = {"score": 1.0}
    elif 'mv' in observed:
        data["partial_scores"]["move_file"] = {"score": 0.25}
    else:
        data["partial_scores"]["move_file"] = {"score": 0.0}

    # copy_file (Q7)
    source_dir = data["params"]["dir_to_copy"]
    source_file = data["params"]["file_to_copy"]
    observed = data["submitted_answers"]['copy_file'].strip()  
    expected = re.compile(f'^cp\\s+{source_dir}/{source_file}\\s+(\\.|/home/jovyan|~)(/|/{source_file})?$')
    if (expected.match(observed)):
        data["partial_scores"]["copy_file"] = {"score": 1.0}
    elif 'cp' in observed:
        data["partial_scores"]["copy_file"] = {"score": 0.25}
    else:
        data["partial_scores"]["copy_file"] = {"score": 0.0}

    # copy_images (Q8)
    img_type = data["params"]["pict_type_to_copy"]
    observed = data["submitted_answers"]['copy_images'].strip()  
    expected = re.compile(f'^cp\\s+Pictures/(IMG)?\\*(\\.)?{img_type}\\s+/tmp(/)?$')
    if (expected.match(observed)):
        data["partial_scores"]["copy_images"] = {"score": 1.0}
    elif 'mv' in observed:
        data["partial_scores"]["copy_images"] = {"score": 0.25}
    else:
        data["partial_scores"]["copy_images"] = {"score": 0.0}

    # command_for_size (Q9)
    observed = data["submitted_answers"]['command_for_size'].strip()  
    expected = re.compile(f'^ls\\s+-(.*)l')
    if (expected.match(observed)):
        data["partial_scores"]["command_for_size"] = {"score": 1.0}
    elif 'ls' in observed:
        data["partial_scores"]["command_for_size"] = {"score": 0.5}
    elif '-l' in observed:
        data["partial_scores"]["command_for_size"] = {"score": 0.5}
    else:
        data["partial_scores"]["command_for_size"] = {"score": 0.0}    

    score = 0
    for key, value in data["partial_scores"].items():
        score += value["score"]
    data["score"] = score / len(data["partial_scores"])