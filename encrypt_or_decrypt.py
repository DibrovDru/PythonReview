from string import ascii_lowercase as low
from string import ascii_uppercase as up


def enc_or_dec_caesar(old_text, new_file, namespace):
    for i in range(len(namespace.key)):
        if namespace.key[i].isalpha():
            print("It's a mistake, sorry. Try to write a number.")
            return

    if namespace.command == 'decrypt':
        namespace.key = str(26 - int(namespace.key) % 26)

    for letter in old_text:
        if not letter.isalpha():
            new_file.write(letter)
            continue
        if letter.upper() == letter:
            new_file.write(up[(up.index(letter)
                               + int(namespace.key)) % len(up)])
        else:
            new_file.write(low[(low.index(letter)
                               + int(namespace.key)) % len(low)])


def enc_or_dec_vizhener(old_text, new_file, namespace):
    for symbol in namespace.key:
        if not symbol.isalpha():
            print("It's a mistake, sorry. Try to write a word.")
            return

    if namespace.command == 'decrypt':
        new_key = ""
        for letter in namespace.key:
            if letter.lower() == letter:
                new_key += low[(len(low) - low.index(letter)) % len(up)]
            else:
                new_key += up[(len(up) - up.index(letter)) % len(low)]

        namespace.key = new_key

    key_index = 0
    key = namespace.key
    for letter in old_text:
        if not letter.isalpha():
            new_file.write(letter)
            continue
        if letter.upper() == letter:
            if key[key_index].lower() == key[key_index]:
                new_file.write(up[(up.index(letter)
                                   + low.index(key[key_index])) % len(up)])
            else:
                new_file.write(up[(up.index(letter)
                                   + up.index(key[key_index])) % len(up)])
        else:
            if key[key_index].lower() == key[key_index]:
                new_file.write(low[(low.index(letter)
                                    + low.index(key[key_index])) % len(low)])
            else:
                new_file.write(low[(low.index(letter)
                                    + up.index(key[key_index])) % len(low)])
        key_index += 1
        if key_index == len(namespace.key):
            key_index = 0


def enc_or_dec_vernam(old_text, new_file, namespace):
    enc_or_dec_vizhener(old_text, new_file, namespace)
