#! python3

# CaesarCipher.py - this program encodes/decodes strings passed to it as input

import random


def encode(shift, text):
    char_list = []
    for i in range(len(text)):
        character = text[i]
        new_character = ''
        if character in special:
            char_list.append(character)
        elif character in alphabet:
            if alphabet.index(character) + shift > len(alphabet) - 1:
                new_character = alphabet[alphabet.index(character) + shift - len(alphabet)]
            else:
                new_character = alphabet[alphabet.index(character) + shift]
        elif character in cap_alphabet:
            if cap_alphabet.index(character) + shift > len(cap_alphabet) - 1:
                new_character = cap_alphabet[cap_alphabet.index(character) + shift - len(cap_alphabet)]
            else:
                new_character = cap_alphabet[cap_alphabet.index(character) + shift]
        else:
            new_character = character
        char_list.append(new_character)
    response = 'Encoded string: ' + ''.join(char_list)
    print(response)


def decode(shift, text):
    char_list = []
    for i in range(len(text)):
        character = text[i]
        new_character = ''
        if character in special:
            char_list.append(character)
        elif character in alphabet:
            if alphabet.index(character) - shift < 0:
                new_character = alphabet[alphabet.index(character) - shift + len(alphabet)]
            else:
                new_character = alphabet[alphabet.index(character) - shift]
        elif character in cap_alphabet:
            if cap_alphabet.index(character) - shift < 0:
                new_character = cap_alphabet[cap_alphabet.index(character) - shift + len(cap_alphabet)]
            else:
                new_character = cap_alphabet[cap_alphabet.index(character) - shift]
        else:
            new_character = character
        char_list.append(new_character)
    response = 'Decoded string: ' + ''.join(char_list)
    print(response)


alphabet = 'abcdefghijklmnopqrstuvwxyz'
cap_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
special = [' ', '_' ',', '-', '!', '?', '@', ':', ';', '.', '#', '$', '%', '&', '*', '(', ')', '+', '=', '[', ']']


if __name__ == '__main__':
    print('Please input a string.')
    my_string = input()
    #while all(x.isalpha() or x.isspace() or x in special for x in my_string) is not True:
        #print('Cannot use string. Input must be composed of alphabetic characters only.')
        #my_string = input()
    print('Would you like to encode (e) or decode (d) the string?')
    encode_or_decode = input()
    while encode_or_decode not in ['e', 'd']:
        print("Please input 'e' for encoding or 'd' for decoding.")
        encode_or_decode = input()
    if encode_or_decode == 'e':
        r = random.randint(1, 25)
        encode(r, text=my_string)
        print('The shift applied to the text was s = ' + str(r) + '.')
    elif encode_or_decode == 'd':
        print('Please inform the shift of the code.')
        informed_shift = input()
        while informed_shift.isnumeric() is False:
            print('Cannot decode. Shift must be a whole number.')
            informed_shift = input()
        decode(int(informed_shift), text=my_string)
