import prairielearn as pl
import random

def replace(c, alphabet, conversion):
    if c in alphabet:
        return conversion[alphabet.find(c)]
    elif c.lower() in alphabet:
        return conversion[alphabet.find(c.lower())].upper()
    else:
        return c

def encrypt(plaintext, alphabet, conversion):
    return ''.join([replace(c, alphabet, conversion) for c in plaintext])

def generate(data):

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    conversion = random.sample(alphabet, len(alphabet))

    list = [
        ['The', 'Some', 'One', 'My'],
        ["adorable", "clueless", "dirty", "odd", "happy"],
        ["puppy", "car", "rabbit", "friend", "monkey"],
        ["runs", "eats", "jumps", "drives", "plays"],
        ["crazily.", "recklessly.", "foolishly.", "merrily.", "occasionally."]
    ]
    plaintext = ' '.join([random.choice(component) for component in list])
    
    ciphertext = encrypt(plaintext, alphabet, conversion)
    
    data['params']['conversion_alphabet'] = ' '.join(conversion)
    data['params']['plaintext'] = plaintext

    data['correct_answers']['ciphertext'] = ciphertext
    
