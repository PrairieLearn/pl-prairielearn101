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
    key = random.randrange(1, len(alphabet))
    conversion = (alphabet + alphabet)[key:]

    user = random.choice(['admin', 'root', 'john', 'bob', 'alice'])
    password = random.choice(['qwerty', 'liverpool', 'iloveyou', 'monkey', 'dragon'])
    
    plaintext1 = "USER %s" % (user)
    plaintext2 = "PASS %s" % (password)
    
    ciphertext1 = encrypt(plaintext1, alphabet, conversion)
    ciphertext2 = encrypt(plaintext2, alphabet, conversion)
    
    data['params']['ciphertext1'] = ciphertext1
    data['params']['ciphertext2'] = ciphertext2

    data['correct_answers']['plaintext1'] = plaintext1
    data['correct_answers']['plaintext2'] = plaintext2
    
