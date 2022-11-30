#!/usr/bin/python3
number = 0
for c in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(c - number)), end="")
    number = 32 if number == 0 else 0
