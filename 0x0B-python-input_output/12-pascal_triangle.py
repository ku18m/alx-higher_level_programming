#!/usr/bin/python3

"""pascal_triangle module"""


def pascal_triangle(n):
    """
    Function that returns:
    a list of lists of integers representing the Pascal's triangle of n.

    Args:
        n: The size of the triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) != n:
        last = triangle[-1]
        first = [1]

        for i in range(len(last) - 1):
            first.append(last[i] + last[i + 1])

        first.append(1)
        triangle.append(first)

    return triangle
