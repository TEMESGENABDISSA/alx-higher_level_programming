#!/usr/bin/python3
# Author - Temesgen Abdissa
for c in range(ord('a'), ord('z')+1):
    if c not in [ord('q'), ord('e')]:
        print(chr(c), end='')
