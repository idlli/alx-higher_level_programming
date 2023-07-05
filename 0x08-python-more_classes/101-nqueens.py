#!/usr/bin/python3
"""A module that defines a class `Rectangle`"""


from sys import argv

if len(argv) != 2:
    print('Usage: nqueens N')
    exit(1)

n = None

try:
    n = int(argv[1])
except ValueError:
    print('N must be a number')
    exit(1)

if n < 4:
    print('N must be at least 4')
    exit(1)

board = {(x, y): 0 for x in range(n) for y in range(n)}

states = []

queen_stack = []


def act_queen(pos, take_out=False):
    targets = []
    board[pos] = 0 if take_out else -1
    for key in board:
        if (pos[0] == key[0]
                or pos[1] == key[1]
                or abs(pos[0] - key[0]) == abs(pos[1] - key[1])):
            if key == pos:
                continue
            if board[key] == -1:
                board[pos] = 0
                for t in targets:
                    board[t] -= -1 if take_out else 1
                return False
            targets.append(key)
            board[key] += -1 if take_out else 1
    return True


def backtrack(m):
    if m == 0:
        # jump = False
        # for st in states:
        #     occ = 0
        #     for pos in st:
        #         if pos in queen_stack:
        #             occ += 1
        #     if occ == n:
        #         jump = True
        #         break
        # if jump:
        #     return
        for st in states:
            if all(pos in st for pos in queen_stack):
                return
        states.append(queen_stack.copy())
        return
    for x in range(n):
        for y in range(n):
            pos = (x, y)
            if board[pos] != 0:
                continue
            if not act_queen(pos, take_out=False):
                continue
            queen_stack.append(pos)
            backtrack(m - 1)
            act_queen(pos, take_out=True)
            queen_stack.pop()


backtrack(n)

print(*states, sep='\n')
