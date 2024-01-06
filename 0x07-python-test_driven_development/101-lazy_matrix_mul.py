#!/usr/bin/python3
"""
Module to perform lazy matrix multiplication using NumPy
"""

import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """
    Function to multiply two matrices using NumPy.

    Args:
    - m_a: First matrix (list of lists of integers or floats)
    - m_b: Second matrix (list of lists of integers or floats)

    Raises:
    - ValueError: If matrices cannot be multiplied or if matrices are empty.

    Returns:
    - Resulting matrix (NumPy array)
    """
    np_m_a = np.array(m_a)
    np_m_b = np.array(m_b)

    if len(np_m_a) == 0 or len(np_m_b) == 0 or np_m_a.size == 0 or np_m_b.size == 0:
        raise ValueError("Matrices can't be empty")

    if np_m_a.shape[1] != np_m_b.shape[0]:
        raise ValueError("Matrices can't be multiplied")

    result = np.dot(np_m_a, np_m_b)

    return result.tolist()

