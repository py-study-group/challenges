

# A script that encodes arbitrary text into Morse code.
# A bonus feature of the script is that it attempts
# to plays a short or long sound for each
# code symbol (hopefully cross-platform, but I only
# tested it on my Linux machine).
# Sounds are played using Python subprocess module call()
# which somehow doesn't want to let me do:
# print symbol - play sound, print symbol - play sound ...
# I wasn't able to solve this  so in the end
# The whole text is beeped, and only then printed in Morse code.
# After the script exits two wav files are left
# in the user's temp directory.

import os, sys, time
from tempfile import gettempdir
from subprocess import call


# Copied from kaiserm1's solution
MORSE_ALPHABET = {"A": ".-", "B": "-...", "C": "-.-.", "D": "-..",
                  "E": ".", "F": "..-.", "G": "--.", "H": "....",
                  "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
                  "M": "--", "N": "-.", "O": "---", "P": ".--.",
                  "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
                  "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
                  "Y": "-.--", "Z": "--..", "0": "-----", "1": ".----",
                  "2": "..---", "3": "...--", "4": "....-", "5": ".....",
                  "6": "-....", "7": "--...", "8": "---..", "9": "----.",
                  ".": ".-.-.-", ",": "--..--", "?": "..--..", "'": ".----.",
                  "!": "-.-.--", "/": "-..-.", "(": "-.--.", ")": "-.--.-",
                  "&": ".-...", ":": "---...", ";": "-.-.-.", "=": "-..-",
                  "+": ".-.-.", "-": "-....-", "_": "..--.-", '"': ".-..-.",
                  "$": "...-..-", "@": ".--.-."} 



# Credit for the audio:
#
# https://gist.github.com/juancarlospaco/c295f6965ed056dd08da
# I have no idea how this works.

WAVEFORM = (79, 45, 32, 50, 99, 113, 126, 127)

DOT_DURATION = 100 # milliseconds
DASH_DURATION = 300 # milliseconds

SYMBOL_DURATION = 0.02 # seconds
LETTER_DURATION = 0.06 # seconds
WORD_DURATION = 0.12 # seconds
GAP = time.sleep


# Generates the short beep sound
# and saves it to the temp directory
def dot(waveform=WAVEFORM):

    wavefile = os.path.join(gettempdir(), "dot.wav")

    file_exists = os.path.isfile(wavefile)
    accesible = os.access(wavefile, os.R_OK)
    
    if not file_exists or not os.access(wavefile, os.R_OK):
        with open(wavefile, "w+") as wave_file:
            for sample in range(0, DOT_DURATION, 1):
                for wav in range(0, 8, 1):
                    wave_file.write(chr(waveform[wav]))

    return wavefile


# Generates the long beep sound
# and saves it to the temp directory
def dash(waveform=WAVEFORM):

    wavefile = os.path.join(gettempdir(), "dash.wav")

    file_exists = os.path.isfile(wavefile)
    accesible = os.access(wavefile, os.R_OK)
    
    if not file_exists or not os.access(wavefile, os.R_OK):
        with open(wavefile, "w+") as wave_file:
            for sample in range(0, DASH_DURATION, 1):
                for wav in range(0, 8, 1):
                    wave_file.write(chr(waveform[wav]))

    return wavefile    


# Plays either the short or the long beep sound
# Hopefully cross platform, but I only tested it on Linux
def play(wavefile=None):
    
    if sys.platform.startswith("linux"):
        command = "chrt -i 0 aplay '{}' &>/dev/null"
        call(command.format(wavefile), shell=1)
    if sys.platform.startswith("darwin"):
        command = "afplay '{}' >/dev/null"
        call(command.format(wavefile), shell=True)
    if sys.platform.startswith("win"):
        command = "start /low /min '{}' > NUL" 
        call(command.format(wavefile), shell=1)


# Finds a letter in the code dictionary,
# prints its Morse code and plays a sound 
# for each dash and dot in the code.
def morse_encode_letter(letter):

    dot_file = dot()
    dash_file = dash()    

    code = MORSE_ALPHABET[letter]
    
    for symbol in code:
        print(symbol, end='')
        if symbol == '.':
            play(dot_file)
        else:
            play(dash_file)
        GAP(SYMBOL_DURATION)


# Splits the word into letters,
# encode each letter, prints a space
# after each letter and makes a small pause
# in the end.
def morse_encode_word(word):

    for letter in word.upper():
        morse_encode_letter(letter)
        print(' ', end='')
        GAP(LETTER_DURATION)


# Splits the text into words
# and encodes each word into morse code.
# After each word prints three spaces
# and makes a little bit longer pause.
def morse_encode_text(text):

    text = text.strip()
    for word in text.split():
        morse_encode_word(word)
        print('   ', end='')
        GAP(WORD_DURATION)

            

if __name__ in '__main__':


    text1 = 'SOS'
    text2 = 'Small is beautiful.'
    text3 = 'Life is wasted on the living.'

    print(text1)
    morse_encode_text(text1)
    print()

    print(text2)
    morse_encode_text(text2)
    print()

    print(text3)
    morse_encode_text(text3)
    print()
