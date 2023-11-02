"""
For example, if you have the set {1, 2, 3, 4} and you want to find all combinations of 2 elements (K = 2),
the valid combinations would be:

    {1, 2}
    {1, 3}
    {1, 4}
    {2, 3}
    {2, 4}
    {3, 4}
"""


class Solution(object):

    def find_combinations(self, index, candidates, k, combinations):

        if len(combinations) == 2:
            print(combinations)
            return

        for i in range(index, len(candidates)):
            combinations.append(candidates[i])
            self.find_combinations(i + 1, candidates, k, combinations)
            combinations.pop()

    def driver(self):
        candidates = [1, 2, 3, 4]
        k = 2
        combinations = []
        self.find_combinations(0, candidates, k, combinations)


obj = Solution()
obj.driver()
