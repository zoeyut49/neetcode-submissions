class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # check each row
        for i in range(9):
            row = set()
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in row:
                    return False
                row.add(board[i][j])

        # check each column
        for i in range(9):
            column = set()
            for j in range(9):
                if board[j][i] == ".":
                    continue
                if board[j][i] in column:
                    return False
                column.add(board[j][i])
        
        # check each 3*3 box
        for i in range(3):
            for j in range(3):
                square = set()
                for m in range(3*i, 3*i + 3):
                    for n in range(3*j, 3*j + 3):
                        if board[m][n] == ".":
                            continue
                        if board[m][n] in square:
                            return False
                        square.add(board[m][n])

        return True