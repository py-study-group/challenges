import string


# Lists of letters
lower_list = []
upper_list = []
new_message = []

# Alphabet
lower = string.ascii_lowercase
upper = string.ascii_uppercase

# Creating lists of letters
for letter in lower:
    lower_list.append(letter)
for letter in upper:
    upper_list.append(letter)

# Allow user to pick if they want to encode or decode
action = input("encode or decode?")

if action != "decode" and action != "encode":
    print("That is not a valid function.")

elif action == "encode":
    message = input("Type in the message that you want to encoded: ")
    for letter in message:
        if letter not in lower_list and letter not in upper_list and letter != " ":
            print("Your message contains characters that are not letters.")
            quit()
        if letter in lower_list:
            index = lower_list.index(letter)
            if index == 23:
                index = -3
            elif index == 24:
                index = -2
            elif index == 25:
                index = -1
            new_index = index + 3
            new_message.append(lower[new_index])

        if letter in upper_list:
            index = upper_list.index(letter)
            if index == 23:
                index = -3
            elif index == 24:
                index = -2
            elif index == 25:
                index = -1
            new_index = index + 3
            new_message.append(upper[new_index])

        if letter == " ":
            new_message.append(" ")

    sentence = "".join(new_message)
    print(sentence)


elif action == "decode":
    message = input("Type in the message that you want to decoded: ")
    for letter in message:
        if letter not in lower_list and letter not in upper_list and letter != " ":
            print("Your message contains characters that are not letters.")
            break
        if letter in lower_list:
            index = lower_list.index(letter)
            if index == 0:
                index = 26
            elif index == 1:
                index = 27
            elif index == 2:
                index = 28
            new_index = index - 3
            new_message.append(lower[new_index])

        if letter in upper_list:
            index = upper_list.index(letter)
            if index == 0:
                index = 26
            elif index == 1:
                index = 27
            elif index == 2:
                index = 28
            new_index = index - 3
            new_message.append(upper[new_index])

        if letter == " ":
            new_message.append(" ")