#!/usr/bin/env python3

"""Morse code translator.
Translate text from interactive input, 
piped input, or from a file.
"""

import argparse
import readline

_values = {
    ' ': '|',
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',
    '\n': '\n\b',
}


def translate(text):
    """Translate text to morse"""
    assert type(text) is str, "Input must be a string"
    result = ' '.join(_values.get(s.upper(), f'#{s}') for s in text)
    return result


def main():
    # Support Command line arguments and define flags
    parser = argparse.ArgumentParser(description='Translate text into morse code')
    parser.add_argument('string', metavar='S', nargs='*')
    parser.add_argument('-f', '--file', dest='file', help="Give file to be translated")
    args = parser.parse_args()

    if args.string:
        # Multiple words in the command line are imported as a list
        # so we will merge all of those words into a single string.
        text = ' '.join(args.string)
    elif args.file:
        # Read in file
        with open(args.file, 'r') as text_file:
            text = text_file.read()
    else:
        # Read from interactive or piped text input
        print("Type ctrl-D to submit text")
        lines = []
        while True:
            try:
                line = input()
            # Reading from piped text will raise EOFError
            # so we will handle that gracefully.
            except EOFError:
                break
            lines.append(line)
        text = '\n'.join(lines)

    print(translate(text))

if __name__ == "__main__":
    main()
