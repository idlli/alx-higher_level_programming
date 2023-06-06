#!/usr/bin/python3
for i in range(25, -1, -1):
    print("{}".format(chr(i + (ord('A') if i % 2 == 0 else ord('a')))), end='')
