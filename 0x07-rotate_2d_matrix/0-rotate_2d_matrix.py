#!/usr/bin/python3
"""rotates 2d matrix"""


def rotate_2d_matrix(matrix):
    """
    Rotates a 2D matrix 90 degrees clockwise in-place.

    Args:
        matrix (list[list]): The 2D matrix to be rotated.

    Returns:
        None. The matrix is edited in-place.
    """

    n = len(matrix)

    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row of the transposed matrix
    for i in range(n):
        matrix[i] = matrix[i][::-1]
