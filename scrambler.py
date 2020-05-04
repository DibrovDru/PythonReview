from encrypt_or_decrypt import enc_or_dec_caesar
from encrypt_or_decrypt import enc_or_dec_vizhener
from encrypt_or_decrypt import enc_or_dec_vernam
from hacker import hacker_func, hacker_learning
import argparse


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('way_old', type=argparse.FileType(mode='r'), nargs='?')
    parser.add_argument('way_new', type=argparse.FileType(mode='w'), nargs='?')
    parser.add_argument('command', choices=['encrypt', 'decrypt', 'broke'])
    parser.add_argument('cipher', nargs='?',
                        choices=['vizhener', 'caesar', 'vernam'])
    parser.add_argument('key', nargs='?')
    return parser


parser = create_parser()
namespace = parser.parse_args()

if isinstance(namespace.way_old, type(None)) or\
        isinstance(namespace.way_new, type(None) or
                                      namespace.way_old == namespace.way_new):
    print("You should write two different addresses")
else:
    old_text = namespace.way_old.read()
    namespace.way_old.close()

    if namespace.command == 'broke':
        hacker_func(old_text, namespace.way_new, namespace)

    if namespace.command == 'decrypt' or namespace.command == 'encrypt':
        if namespace.cipher == 'vizhener':
            if not isinstance(namespace.key, type(None)):
                enc_or_dec_vizhener(old_text, namespace.way_new, namespace)
            else:
                print("I think that You should enter a key")

        if namespace.cipher == 'caesar':
            if not isinstance(namespace.key, type(None)):
                enc_or_dec_caesar(old_text, namespace.way_new, namespace)
            else:
                print("I think that You should enter a key")

        if namespace.cipher == 'vernam':
            if not isinstance(namespace.key, type(None)):
                enc_or_dec_vernam(old_text, namespace.way_new, namespace)
            else:
                print("I think that You should enter a key")
