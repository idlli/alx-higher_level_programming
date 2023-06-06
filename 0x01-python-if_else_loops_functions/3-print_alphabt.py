#!/usr/bin/python3
for ch in range(ord('a'), ord('z') + 1):
    if not chr(ch) in "qe":
        print("{}".format(chr(ch)), end="")
