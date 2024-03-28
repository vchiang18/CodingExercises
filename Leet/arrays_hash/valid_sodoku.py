# https://leetcode.com/problems/valid-sudoku/
from collections import defaultdict

# solution 1 - Using a set for each row/col/square. O(n^2).
# use index coordinates as key for squares hashmap
    def isValidSudoku(self, board):
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] != '.':
                    if(
                        board[r][c] in rows[r] or
                        board[r][c] in cols[c] or
                        board[r][c] in squares[(r//3, c//3)]
                    ):
                        return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])
        return True



# solution 2 - Brute force, with each row/column/square as dict. O(n^2).
class Solution(object):
    def isValidSudoku(self, board):
        for i in range(len(board)):
            row_hash = {}
            row = board[i]
            for j in range(len(row)):
                if row[j] != '.':
                    row_hash[row[j]] = 1 + row_hash.get(row[j], 0)
                    if row_hash[row[j]] > 1:
                        return False

        #repeat with column
        for j in range(len(board[0])):
            col_hash = {}
            for i in range(len(board)):
                col = board[i][j]
                if col != '.':
                    col_hash[col] = 1 + col_hash.get(col, 0)
                    if col_hash[col] > 1:
                        return False

        #repeat with 3x3 square
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                square_hash = {}
                for x in range(3):
                    for y in range(3):
                        x_pos = i + x
                        y_pos = j + y
                        if board[x_pos][y_pos] != '.':
                            square_hash[board[x_pos][y_pos]] = 1 + square_hash.get(board[x_pos][y_pos], 0)
                            if square_hash[board[x_pos][y_pos]] > 1:
                                return False

        return True


# Input: board =
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true
# Example 2:

# Input: board =
# [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
