#!/usr/bin/python3.5
"""

Multiplies 2 matrices by using the module NumPy.

"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies 2 matrices by using the module NumPy.

    Args:
        m_a: The first matrix to multiply.
        m_b: The second matrix to multiply.

    Returns:
        The multiplied matrix.
    """

    return (numpy.matmul(m_a, m_b))
