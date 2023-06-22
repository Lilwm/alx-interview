#!/usr/bin/python3
""" a function that returns perimeter of a grid"""


def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid.

    grid is a list of list of integers:
      0 represents water
      1 represents land
    Each cell is square, with a side length of 1
    Cells are connected horizontally/vertically (not diagonally).
    grid is rectangular, with its width and height not exceeding 100
    The grid is completely surrounded by water
    There is only one island (or nothing).
    The island doesn’t have “lakes” .
    """
    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    cols = len(grid[0])

    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # assume that all sides are part of the perimeter
                perimeter += 4

                # Check adjacent cells
                if i > 0 and grid[i - 1][j] == 1:
                    # Subtract 2  from each shared side adjacent to land cell
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

    return perimeter
