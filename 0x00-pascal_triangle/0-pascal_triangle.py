#!/usr/bin/python3
""" pascal's triangle"""


def pascal_triangle(n):
    """
    creates a Pascal's triangle up to n rows and returns it as a list of list

    Args:
    - n (int): the number of rows in the triangle to generate.
    
    Returns:
    - triangle : a list of n sublists, each containing the integers in the corresponding row of the Pascal's triangle. If n <= 0, returns an empty list.
    """
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        prev_row = triangle[i-1]
        cur_row = [1]
        for j in range(1, i):
            cur_row.append(prev_row[j-1] + prev_row[j])
        cur_row.append(1)
        triangle.append(cur_row)
    return triangle
