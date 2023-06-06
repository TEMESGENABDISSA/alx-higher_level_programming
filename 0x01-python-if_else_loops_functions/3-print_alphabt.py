#!/usr/bin/python3
# Author - Temesgen Abdissa
for letter in range(97, 123):
    if chr(letter) != 'q' and chr(letter) != 'e':
        print("{}".format(chr(letter)), end="")
