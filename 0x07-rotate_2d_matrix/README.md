# 2D Matrix Rotation

This code rotates a given n x n 2D matrix 90 degrees clockwise. The rotation is done in-place, meaning the matrix is modified directly without creating a new matrix.

## Requirements

- Python 3

## Usage

1. Clone the repository or download the script file.

2. Open a terminal and navigate to the directory containing the script.

3. Run the script with the input matrix defined in the `rotate_2d_matrix` function. Modify the matrix variable to your desired input.

4. Execute the script using the following command:

   ```shell
   ./main_0.py
The script will rotate the matrix 90 degrees clockwise and modify it in-place

## Code Explanation
The code follows these steps to rotate the matrix:

1. Calculate the size n of the matrix (assuming it's a square matrix).

2. Transpose the matrix by swapping elements along the main diagonal. This step swaps the elements at (i, j) with the elements at (j, i).

3. Reverse each row of the transposed matrix. This step flips the order of elements in each row.
