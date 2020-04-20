from string import ascii_lowercase as low
from string import ascii_uppercase as up


def enc_or_dec_caesar(old_text, new_file, namespace):
    for i in range(len(namespace.key)):
        if namespace.key[i].isalpha():
            print("It's a mistake, sorry. Try to write a number.")
            return

    if namespace.command == 'decrypt':
        namespace.command = 'encrypt'
        namespace.key = str(26 - int(namespace.key) % 26)
        enc_or_dec_caesar(old_text, new_file, namespace)
    else:
        for i in range(len(old_text)):
            if not old_text[i].isalpha():
                new_file.write(old_text[i])
                continue
            if old_text[i].upper() == old_text[i]:
                new_file.write(up[(up.index(old_text[i])
                                   + int(namespace.key)) % len(up)])
            else:
                new_file.write(low[(low.index(old_text[i])
                                   + int(namespace.key)) % len(low)])


def enc_or_dec_vizhener(old_text, new_file, namespace):
    if namespace.command == 'decrypt':
        namespace.command = 'encrypt'
        new_key = ""
        for i in range(len(namespace.key)):
            if not namespace.key[i].isalpha():
                print("It's a mistake, sorry. Try to write a word.")
                return
            elif namespace.key[i].lower() == namespace.key[i]:
                new_key += low[(len(low) - low.index(namespace.key[i])) % len(up)]
            else:
                new_key += up[(len(up) - up.index(namespace.key[i])) % len(low)]

        namespace.key = new_key
        enc_or_dec_vizhener(old_text, new_file, namespace)
    else:
        key_index = 0
        key = namespace.key
        for i in range(len(old_text)):
            if not old_text[i].isalpha():
                new_file.write(old_text[i])
                continue
            if old_text[i].upper() == old_text[i]:
                if key[key_index].lower() == key[key_index]:
                    new_file.write(up[(up.index(old_text[i])
                                        + low.index(key[key_index])) % len(up)])
                else:
                    new_file.write(up[(up.index(old_text[i])
                                        + up.index(key[key_index])) % len(up)])
            else:
                if key[key_index].lower() == key[key_index]:
                    new_file.write(low[(low.index(old_text[i])
                                        + low.index(key[key_index])) % len(low)])
                else:
                    new_file.write(low[(low.index(old_text[i])
                                        + up.index(key[key_index])) % len(low)])
            key_index += 1
            if key_index == len(namespace.key):
                key_index = 0


def enc_or_dec_vernam(old_text, new_file, namespace):
    enc_or_dec_vizhener(old_text, new_file, namespace)