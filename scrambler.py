import sys
from encrypt_or_decrypt import enc_or_dec_caesar
from encrypt_or_decrypt import enc_or_dec_vizhener
from encrypt_or_decrypt import enc_or_dec_vernam
from hacker import hacker_func, hacker_learning
import argparse

def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('way_old', type=argparse.FileType(mode = 'r'))
    parser.add_argument('way_new', type=argparse.FileType(mode='w'))
    parser.add_argument('command')
    parser.add_argument('cipher')
    parser.add_argument('key')
    return parser


parser = create_parser()
namespace = parser.parse_args()
old_text = namespace.way_old.read()
namespace.way_old.close()

if namespace.command == 'broke':
    hacker_func(old_text, namespace.way_new, namespace)

elif namespace.command == 'decrypt' or namespace.command == 'encrypt':
    if namespace.cipher == 'vizhener':
        enc_or_dec_vizhener(old_text, namespace.way_new, namespace)
    elif namespace.cipher == 'caesar':
        enc_or_dec_caesar(old_text, namespace.way_new, namespace)
    elif namespace.cipher == 'vernam':
        enc_or_dec_vernam(old_text, namespace.way_new, namespace)
else:
    print("It's a mistake, sorry. Try again.")