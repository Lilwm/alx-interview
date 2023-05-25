#!/usr/bin/env python3
"""Solve the N-queens puzzle."""
import sys


def n_queens(row, N, queens, blocked_cols, blockedDiags, blockedRevDiags):
    """Solve the N-queens puzzle.
    Args:
    n: The size of the chessboard.

    Returns:
    A list of all possible solutions to the puzzle.
    """
    if row == N:
        if len(queens) == N:
            print(queens)
        return

    possible_moves = []
    for col in range(N):
        if col in blocked_cols:
            continue
        if row - col in blockedDiags or N - col - row in blockedRevDiags:
            continue
        if [row, col] not in queens:
            possible_moves.append(col)

    for col in possible_moves:
        n_queens(
            row + 1,
            N,
            queens + [[row, col]],
            blocked_cols + [col],
            blockedDiags + [row - col],
            blockedRevDiags + [N - col - row]
        )


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    N = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if N < 4:
    print("N must be at least 4")
    sys.exit(1)

n_queens(0, N, [], [], [], [])
