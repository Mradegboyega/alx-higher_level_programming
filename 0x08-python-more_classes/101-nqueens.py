#!/usr/bin/python3
"""
N-Queens Solver
"""

import sys


def is_safe(board, row, col, n):
    """Check if it's safe to place a queen at board[row][col]"""

    # Check this row on the left side
    for i in range(col):
        if board[i] == row or \
           board[i] + i == row + col or \
           board[i] - i == row - col:
            return False

    return True


def solve_nqueens(board, col, n):
    """Recursively solve the N-Queens problem and print solutions"""

    if col == n:
        # All queens are placed, print the solution
        solution = []
        for i in range(n):
            solution.append([i, board[i]])
        print(solution)
        return

    for i in range(n):
        if is_safe(board, i, col, n):
            board[col] = i
            solve_nqueens(board, col + 1, n)


def nqueens(n):
    """Main function to solve N-Queens problem"""

    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Initialize the board
    board = [0] * n

    solve_nqueens(board, 0, n)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        nqueens(n)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

