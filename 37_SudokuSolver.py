#37. Sudoku Solver
class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.backtrack(board)
        return board
        
    def backtrack(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for c in '123456789':
                        if self.isPointValid(board, i, j, c):
                            board[i][j] = c
                            if self.backtrack(board): 
                                return True
                            else:
                                board[i][j] = '.' # backtrack
                    return False
        return True
        #return board
    
    def isPointValid(self, board, x, y, c):
        for i in range(9):
            if board[i][y] == c: # check col
                return False
            if board[x][i] == c: # check row
                return False
            if board[3*(x//3)+i//3][3*(y//3)+i%3] == c: # check 3 * 3 block
                return False
        return True
    
        
board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
a=Solution().solveSudoku(board)
print(a)
