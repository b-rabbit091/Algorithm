class NQueenProblem(object):

    def isFreeFromAttack(self, chess, row, col):

        for r in range(0, row):
            if chess[r][col] == 1:
                return False

        for c in range(0, col):
            if chess[row][c] == 1:
                return False

        for d1 in range(0, col):
            if chess[d1][d1] == 1:
                return False

        for d2 in range(col+1 , 4):
            row = row-1
            if chess[row][d2] == 1:
                return False

        return True

    def findPositionForQueen(self, chess, row):

        if row == 4:
            return True
        for col in range(4):
            if self.isFreeFromAttack(chess, row, col):
                chess[row][col] = 1
                if self.findPositionForQueen(chess, row + 1):
                    return True
                chess[row][col] = 0
        return False

    def driver(self):
        n = 4
        chess = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(0,n):
            self.findPositionForQueen(chess, 0)
        print(chess)


obj = NQueenProblem()
obj.driver()
