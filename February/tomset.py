
import argparse
import sys

letters = 'abcdefghijklmnopqrstuvwxyz'


def convert(mode, text, shift):
	"""
	Method to convert characters based on provided cipher
	:param mode: 'encode' or 'decode'
	:param text: text to be encoded/decoded - either provided by user or parsed from given file
	:param shift: Offset (integer) used to shift characters in the 'letters' string
	:return: Encoded or decoded text
	"""
	new_text = ''
	for char in text.lower():
		if char == ' ':
			new_char = ' '
			new_text += new_char
			continue
		try:
			i = letters.index(char)
		except ValueError:
			if char == '\n':
				continue
			else:
				print('Only letters(a-z) accepted, try again')
				sys.exit()
		if mode == 'encode':
			n = (i + shift) % 26
			new_char = letters[n]
			new_text += new_char
		elif mode == 'decode':
			n = i - (shift % 26)
			new_char = letters[n]
			new_text += new_char
	return new_text


def main():
	"""
	Parses command line arguments to determine text location (text or file), shift offset, and encode/decode option.
	Main then calls the 'Convert' method to encode or decode text and prints the result to console.
	"""
	parser = argparse.ArgumentParser()
	parser.add_argument(
		"-s", "--shift", help="character offset (integer) to implement while encoding/decoding", required=True,
		type=int)
	parser.add_argument(
		"-m", "--mode", choices=['encode', 'decode'], help="options: 'encode' or 'decode' the message", required=True,
		type=str)
	parser.add_argument(
		"-d", "--decode", help="specifies that the characters from file or text will be decoded")
	parser.add_argument(
		"-t", "--text", help="text to encode/decode is supplied")
	parser.add_argument(
		"-f", "--file", help="path to file for encoding/decoding is supplied")
	args = parser.parse_args()
	text = args.text
	file = args.file
	mode = args.mode
	shift = args.shift

	if not text and not file:
		format_input = input(f"{mode} from text or file? Enter 'text' or 'file': ".format(mode))
		if format_input == 'text':
			text = input(f"Enter 'text' to {mode}: ".format(mode))
		elif format_input == 'file':
			file = input(f"Enter filename to {mode}: ".format(mode))

	if text:
		new_text = convert(mode, text, shift)
		print(f'Text {mode}d: '.format(mode), new_text)

	elif file:
		with open(file, 'r') as f:
			text = f.readlines()
			for line in text:
				new_text = convert(mode, line, shift)
				print(f'Text {mode}d: '.format(mode), new_text)

if __name__ == '__main__':
	main()









