# This is an unfinished solution to "Valid Sudoku" problem on LeetCode
# Currently it validates every column and row but does not check every 3x3 box

import numpy as np

board = [
    ["5", "3", ".", ".", "0", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]

board = np.array(board)


valid = True

for ind in range(9):
    row = board[: ind + 1,][0]

    uniq_vals, counts = np.unique(row, return_counts=True)
    for val, count in zip(uniq_vals, counts):
        if val == ".":
            continue

        elif count > 1:
            valid = False

    column = board[:, ind]

    uniq_vals, counts = np.unique(column, return_counts=True)
    for val, count in zip(uniq_vals, counts):
        if val == ".":
            continue

        elif count > 1:
            valid = False


print(valid)
