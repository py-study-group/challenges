'''
Caesar cipher
'''
import argparse
import sys
from random import randint

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'


def encode(string, key=None):
    '''Encodes the string with the key of choice.'''
    randomized_key = False
    if not key:
        key = randint(1, 25)
        randomized_key = True

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

    if randomized_key:
        print("Your key has been randomized and it is --> {}".format(key))

    return encoded


def decode_key(string, key=None):
    '''Decodes the string you provide with the key you provide'''

    if not key:
        decode_bruteforce(string)
        sys.exit()

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


def help_description():
    print("\nTool for encrypting and decrypting text with Caesar cipher.\n")


def ask_key(encode=False, decode=False):
    if encode:
        print("What key do you want to use [1-{}]? (RETURN for random key.)".
              format(len(ALPHABET)))

    elif decode:
        print("What key do you want to use [1-{}]? (RETURN for brute-force)".
              format(len(ALPHABET)))
    key = input("--> ")

    return key


def args_actions(args):
    if args.text:
        text = args.text

    key = args.key
    if not key:
        key = ask_key(encode=args.encode, decode=args.decode)

    if args.encode:
        encoded = encode(text, key)
        print(encoded)

    elif args.decode:
        print(decode_key(text, key))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=help_description())
    parser.add_argument('-v', '--version',
                        action='version',
                        version='%(prog)s 1.2')

    parser.add_argument('text', type=str, help="text or file to encode")
    parser.add_argument('-k', '--key', type=int,
                        help="key to encode or decode with",
                        required=False)

    # Can't have -f and -t flags at the same time
    input_group = parser.add_mutually_exclusive_group()
    input_group.add_argument('-f', '--file',
                             action='store_true',
                             help='Add file to encode or decode')
    input_group.add_argument('-t', '--text',
                             action='store_true',
                             help='Type text to encode or decode')

    # You can encode or you can decode, can't do both
    action_group = parser.add_mutually_exclusive_group()
    action_group.add_argument('-e', '--encode',
                              action='store_true',
                              help='Encodes using a key or with random key')
    action_group.add_argument('-d', '--decode',
                              action='store_true',
                              help='Decodes using one of decode methods')

    args = parser.parse_args()
    try:
        args_actions(args)
    # Used for CTRL-C
    except KeyboardInterrupt:
        print('')
