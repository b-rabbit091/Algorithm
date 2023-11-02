"""
Let's say you have candidates = [2, 3, 6, 7] and target = 7.
The valid combinations are [2, 2, 3] and [7].
The algorithm would find and return these combinations.
"""


class Solution(object):

    def find_combinations(self, index, candidates, target, combinations):

        if sum(combinations) > target:
            return

        if sum(combinations) == target:
            print(combinations)
            return

        for i in range(index, len(candidates)):
            combinations.append(candidates[i])
            self.find_combinations(i, candidates, target, combinations)
            combinations.pop()

    def driver(self):
        candidates = [2, 3, 6, 7]
        target = 7
        combinations = []

        self.find_combinations(0, candidates, target, combinations)


obj = Solution()
obj.driver()
