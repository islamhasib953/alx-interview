# #!/usr/bin/python3

# import sys


# def issafe(board, row, col):
#     for i in range(col):
#         if board[row][i] == 1:
#             return False

#     for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
#         if board[i][j] == 1:
#             return False

#     for i, j in zip(range(row, N, 1), range(col, -1, -1)):
#         if board[i][j] == 1:
#             return False
#     return True


# final_solve = []


# def nqueens(board, col, solve_queens):
#     if col >= N:
#         final_solve.append(sorted(solve_queens))
#         return True
#     for i in range(N):
#         if issafe(board, i, col):
#             board[i][col] = 1
#             solve_queens.append([i, col])
#             nqueens(board, col + 1, solve_queens)
#             board[i][col] = 0
#             solve_queens.pop()


# def slove():
#     if len(sys.argv) != 2:
#         print("Usage: nqueens N")
#         return sys.exit(1)

#     try:
#         global N
#         N = int(sys.argv[1])
#     except ValueError:
#         print("N must be a number")
#         return sys.exit(1)

#     if N < 4:
#         print("N must be at least 4")
#         return sys.exit(1)

#     board = [[0 for j in range(N)] for i in range(N)]
#     nqueens(board, 0, [])

#     final_solve.sort()
#     for i in final_solve:
#         print(i)


# slove()


#!/usr/bin/python3

from sys import argv


def backtrack(r):
    if r == n:
        copy = ["".join(row) for row in board]
        res.append(copy)
        return
    for c in range(n):
        if c in col or (r + c) in posDiag or (r - c) in negDiag:
            continue
        col.add(c)
        posDiag.add(r + c)
        negDiag.add(r - c)
        board[r][c] = "Q"
        backtrack(r + 1)
        col.remove(c)
        posDiag.remove(r + c)
        negDiag.remove(r - c)
        board[r][c] = "."


if len(argv) != 2:
    print('Usage: nqueens N')
    exit(1)
try:
    n = int(argv[1])
except BaseException:
    print('N must be a number')
    exit(1)
if n < 4:
    print('N must be at least 4')
    exit(1)
else:
    col = set()
    posDiag = set()  # (r + c)
    negDiag = set()  # (r - c)

    res = []
    board = [["."] * n for i in range(n)]
    backtrack(0)
    final = []

    # print(res)

    for i in range(0, len(res)):
        # print(res[i])
        gg = []
        for j in range(0, len(res[i])):
            # print(res[i][j])
            for k in range(0, len(res[i][j])):
                if res[i][j][k] == "Q":
                    # print("HIIIIIIII")
                    # print(j, k)
                    gg.append([j, k])
        final.append(gg)

    for pr in final:
        print(pr)
