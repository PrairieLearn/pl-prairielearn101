import random


def generate(data):
    data['params'] = random.choice([
        {'scenario': "translate user-supplied text from one language to another", 'approach': "ask users for explicit feedback on each translation (thumbs up or thumbs down)",
        'correct': ["The response rate is likely to be low", "The user may not be a reliable judge of whether the prediction is good or not"],
        'incorrect': ["The model itself may influence the outcome, so it will be unclear whether the original prediction was correct or not", "The feedback loop is very long, so the intial inferred label may be premature"]
        },
        {'scenario': "decide which applicants should be approved for a one year bank loan", 'approach': "check whether approved applicants have paid back the loan at the end of the one-year loan period",
        'correct': ["The proposed approach only applies to positive samples, no feedback is available for predicted negative samples", "The proposed approach only applies to those who accept the terms of the loan, no feedback is available for those who are approved but decline the offer"],
        'incorrect': ["The response rate is likely to be low", "The inferred label is not a reliable indicator"]
        }
        
        
        ])