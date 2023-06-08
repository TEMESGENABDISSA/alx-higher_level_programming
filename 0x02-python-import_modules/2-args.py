#!/usr/bin/python3
import sys

args = sys.argv[1:]
num_args = len(args)

print("Number of argument(s):", num_args, end=" ")

if num_args == 0:
    print(".", end="\n")
elif num_args == 1:
    print("Argument:", end="\n")
    print("1:", args[0])
else:
    print("Arguments:", end="\n")
    for i, arg in enumerate(args):
        print(f"{i+1}: {arg}")

