#!/usr/bin/python3

import sys

N = int(sys.argv[1])

board = [[0 for j in range(N)] for i in range(N)]


def issafe(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True


def nqueens(board, col, solve_queens):
    if col >= N:
        print(solve_queens)
        return True
    for i in range(N):
        if issafe(board, i, col):
            board[i][col] = 1
            solve_queens.append([i, col])
            nqueens(board, col + 1, solve_queens)
            board[i][col] = 0
            solve_queens.pop()


def slove():
    if len(sys.argv) > 2:
        print("Usage: nqueens N")
        return sys.exit(1)

    if not sys.argv[1].isdigit():
        print("N must be a number")
        return sys.exit(1)

    if N < 4:
        print(" N must be at least 4")
        return sys.exit(1)
    nqueens(board, 0, [])


slove()
