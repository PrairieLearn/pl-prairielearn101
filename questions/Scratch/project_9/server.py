import sys
sys.path.insert(0, '/course/serverFilesCourse')
import scratch

def generate(data):
    pass

def parse(data):
    scratch.parse(data, 'scratch9.sb3')

def grade(data):
    points = 0
    correct_feedback = ''
    error_feedback = ''

    # three sprites
    spriteCount = len(data['submitted_answers']['sprites'])
    points += max(3, spriteCount)
    if spriteCount >= 3:
        correct_feedback += f'You have {spriteCount} sprite(s).<br>'
    else:
        error_feedback += 'You should have at least three sprites.<br>'

    # three stages
    backdropCount = len(data['submitted_answers']['stages'])
    points += max(3, backdropCount)
    if backdropCount >= 3:
        correct_feedback += f'You have {backdropCount} stage(s).<br>'
    else:
        error_feedback += 'You should have at least three stages.<br>'

    # one broadcast
    broadcastCount = len(data['submitted_answers']['broadcasts'])
    if broadcastCount > 0:
        points += 1
        correct_feedback += f'You have {broadcastCount} broadcast(s).<br>'
    else:
        error_feedback += 'You should have at least one broadcast.<br>'
    
    # one clone
    blocks = data['submitted_answers']['blocks']
    cloneCount = blocks.count('control_create_clone_of')
    if cloneCount > 0:
        points += 1
        correct_feedback += f'You have {cloneCount} block(s) to create a clone.<br>'
    else:
        error_feedback += 'You should have at least one block to create a clone.<br>'

    # one custom block ("procedures")
    blockCount = blocks.count('procedures_definition')
    if blockCount > 0:
        points += 1
        correct_feedback += f'You have {blockCount} custom block(s).<br>'
    else:
        error_feedback += 'You should have at least one custom block.<br>'
    
    # one variable
    varCount = len(data['submitted_answers']['variables'])
    if varCount > 0:
        points += 1
        correct_feedback += f'You have {varCount} variable(s).<br>'
    else:
        error_feedback += 'You should have at least one variable.<br>'
    
    # one loop
    loopCount = blocks.count('control_repeat') + blocks.count('control_forever')
    if loopCount > 0:
        points += 1
        correct_feedback += f'You have {loopCount} loop(s).<br>'
    else:
        error_feedback += 'You should have at least one loop.<br>'

    # one conditional
    conditionalCount = blocks.count('control_if') + blocks.count('control_if_else')
    if conditionalCount > 0:
        points += 1
        correct_feedback += f'You have {conditionalCount} conditional(s).<br>'
    else:
        error_feedback += 'You should have at least one conditional.<br>'
    
    # one event
    eventCount = blocks.count('event') - blocks.count('event_broadcast')    
    if eventCount > 0:
        points += 1
        correct_feedback += f'You have {eventCount} event(s).<br>'
    else:
        error_feedback += 'You should have at least one event.<br>'
        
    data['feedback']['correct'] = correct_feedback
    data['feedback']['error'] = error_feedback
    data['score'] = points / 13
