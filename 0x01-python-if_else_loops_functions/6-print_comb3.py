#!/usr/bin/python3
for i in range(10):
    for j in range(i, 10):
        if not j == i:
            print("{}{}".format(i, j), end='\n' if i == 8 and j == 9 else ', ')
