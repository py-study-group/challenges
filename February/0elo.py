#!/usr/bin/python

'''
February challenge from py-study-group/challenges:
Caesar cipher encoder/decoder (Advanced)

Link: https://github.com/py-study-group/challenges/tree/master/February

'''

import argparse, os
from pathlib import Path
from langdetect import detect
from polyglot.text import Text

#__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

__location__ = Path.cwd()

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
ALPHABET_LEN = 26
ASCII = [65, 90, 97, 122]
COMMON_LETTERS = 'etaoinsrhldcumfpgwybvkxjqz'

class Cipher:
    '''Represents the message to be encoded/decoded.
    This class is used to encode and decode messages.

    Attributes:
        string (str): The message to be encoded/decoded.
        shift  (int): The amount to shift the message by.

    '''
    
    def __init__(self, string, shift = None):
        '''This is the __init__ method.

        Args:
            string (str): The message to be encoded/decoded.
            shift (int, optional): The amount to shift the message by.

        '''
        self.string = string
        if shift == None:
            self.shift = 0
        else:
            self.shift = shift
        self.encoded = ''
        self.decoded = ''

    def printEncodedHash(self):
        print(self.encodeHashTable())
        
    def printDecodedHash(self):
        print(self.decodeHashTable())

    def cleanString(self, string):
        cleaned = ''.join([i for i in string.lower() if i.isalpha()])
        return cleaned

    def detectEnglish(self, string):
        '''
        Current solution to detect if string is English
        is to check against both langdetect and polyglot.
        Longer sentences are split by every ten words and
        verified via polyglot a second time.
        Will make solution more robust (if necessary)
        following extensive testing.
        '''
        text = Text(string)
        if detect(string) == 'en' and text.language.code == 'en':
            textSplit = text.split(' ')
            words = []
            temp = []
            counter = 0
            modNum = 10
            remaining = 0
            
            for idx, i in enumerate(textSplit):
                temp.append(i)
                remaining += 1
                if ((idx+1) % modNum) == 0:
                    words.append(temp)
                    remaining = 0
                    temp = []
            if temp:
                if remaining < (modNum/2):
                    words[-1].extend(temp)
                else:
                    words.append(temp)

            for group in words:
                if Text(' '.join(group)).language.code != 'en':
                    return False
            return True
        return False

    def printPrediction(self):
        guess, original, decoded = self.detectByFrequency()
        
        print('\nOriginal string:\n{}'.format(original))
        print('\nPredicted shift of: {}'.format(guess))
        print('\nDecoded string:\n{}\n'.format(decoded))
    
    def detectByFrequency(self):

        if self.detectEnglish(self.string):
            return(0,self.string,self.string)
        temp = self.string
        cleaned = self.cleanString(temp)
        letters = dict.fromkeys(cleaned, 0)
        for letter in self.string.lower():
            if letter in letters:
                letters[letter] += 1

        swapList = sorted(letters.items(), reverse=True)
        swapList = swapList[:7]
        for swap in COMMON_LETTERS:
            for pair in swapList:
                swapee = pair[0]
                if ord(swapee) > ord(swap):
                    guess = 26 - (ord(swapee) - ord(swap))
                else:
                    guess = (ord(swap)-ord(swapee))
                    
                guessValues = ALPHABET[-guess:] + ALPHABET[:-guess]
                decodeMap = dict(zip(ALPHABET, guessValues))

                decoded = ''.join([decodeMap[i.lower()].upper() if i.lower() in decodeMap and i.isupper() else decodeMap[i] if i in decodeMap else i for i in self.string])
                if self.detectEnglish(decoded):
                    return(guess,self.string,decoded)

        return(0,self.string,'Could not determine')
        
    def encodeHashTable(self):
        '''Encodes message using a hash table implementation.
        
        Returns:
            str: Encoded message.

        '''
        encodedValues = ALPHABET[self.shift:] + ALPHABET[:self.shift]
        encodeMap = dict(zip(ALPHABET, encodedValues))
        self.encoded = ''.join([encodeMap[c] if c.islower() else encodeMap[c.lower()].upper() if c.lower() in encodeMap else c for c in self.string])
        return('Encoded string:\n{}\n'.format(self.encoded))

    def decodeHashTable(self):
        '''Decodes message using a hash table implementation.

        Returns:
            str: Decoded message.

         '''
        decodedValues = ALPHABET[-self.shift:] + ALPHABET[:-self.shift]
        decodeMap = dict(zip(ALPHABET, decodedValues))
        self.decoded = ''.join([decodeMap[c] if c.islower() else decodeMap[c.lower()].upper() if c.lower() in decodeMap else c for c in self.string])
        return('Decoded string:\n{}\n'.format(self.decoded))
    
    def encodeOrdinal(self):
        '''Encodes message using ordinals, with the ugliest possible list comprehension.

        Returns:
            str: Encoded message.

        '''
        return('Encoded sentence:\n{}\n'.format(''.join([chr(ord(c)+self.shift) if ( (c.isupper() and (ord(c)+self.shift >= ASCII[0] and ord(c)+self.shift <= ASCII[1]) ) or (c.islower() and (ord(c)+self.shift >= ASCII[2] and ord(c)+self.shift <= ASCII[3]) ) ) else chr(ord(c)+self.shift-ALPHABET_LEN) if ( (c.isupper() and (ord(c)+self.shift-ALPHABET_LEN >= ASCII[0] and ord(c)+self.shift-ALPHABET_LEN <= ASCII[1]) ) or (c.islower() and (ord(c)+self.shift-ALPHABET_LEN >= ASCII[2] and ord(c)+self.shift-ALPHABET_LEN <= ASCII[3]) ) ) else c for c in self.string])))
        
    def decodeOrdinal(self):
        '''Decodes message using ordinals, with the ugliest possible list comprehension.

        Returns:
            str: Decoded message.

        '''
        return('Decoded sentence:\n{}\n'.format(''.join([chr(ord(c)-self.shift) if ( (c.isupper() and (ord(c)-self.shift >= ASCII[0] and ord(c)-self.shift <= ASCII[1]) ) or (c.islower() and (ord(c)-self.shift >= ASCII[2] and ord(c)-self.shift <= ASCII[3]) ) ) else chr(ord(c)-self.shift+ALPHABET_LEN) if ( (c.isupper() and (ord(c)-self.shift+ALPHABET_LEN >= ASCII[0] and ord(c)-self.shift+ALPHABET_LEN <= ASCII[1]) ) or (c.islower() and (ord(c)-self.shift+ALPHABET_LEN >= ASCII[2] and ord(c)-self.shift+ALPHABET_LEN <= ASCII[3]) ) ) else c for c in self.string])))


