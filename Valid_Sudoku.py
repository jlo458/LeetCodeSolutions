# This is my valid sudoku checker
# It checks whether a given 9x9 grid is valid
# Each row, column and 3x3 square has no repeating numbers 
# Spaces filled with "." are not checked e.g. 

''' [ 
[
    ["7",".","6",".","4",".",".",".","."],
    [".",".",".","8","6","5",".",".","."],
    [".","1",".","2",".",".",".",".","."],
    [".",".",".",".",".","9",".",".","."],
    [".",".",".",".","5",".","5",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".","2",".",".",".","2",".","."],
    ["5",".",".",".",".",".",".",".","."],
    [".","4",".",".",".",".",".",".","."]
] '''

import numpy as np

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        board = np.array(board)

        def checkLine(line): 
            uniq_vals, counts = np.unique(line, return_counts=True)
            for val, count in zip(uniq_vals, counts):
                if val == ".":
                    continue

                elif count > 1:
                    return False
                
                
            return True

        def checkSqu(board):
            newBoard = board.reshape(3, 3, 3, 3)
            for threeLine in newBoard: 
                squ1 = np.array([])
                squ2 = np.array([])
                squ3 = np.array([])


                for line in threeLine: 
                    squ1 = np.concatenate((squ1, line[0]))
                    squ2 = np.concatenate((squ2, line[1]))
                    squ3 = np.concatenate((squ3, line[2]))
                
                res1 = checkLine(squ1)
                res2 = checkLine(squ2)        
                res3 = checkLine(squ3)

                if not res1 or not res2 or not res3: 
                    return False
                
            return True

        valid = True

        for ind in range(9):
            row = board[ind,]
            resA = checkLine(row)

            column = board[:, ind]
            resB = checkLine(column)

            resC = checkSqu(board)

            if not resA or not resB or not resC: 
                valid = False

        return valid
