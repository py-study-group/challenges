import sys

morse_dict={"A": ".-",
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

def encode(string):
    string=string.upper()
    print(string)
    out=""
    for char in string:
        print(char)
        if char!=" ":
            out+=morse_dict[char]
            out+=' '
        else:
            out+=' '
    return out

def decode(string):
    out=""
    l=string.split()
    for word in l:
        out+=list(morse_dict.keys())[list(morse_dict.values()).index(word)]
        out+=' '
    return out

def main():
    out=""
    print("press 1 to code to morse\n Press 2 to decode a morse code\n")
    inp=int(input())
    print("Enter the string")
    string=input()
    if inp==1:
        print(encode(string))
    elif inp==2:
        print(decode(string))

if __name__ == '__main__':
    main()