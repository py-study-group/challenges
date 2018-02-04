#!/usr/bin/python

'''
Caesar cipher encoder/decoder (Intermediate)
'''

import argparse, os


__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
ALPHABET_LEN = 26
ASCII = [65, 90, 97, 122]

class String:
    '''Represents the message to be encoded/decoded.
    This class is used to encode and decode messages.

    Attributes:
        string (str): The message to be encoded/decoded.
        shift  (int): The amount to shift the message by.

    '''
    
    def __init__(self, string, shift = 0):
        '''This is the __init__ method.

        Args:
            string (str): The message to be encoded/decoded.
            shift (int, optional): The amount to shift the message by.

        '''
        self.string = string
        self.shift = shift
        
    def encodeHashTable(self):
        '''Encodes message using a hash table implementation.
        
        Returns:
            str: Encoded message.

        '''
        encodedValues = ALPHABET[self.shift:] + ALPHABET[:self.shift]
        encodeMap = dict(zip(ALPHABET, encodedValues))
        return('Encoded sentence: {}'.format(''.join([encodeMap[c] if c.islower() else encodeMap[c.lower()].upper() if c.lower() in encodeMap else c for c in self.string])))

    def decodeHashTable(self):
        '''Decodes message using a hash table implementation.

        Returns:
            str: Decoded message.

        '''
        decodedValues = ALPHABET[-self.shift:] + ALPHABET[:-self.shift]
        decodeMap = dict(zip(ALPHABET, decodedValues))
        return('Decoded sentence: {}'.format(''.join([decodeMap[c] if c.islower() else decodeMap[c.lower()].upper() if c.lower() in decodeMap else c for c in self.string])))
    
    def encodeOrdinal(self):
        '''Encodes message using ordinals, with the ugliest possible list comprehension.

        Returns:
            str: Encoded message.

        '''
        return('Encoded sentence: {}'.format(''.join([chr(ord(c)+self.shift) if ( (c.isupper() and (ord(c)+self.shift >= ASCII[0] and ord(c)+self.shift <= ASCII[1]) ) or (c.islower() and (ord(c)+self.shift >= ASCII[2] and ord(c)+self.shift <= ASCII[3]) ) ) else chr(ord(c)+self.shift-ALPHABET_LEN) if ( (c.isupper() and (ord(c)+self.shift-ALPHABET_LEN >= ASCII[0] and ord(c)+self.shift-ALPHABET_LEN <= ASCII[1]) ) or (c.islower() and (ord(c)+self.shift-ALPHABET_LEN >= ASCII[2] and ord(c)+self.shift-ALPHABET_LEN <= ASCII[3]) ) ) else c for c in self.string])))
        
    def decodeOrdinal(self):
        '''Decodes message using ordinals, with the ugliest possible list comprehension.

        Returns:
            str: Decoded message.

        '''
        return('Decoded sentence: {}'.format(''.join([chr(ord(c)-self.shift) if ( (c.isupper() and (ord(c)-self.shift >= ASCII[0] and ord(c)-self.shift <= ASCII[1]) ) or (c.islower() and (ord(c)-self.shift >= ASCII[2] and ord(c)-self.shift <= ASCII[3]) ) ) else chr(ord(c)-self.shift+ALPHABET_LEN) if ( (c.isupper() and (ord(c)-self.shift+ALPHABET_LEN >= ASCII[0] and ord(c)-self.shift+ALPHABET_LEN <= ASCII[1]) ) or (c.islower() and (ord(c)-self.shift+ALPHABET_LEN >= ASCII[2] and ord(c)-self.shift+ALPHABET_LEN <= ASCII[3]) ) ) else c for c in self.string])))
        
parser = argparse.ArgumentParser(description='Caesar cipher encoder/decoder.')
parser.add_argument('conversion', help = "Choose to 'encode' or 'decode' the string", type = str)
parser.add_argument('shift', help = 'Perform encoding/decoding by a given shift', type = int)
parser.add_argument('-f', '--file', help = 'Specify filepath of file to be encoded/decoded', type = str)
parser.add_argument('-t', '--text', help = 'Specify a string to be encoded/decoded', type = str)

args = parser.parse_args()

encodeFlag = False
decodeFlag = False

if args.conversion == 'encode':
    encodeFlag = True
elif args.conversion == 'decode':
    decodeFlag = True
else:
    parser.error("Enter 'encode' or 'decode' for the conversion argument")

shift = args.shift

if args.file:
    if args.text:
        parser.error('Cannot select both arguments -f/--file, -t/--text')
    if os.path.isfile(args.file):
        theFile = open(os.path.join(__location__,args.file), 'r')
        string = ''.join([line for line in theFile])
        theFile.close()
    else:
        parser.error('Could not locate file!')
        
elif args.text:
    if args.file:
        parser.error('Cannot select both arguments -f/--file, -t/--text')
    string = args.text
    
else:
    string = input('Please enter a sentence: ')

if ALPHABET_LEN < shift:
    shift = shift % ALPHABET_LEN
    
message = String(string, shift)

print('Original message: {}'.format(string))

if encodeFlag:
    print(message.encodeHashTable())
    if message.encodeHashTable() == message.encodeOrdinal():
        print ('Success!')
    else:
        print('Awww :(')
if decodeFlag:
    print(message.encodeHashTable())
    if message.decodeHashTable() == message.decodeOrdinal():
        print ('Success!')
    else:
        print('Awww :(')


