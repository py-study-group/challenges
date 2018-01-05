from tkinter import *
import morse


morse_code = {
        'A': '.-',     'B': '-...',   'C': '-.-.',
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
     	'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',

        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.' , " ": '/', ',': '--..--',
        '.': '·-·-·-', ';': '-·-·-·', ':': '---···',
        "!": '-·-·--', "?": "··--··", "&": '·-···',
        "@": '·--·-·'
}

def encode_morse(input_str):

    encoded_message = ""
    raw_code = input_str.split(" ")
    for raw_element in raw_code:
        for symbol, code in morse_code.items():
            if raw_element == code:
                if len(encoded_message) == 0 or encoded_message[-1] == " ":
                    encoded_message += symbol
                else:
                    encoded_message += symbol.lower()
    return(encoded_message)

def code_morse(input_str):

    coded_message = ""

    for raw_symbol in input_str:
        coded_message += morse_code[raw_symbol.upper()] + " "

    return(coded_message)


root = Tk()



def decode(event):
    label_decode["text"] = encode_morse(entry_decode.get())

def code_input(event):
    label_code['text'] = code_morse(entry_code.get())

entry_decode = Entry(root,width = 50)
entry_decode.pack()

button = Button(root, text="Decode")
button.bind("<Button-1>", decode)
button.pack()

label_decode = Label(root,text=entry_decode.get(),height=5, width=50)
label_decode.pack()

entry_code = Entry(root, width=50)
entry_code.pack()

button2 = Button(root, text="Code")
button2.bind("<Button-1>", code_input)
button2.pack()

label_code = Label(root, text="",height=5, width=50)
label_code.pack()

root.mainloop()