class handleArgs:

    def __init__(self):
        self.encodeFlag = False
        self.decodeFlag = False
        self.handleDetect = False
        self.handleFile = False
        self.handleText = False
        self.shift = 0
        self.string = ''
        self.conversion = ''
            
    def getShift(self):
        return self.shift

    def getString(self):
        return self.string

    def printString(self):
        return 'Original message: {}'.format(self.string)
        
    def getArgs(self):
        
        parser = argparse.ArgumentParser(description='Caesar cipher encoder/decoder.')

        subparser = parser.add_subparsers(dest='selection',help = 'commands')
        subparser.required = True
        # Detect Command
        detect_command = subparser.add_parser('detect', help='Detect shift of an encoded string')
        detect_command.add_argument('d_file', action='store', help='File to be decoded')

        # File Command
        file_command = subparser.add_parser('file', help='File to be encoded or decoded')
        file_command.add_argument('f_conversion', action='store', help="Choose to 'encode' or 'decode' the string", type=str)
        file_command.add_argument('f_shift', action='store', help='Shift the string by this amount', type=int)
        file_command.add_argument('thefile', action='store', help='File containing string to be encoded or decoded', type=str)
        
        # Text Command
        text_command = subparser.add_parser('text', help='String to be encoded or decoded')
        text_command.add_argument('t_conversion', action='store', help="Choose to 'encode' or 'decode' the string", type=str)
        text_command.add_argument('t_shift', action='store', help='Shift the string by this amount', type=int)
        text_command.add_argument('thetext', action='store', help='Text to be encoded or decoded', type=str)
        
        args = vars(parser.parse_args())
        #print(args)
        
        if 'd_file' in args:
            self.handleDetect = True
        elif 'f_conversion' in args:
            self.conversion = args['f_conversion']
            self.handleFile = True
            self.shift = args['f_shift']
        elif 't_conversion' in args:
            self.conversion = args['t_conversion']
            self.handleText = True
            self.shift = args['t_shift']

        if self.handleFile:
#            if os.path.isfile(args['thefile']):
            if Path(args['thefile']).is_file():
                theFile = open(Path(__location__ / args['thefile']), 'r')
                self.string = ''.join([line for line in theFile])
                theFile.close()
            else:
                parser.error('Could not locate file!')
                
        elif self.handleText:
            self.string = args['thetext']

        elif self.handleDetect:
            if Path(args['d_file']).is_file():
                theFile = open(Path(__location__ / args['d_file']), 'r')
                self.string = ''.join([line for line in theFile])
                theFile.close()

            else:
                parser.error('Could not locate file!')
            self.conversion = 'decode'
        else:
            self.string = input('Please enter a sentence: ')
            conversionType = input('Encode or decode: ')
            while conversionType != 'encode' or conversionType != 'decode':
                conversionType = input('Encode or decode: ')
            self.conversion = conversionType
            shiftNum = input('Please enter a shift amount: ')
            while not shiftNum.isdigit():
                shiftNum = input('Please enter a shift amount: ')
            self.shift = shiftNum

        if self.conversion == 'encode':
            self.encodeFlag = True
        elif self.conversion =='decode':
            self.decodeFlag = True
        else:
            parser.error("Enter 'encode' or 'decode' for the conversion argument!")
        if ALPHABET_LEN < self.shift:
            self.shift = self.shift % ALPHABET_LEN

            
if __name__ == '__main__':
    print('\n{}\nC A E S A R   C I P H E R\n{}\n'.format('*'*24,'*'*24))
    
    args = handleArgs()
    args.getArgs()
    message = Cipher(args.getString(), args.getShift())
    
    if args.handleDetect:
        message.printPrediction()
    else:
        if args.encodeFlag:
            message.printEncodedHash()
        else:
            message.printDecodedHash()
