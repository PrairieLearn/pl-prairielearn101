# This problem was developed by Steven Wolfman, Karina Mochetti, Jordon Johnson, and Ricky Lau at UBC, 2025.
# It is available for use via a CC-BY-4.0 license: https://creativecommons.org/licenses/by/4.0/.
#
# The wordlist used below is based on Wikipedia work and so is available
# via a slightly more restricted license. See wordlist.py for more information.
from timehash import TimeHasher
from wordlist import SPELLABLE_WORDS

# Choose a bit of arbitrary text.
# Use the same text in conceptually the same "set of tutorial attendance questions".
# Two versions of the question with the same salt and granularity will show the same
# current answer at each time.
SALT = 'sample salt text; choose your own!'
GRANULARITY_SECONDS = 60  # Measure in minutes
LEEWAY_UNITS = 5          # Allow five minutes' leeway from receiving the answer.

def createHasher(data):
    return TimeHasher(data['params']['salt'], data['params']['granularitySeconds'], data['params']['items'])

def generate(data):
    data['params']['salt'] = SALT
    data['params']['granularitySeconds'] = GRANULARITY_SECONDS
    data['params']['items'] = SPELLABLE_WORDS
    data['params']['leeway'] = LEEWAY_UNITS
    data['params']['timeLimit'] = f'{GRANULARITY_SECONDS * LEEWAY_UNITS // 60} minutes'
    data['correct_answers']['code'] = 'TAs enter any text and click Save & Grade to see the code in the Show/Hide answer area'

def parse(data):
    # Set the correct answer here so it is accessible even if nothing was entered in the blank.
    data['correct_answers']['code'] = createHasher(data).get()

def grade(data):
    answer = data['submitted_answers']['code']
    hasher = createHasher(data)

    # always the current answer, even if a different valid answer is submitted
    data['correct_answers']['code'] = hasher.get()

    if hasher.matchesWithLeeway(answer, data['params']['leeway']):
        data['score'] = 1
        data['partial_scores']['code']['score'] = 1
        data['feedback']['code'] = 'This response is correct and has not expired.'
    else:
        data['score'] = 0
        data['partial_scores']['code']['score'] = 0
        data['feedback']['code'] = 'This response is incorrect or has expired.'
