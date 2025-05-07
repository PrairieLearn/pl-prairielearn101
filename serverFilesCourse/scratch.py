import base64
import json
import os
import zipfile

def parse(data, filename='scratch.sb3'):
    try:
        files = data['submitted_answers']['_files']
    except KeyError:
        data['format_errors']['file'] = f'You should submit a file named "{filename}".'
        return

    # expect exactly one file
    if len(files) != 1:
        data['format_errors']['file'] = 'You should submit exactly one file.'
        return
    file = files[0]

    # check file name
    if file['name'] != filename:
        data['format_errors']['file'] = f'The file should be named "{filename}".'
        return

    # read the file
    with open('scratch.sb3', 'wb') as f:
        f.write(base64.b64decode(file['contents']))

    # extract the file
    try:
        with zipfile.ZipFile('scratch.sb3', 'r') as zip_ref:
            zip_ref.extractall('scratch')
    except Exception as e:
        data['format_errors']['file'] = f'The file did not extract properly: {e}.'
        return

    # read the project.json file
    try:
        with open('scratch/project.json', 'r') as f:
            project = json.loads(f.read())
    except Exception as e:
        data['format_errors']['file'] = f'The extracted file did not contain "project.json": {e}.'
        return

    # extract the information
    try: 
        with open('scratch/project.json', 'r') as f:
            project = json.loads(f.read())
    except Exception as e:
        data['format_errors']['file'] = f'"project.json" was not a proper JSON file: {e}.'
        return

    broadcasts = list()
    sprites = list()
    stages = list()
    variables = list()
    try:
        for target in project['targets']:
            if target['isStage']:
                for costume in target['costumes']:
                    stages.append(costume['name'])
            else:
                sprite = {'name': target['name'], 'blocks': []}
                for block in target['blocks'].values():
                    if 'opcode' not in block:
                        continue    # variables don't have opcodes
                    sprite['blocks'].append(block['opcode'])
                    sprite['blocks'].append(block['opcode'].split('_')[0])
                sprites.append(sprite)
            for variable in target['variables'].values():
                variables.append(variable[0])
            broadcasts.extend(target['broadcasts'].values())
    except Exception as e:
        data['format_errors']['file'] = f'An error occurred while processing "project.json": {e}.'
        return

    blocks = list()
    for sprite in sprites:
        blocks.extend(sprite['blocks'])

    data['submitted_answers']['blocks'] = blocks
    data['submitted_answers']['broadcasts'] = broadcasts
    data['submitted_answers']['stages'] = stages
    data['submitted_answers']['sprites'] = sprites
    data['submitted_answers']['variables'] = variables

    # clean up
    os.remove('scratch.sb3')
    for root, dirs, files in os.walk('scratch', topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))
    os.rmdir('scratch')
