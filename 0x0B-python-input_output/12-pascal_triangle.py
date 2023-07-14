#!/usr/bin/python3
"""Modlue for ``pascal_triangle()`` function"""


def pascal_triangle(n):
    """
    Calculates a pascal triangle of height n
    Args:
        n (int): the height of the triangle
    Returns:
        list of lists representing rows of the triangle
    """
    result = []
    if n <= 0:
        return result
    result.append([1])
    for row in range(1, n):
        result.append([])
        for i in range(row + 1):
            if i == 0 or i == row:
                result[-1].append(1)
                continue
            num = result[-2][i - 1]
            num += result[-2][i]
            result[-1].append(num)
    return result
