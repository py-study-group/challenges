import argparse
import os.path

morse_code = {
	'A':'.-',    'B':'-...',  'C':'-.-.',
	'D':'-...',  'E':'.', 	  'F':'..-.',
	'G':'--.',   'H':'....',  'I':'..',
	'J':'.---',  'K':'-.-',   'L':'.-..',
	'M':'--',    'N':'-.',    'O':'---',
	'P':'.--.',  'Q':'--.-',  'R':'.-.',
	'S':'...',   'T':'-',     'U':'..-',
	'V':'...-',  'W':'.--',   'X':'-..-',
	'Y':'-.--',  'Z':'--..',  '0':'-----',
	'1':'.----', '2':'..---', '3':'...--',
	'4':'....-', '5':'.....', '6':'-....',
	'7':'--...', '8':'---..', '9':'----.'
}

def File_Converter(file):
	outf = open('Converted.txt', 'a')
	with open(file, 'r') as inf:
		for line in inf:
			for letter in line:
				if letter.upper() in morse_code:
					outf.write(morse_code[letter.upper()] + ' ')
				else:
					pass
	print("\nFile %s has been succesfully converted.\n" % file)

	outf.close()
	inf.close()


def Message_Converter(message):
	for letter in message:
		if letter.upper() in morse_code:
			print(morse_code[letter.upper()])
		else:
			pass

def Main():
	parser = argparse.ArgumentParser()

	parser.add_argument("Message", help='Enter a single world, or a message within "quotes" to convert to morse code')
	parser.add_argument("-F", "--Filename", help='Enter a file name to convert the text to morse code.', action="store_true")

	args = parser.parse_args()

	if args.Filename:
		if os.path.exists(args.Message):
			File_Converter(args.Message)
		else:
			print("This file does not exitst!")
	else:
		Message_Converter(args.Message)


if __name__ == '__main__':
	Main()












