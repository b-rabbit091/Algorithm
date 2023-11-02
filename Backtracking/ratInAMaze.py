"""
Given the path of maze in matrix form, the algorith returns the path
that can be travelled to get to the destinations.

Ex:
Maze= [[1, 0, 0, 0],
       [1, 1, 0, 1],
       [1, 1, 0, 0],
       [0, 1, 1, 1]]


Solution :

1. [[1, 0, 0, 0],
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 1, 1, 1]]

2. [[1, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 1]]

"""
class Solution(object):

    def find_path(self, maze, row, col, res):

        if row > len(maze) - 1 or col > len(maze) - 1:
            return

        if row == len(maze) - 1 and col == len(maze) - 1:
            res[row][col] = 1
            k = res.copy()
            print(k)
            return

        if maze[row][col] == 1:
            res[row][col] = 1
            self.find_path(maze, row + 1, col, res)
            self.find_path(maze, row, col + 1, res)
            res[row][col] = 0
        return

    def driver(self):
        maze = [[1, 0, 0, 0], [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1]]
        res = [[0 for _ in range(len(maze))] for _ in range(len(maze))]

        self.find_path(maze, 0, 0, res)


obj = Solution()
obj.driver()
