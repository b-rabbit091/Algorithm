class Solution(object):
    def valid_value(self, board, row, col, value):
        # Check the row for the same value
        if value in board[row]:
            return False

        # Check the column for the same value
        if value in [board[i][col] for i in range(len(board))]:
            return False

        # Check the 3x3 subgrid for the same value
        subgrid_size = int(len(board) ** 0.5)  # Assuming a square Sudoku
        start_row, start_col = (row // subgrid_size) * subgrid_size, (col // subgrid_size) * subgrid_size
        for i in range(start_row, start_row + subgrid_size):
            for j in range(start_col, start_col + subgrid_size):
                if board[i][j] == value:
                    return False

        return True

    def sudoku_solve(self, board, row, col):
        r = row
        c=col


        if c == len(board):
            r = row+1
            c=0

        if r == len(board):
            return True

        for value in range(1, len(board)+1):
            if self.valid_value(board, r, c, value):
                board[r][c] = value
                if self.sudoku_solve(board, r, c + 1):
                    return True
                board[r][c]=-1
        return False

    def driver(self):
        n = 9
        board = [[-1 for _ in range(n)] for _ in range(n)]
        self.sudoku_solve(board, 0, 0)
        print(board)


obj = Solution()
obj.driver()
