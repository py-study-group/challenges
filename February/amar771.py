'''
Caesar cipher
'''
import sys

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'


def encode(string, key):
    '''Encodes the string with the key of choice.'''

    try:
        key = int(key)
    except ValueError:
        return ("Key needs to be numerical value.")

    # Checks if the string will be the same after encoding
    if key % len(ALPHABET) == 0:
        return string

    encoded = ''
    for letter in string:
        if letter not in ALPHABET:
            encoded += letter

        else:
            encoded += ALPHABET[(ALPHABET.index(letter) + key) % len(ALPHABET)]

    return encoded


def decode_key(string, key):
    '''Decodes the string you provide with the key you provide'''

    try:
        key = int(key)
    except ValueError:
        return ("Key needs to be numerical value.")

    key = abs(key - len(ALPHABET))
    return encode(string, key)


def decode_bruteforce(string):
    '''Decodes the string by brute forcing all the results'''

    for number in range(len(ALPHABET), 0, -1):
        key = len(ALPHABET) - number
        print("Key ({0:2d}) - {1}".format(key, encode(string, number)))


if __name__ == '__main__':
    to_encode = 'abcz'
    encoded = encode(to_encode, 1)

    decode_bruteforce(encoded)
