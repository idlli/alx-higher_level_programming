#!/usr/bin/python3
"""Module for matrix_divided function"""


def matrix_divided(matrix, div):
    """Devides a matrix by a number
    Args:
        matrix (list): the original matrix
        div (int|float): the divider

    Return: a new matrix devided by div

    Raises: TypeError when an arg is not correct
    """
    type_checks = (
        isinstance(matrix, list),
        all(isinstance(row, list) for row in matrix),
        all(isinstance(i, (int, float)) for row in matrix for i in row),
    )
    if not all(type_checks):
        raise TypeError('''matrix must be a matrix \
(list of lists) of integers/floats''')
    if len(set(map(len, matrix))) > 1:
        raise TypeError('Each row of the matrix must have the same size')
    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    divided = list(list(map(lambda x: round(x / div, 2), r)) for r in matrix)
    return divided
