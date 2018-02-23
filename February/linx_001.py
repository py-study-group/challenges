import os
import string
import argparse

new_message = []
lower_letters = list(string.ascii_lowercase)
upper_letters = list(string.ascii_uppercase)

def Caesar_encode(number, message):
	for l in message:
		if l not in lower_letters and l not in upper_letters:
			new_message.append(l)
		elif l in upper_letters:
			if upper_letters.index(l) + number > 25:
				new_message.append(upper_letters[upper_letters.index(l) + number - 26])
			else:
				new_message.append(upper_letters[upper_letters.index(l) + number])
		elif l in lower_letters:
			if lower_letters.index(l) + number > 25:
				new_message.append(lower_letters[lower_letters.index(l) + number - 26])
			else:
				new_message.append(lower_letters[lower_letters.index(l) + number])


def Caesar_decode(number, message):
	for l in message:
		if l not in lower_letters and l not in upper_letters:
			new_message.append(l)
		elif l in upper_letters:
			if upper_letters.index(l) - number < 0:
				new_message.append(upper_letters[upper_letters.index(l) - number + 26])
			else:
				new_message.append(upper_letters[upper_letters.index(l) - number])
		elif l in lower_letters:
			if lower_letters.index(l) - number < 0:
				new_message.append(lower_letters[lower_letters.index(l) - number + 26])
			else:
				new_message.append(lower_letters[lower_letters.index(l) - number])

def Encrypt_file(number, message):
	outf = open('encrypted.txt', 'a')
	with open(message, 'r') as inf:
		for line in inf:
			Caesar_encode(number, line)
		outf.write(''.join(new_message))

def Decrypt_file(number, message):
	outf = open('decrypted.txt', 'a')
	with open(message, 'r') as inf:
		for line in inf:
			Caesar_decode(number, line)
		outf.write(''.join(new_message))

def auto_file_d(number, message):
	words = open('english_words.txt').readlines()
	outf = open('decrypted.txt', 'a')

	with open(message, 'r') as inf:
		for line in inf:
			outf.write(auto_decode(number, line))

def auto_decode(number, message):
	words = open('english_words.txt').readlines()
	while number < 26:
		del new_message[:]
		Caesar_decode(number, message)
		decoded_string = ''.join(new_message)
		decoded_list = decoded_string.split()

		for l in words:
			if l == decoded_list[0].lower() + '\n':
				print('Shift number is: %s' % number)
				return decoded_string
		number += 1

def Main():
	parser = argparse.ArgumentParser(description="""This is a caesar cipher encrypter/decrypter. 
		If no shift number is given, it will default to 13 (rot13).""")

	parser.add_argument("Message", help="Enter the message you want to encrypt or decrypt within 'quotes'.")
	parser.add_argument("-s", "--Shift_number", type=int, default=13, help="Number of letters to shift to the right.")
	parser.add_argument("-a", "--auto", help="Automatically find the shift number to decode he message.", action="store_true")
	parser.add_argument("-e", "--encrypt", help="Encrypt the Caesar cypher.", action="store_true")
	parser.add_argument("-d", "--decrypt", help="Decrypt the Caesar cypher.", action="store_true")
	parser.add_argument("-fa", "--auto_file", help="Auto decrypts a file and will put the output in a file called encrypted.txt", action="store_true")
	parser.add_argument("-fe", "--file_Encrypt", help="Encrypts a file and will create a new file called encrypted.txt.", action="store_true")
	parser.add_argument("-fd", "--file_Decrypt", help="Decrypts a file and will create a new file called decrypted.txt.", action="store_true")

	args = parser.parse_args()

	if args.encrypt:
		Caesar_encode(args.Shift_number, args.Message)
		print(''.join(new_message))
	elif args.decrypt:
		Caesar_decode(args.Shift_number, args.Message)
		print(''.join(new_message))
	elif args.auto:
		print(auto_decode(1, args.Message))
	elif args.file_Encrypt:
		if os.path.exists(args.Message):
			Encrypt_file(args.Shift_number, args.Message)
		else:
			print("\n  File not found.\n")
	elif args.file_Decrypt:
		if os.path.exists(args.Message):
			Decrypt_file(args.Shift_number, args.Message)
	elif args.auto_file:
		if os.path.exists(args.Message):
			auto_file_d(1, args.Message)


if __name__ == "__main__":
	Main()

