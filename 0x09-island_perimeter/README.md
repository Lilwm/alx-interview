# Island Perimeter

This Python code calculates the perimeter of an island described in a grid. The grid represents a map where:

- 0 represents water
- 1 represents land

Each cell in the grid is a square with a side length of 1 unit. The cells are connected horizontally and vertically, not diagonally. The grid is rectangular, with its width and height not exceeding 100 units. The grid is completely surrounded by water, and there is only one island or no island present. The island doesn't have "lakes" (water inside that isn't connected to the water surrounding the island).

## Function Signature

```python
def island_perimeter(grid):
    pass

## Input
The function island_perimeter takes a single parameter:

grid: A list of lists representing the grid. Each inner list represents a row, and each element in the inner list represents a cell in the row.
## Output
The function returns an integer representing the perimeter of the island.

## Example
grid = [
    [0, 1, 0, 0],
    [1, 1, 1, 0],
    [0, 1, 0, 0],
    [1, 1, 0, 0]
]

perimeter = island_perimeter(grid)
print(perimeter)  # Output: 16

