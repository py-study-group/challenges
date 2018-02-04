import argparse

def caesar_cipher(mode, message, key):
    """
    function to encode/decode caesar cipher
    if decode, negate the key
    """
    if key>26:
        key = key % 26
    if mode == 'd':
        key = -key

    output = ''

    for i in message:
        if i.isalpha():
            num = ord(i)
            num+=key

            if i.isupper():
                if num > ord('Z'):
                    num = num - 26
                elif num < ord('A'):
                    num = num + 26
            elif i.islower():
                if num > ord('z'):
                    num = num - 26
                elif num < ord('a'):
                    num = num + 26
            output += chr(num)
        else:
            output += i

    return output

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('action', help='encode/decode')
    parser.add_argument('shift', help='the amount of shift to be applied')
    parser.add_argument('-f','--file', help='file to be opened')
    parser.add_argument('-t','--text', help='text to be encoded/decoded')
    args = parser.parse_args()

    if args.action == 'encode':
        if args.file:
            try:
                with open(args.file,'r') as file_obj:
                    print(caesar_cipher('e', file_obj.read(), int(args.shift)))
            except FileNotFoundError:
                print('File not found.')
        elif args.text:
            print(caesar_cipher('e', args.text, int(args.shift)))
        else:
            text = input('Enter the string to be encoded: ')
            print(caesar_cipher('e', text, int(args.shift)))
        
    elif args.action == 'decode':
        if args.file:
            try:
                with open(args.file,'r') as file_obj:
                    print(caesar_cipher('d', file_obj.read(), int(args.shift)))
            except FileNotFoundError:
                print('File not found.')
        elif args.text:
            print(caesar_cipher('d', args.text, int(args.shift)))
        else:
            text = input('Enter the string to be decoded: ')
            print(caesar_cipher('d', text, int(args.shift)))

if __name__ == '__main__':
    main()
