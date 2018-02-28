print("Which word would you like to decode?")
codedword = str(input())

listedcodedword = list(codedword)

encodednumber = []
decodednumber = []
decodedword = []

for letter in listedcodedword:
    neworder = ord(letter)
    encodednumber.append(neworder)

    originalorder = neworder - 3
    if neworder >= 97 and originalorder <= 96:
        originalorder += 26
        decodednumber.append((originalorder))
    elif originalorder <= 64 and neworder <= 93:
        originalorder += 26
        decodednumber.append(originalorder)
    else:
        decodednumber.append(originalorder)

for number in decodednumber:
    originalorder = chr(number)
    decodedword.append(originalorder)

decodedwordjoined= ''.join(decodedword)

print("Your word", codedword, "is encoded into", decodedwordjoined)