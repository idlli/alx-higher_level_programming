#!/usr/bin/python3
def uppercase(str):
    tr = dict()
    for char in range(ord('a'), ord('z') + 1):
        tr[chr(char)] = chr(char - ord('a') + ord('A'))
    for c, C in tr.items():
        str = str.replace(c, C)
    print("{}".format(str))
