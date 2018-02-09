print("Which word would you like to encode?")
word = str(input())

listedword = list(word)

encodednumber = []
decodednumber = []
newword = []

for letter in listedword:
    originalorder = ord(letter)
    decodednumber.append(originalorder)

    neworder = originalorder + 3
    if neworder > 121 and originalorder >= 96:
        neworder -= 26
        encodednumber.append((neworder))
    elif neworder > 90 and originalorder >= 65 and neworder < 95:
        neworder -= 26
        encodednumber.append(neworder)
    else:
        encodednumber.append(neworder)

for number in encodednumber:
    neworder = chr(number)
    newword.append(neworder)

newword1= ''.join(newword)

print("Your word", word, "is encoded into", newword1)