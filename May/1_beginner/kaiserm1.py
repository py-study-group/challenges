""" Translates a string into Morse Code.
    Start program without command line argument to be prompted for a string to be translated.
    Translation will be displayed in the console.
    Start program with input file and output file as command line arguments.
    Text from input file will be translated and translation stored in output file.
    
    by Martin Kaiser, 2017-05-03
"""

import re
import sys

# Morse Code from https://en.wikipedia.org/wiki/Morse_code.
MORSE_ALPHABET = {"A": ".-",
                  "B": "-...",
                  "C": "-.-.",
                  "D": "-..",
                  "E": ".",
                  "F": "..-.",
                  "G": "--.",
                  "H": "....",
                  "I": "..",
                  "J": ".---",
                  "K": "-.-",
                  "L": ".-..",
                  "M": "--",
                  "N": "-.",
                  "O": "---",
                  "P": ".--.",
                  "Q": "--.-",
                  "R": ".-.",
                  "S": "...",
                  "T": "-",
                  "U": "..-",
                  "V": "...-",
                  "W": ".--",
                  "X": "-..-",
                  "Y": "-.--",
                  "Z": "--..",
                  "0": "-----",
                  "1": ".----",
                  "2": "..---",
                  "3": "...--",
                  "4": "....-",
                  "5": ".....",
                  "6": "-....",
                  "7": "--...",
                  "8": "---..",
                  "9": "----.",
                  ".": ".-.-.-",
                  ",": "--..--",
                  "?": "..--..",
                  "'": ".----.",
                  "!": "-.-.--",
                  "/": "-..-.",
                  "(": "-.--.",
                  ")": "-.--.-",
                  "&": ".-...",
                  ":": "---...",
                  ";": "-.-.-.",
                  "=": "-..-",
                  "+": ".-.-.",
                  "-": "-....-",
                  "_": "..--.-",
                  '"': ".-..-.",
                  "$": "...-..-",
                  "@": ".--.-."}


def main(args):
    # If no command line arguments are given, ask user for string input, then output translation to console.
    if len(args) == 1:
        user_string = [input("Enter a string: ")]  # Put string in a list to use with translate_to_morse function.
        print(translate_to_morse(user_string))

    # If input file and output file have been specified, read input file, translate and save to output file.
    elif len(sys.argv) == 3:
        infile = str(args[1])
        outfile = str(args[2])
        try:
            with open(infile, "r") as inf:
                in_text = inf.readlines()
        # If input file cannot be found, return 2.
        except IOError:
            print("{} not found!".format(infile))
            return 2

        out_text = translate_to_morse(in_text)
        # If there is an invalid character in the input text, return 4.
        if "invalid character" in out_text:
            print(out_text)
            return 4
        # Else write translation to output file.
        else:
            try:
                with open(outfile, "w") as ouf:
                    ouf.write(out_text)
                print("Translation is stored in {}.".format(outfile))
                return 0
            # If translation cannot be written to output file, return 3.
            except IOError:
                print("Could not write to {}".format(outfile))
                return 3

    # If wrong number of command line arguments were given, show correct usage in console, then return 1.
    else:
        print("correct usage:")
        print("./{}".format(args[0]))
        print("or")
        print("./{} [input_file] [output_file]".format(args[0]))
        return 1


def translate_to_morse(in_text):
    """ Translate a string to morse code
        :text: list of strings
        :returns string
    """
    out_text = []
    for line in in_text:
        out_line = []
        for word in re.split('\S|\\\\n', line.rstrip()):  # input() escapes \n to \\n, so \\\\n to escape \\ in regex.
            out_word = []
            for char in word.upper():
                try:
                    out_word.append(MORSE_ALPHABET[char])
                # If a character in the text is not in the Morse Code Alphabet, return error message.
                except KeyError:
                    return "invalid character: '{}'".format(char)
            # Separate single characters with spaces ' '.
            out_word_string = " ".join(out_word)
            out_line.append(out_word_string)
        # Separate words with slashes ' / '.
        out_line_string = " / ".join(out_line)
        out_text.append(out_line_string)
    # Return whole translation as a single string.
    return " / ".join(out_text)  # Separate lines with slashes as well ' / '.


# Tests:
assert translate_to_morse([""]) == ""
assert translate_to_morse([" "]) == ""
assert translate_to_morse(["Hello, World"]) == ".... . .-.. .-.. --- --..-- / .-- --- .-. .-.. -.."
assert translate_to_morse(["Hello, World\nHello, World"]) == (".... . .-.. .-.. --- --..-- / .-- --- .-. .-.. -.. / "
                                                              ".... . .-.. .-.. --- --..-- / .-- --- .-. .-.. -..")
assert translate_to_morse(["###"]) == "invalid character: '#'"  # test for invalid character catching
assert translate_to_morse(["test\\ntest"]) == "- . ... - / - . ... -"  # test for \n in user input


if __name__ == "__main__":
    main(sys.argv)
