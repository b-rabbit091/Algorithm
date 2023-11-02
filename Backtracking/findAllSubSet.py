"""
Let's say you have candidates = [4,5,6].
The valid subsets are :

[]
[4]
[4, 5]
[4, 5, 6]
[4, 6]
[5]
[5, 6]
[6]

The algorithm would find and return these combinations.
"""

class Solution(object):

    def find_subset(self, eles, array_set, index):

        print(eles)

        if index == len(array_set):
            return

        for char in range(index, len(array_set)):
            eles.append(array_set[char])
            self.find_subset(eles, array_set, char + 1)
            eles.pop()
        return

    def driver(self):
        array_set = [4, 5, 6]

        self.find_subset([], array_set, 0)


obj = Solution()
obj.driver()
