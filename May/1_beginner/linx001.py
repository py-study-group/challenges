import argparse
import os.path

morse_code = {
	'A':'.-',    'B':'-...',  'C':'-.-.',
	'D':'-..',  'E':'.', 	  'F':'..-.',
	'G':'--.',   'H':'....',  'I':'..',
	'J':'.---',  'K':'-.-',   'L':'.-..',
	'M':'--',    'N':'-.',    'O':'---',
	'P':'.--.',  'Q':'--.-',  'R':'.-.',
	'S':'...',   'T':'-',     'U':'..-',
	'V':'...-',  'W':'.--',   'X':'-..-',
	'Y':'-.--',  'Z':'--..',  '0':'-----',
	'1':'.----', '2':'..---', '3':'...--',
	'4':'....-', '5':'.....', '6':'-....',
	'7':'--...', '8':'---..', '9':'----.',
	'.':'.-.-.-', ',':'--..--', '?':'..--..',
	'/':'-..-.', '@':'.--.-.', '!':'-.-.--',
	'&':'.-...', ';':'-.-.-.'
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

def Message_Converter(message):
	new_message= []
	for letter in message:
		if letter.upper() in morse_code:
			new_message.append(morse_code[letter.upper()])
		else:
			pass
	print(' '.join(new_message))

def Message_Decrypter(message):
	encrypted = message.split()
	decrypted_message = []
	for i in encrypted:
		decrypted_letter = letter_converter(i)
		decrypted_message.append(decrypted_letter)

	print(''.join(decrypted_message))

#Had to decode the morse code in two different fucntions since
#doing it in one would print out the letters in alphabetical order.
def letter_converter(code):
	for letter, morse in morse_code.items():
		if code == morse:
			return letter
		else:
			pass

def Main():
	parser = argparse.ArgumentParser()

	parser.add_argument("Message", help="Enter a single world, or a message within 'quotes' to convert to morse code")
	parser.add_argument("-F", "--Filename", help='Enter a file name to convert the text to morse code.', action="store_true")
	parser.add_argument("-D", "--Decrypt", help="Enter morese code within 'quotes' to decrypt to plain text.", action="store_true")

	args = parser.parse_args()


	if args.Decrypt:
			Message_Decrypter(args.Message)
	elif args.Filename:
		if os.path.exists(args.Message):
			File_Converter(args.Message)
		else:
			print("\nFile '%s' does not exitst!\n") % args.Message
	else:
		Message_Converter(args.Message)

if __name__ == '__main__':
	Main()
