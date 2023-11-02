"""
A target to be achieved with sum of given candidates. No repetition.
"""


class Solution(object):

    def find_combinations(self, index, candidates, combinations, target_sum):

        if sum(combinations) == target_sum:
            print(combinations)
            return

        for i in range(index, len(candidates)):
            combinations.append(candidates[i])
            self.find_combinations(i + 1, candidates, combinations, target_sum)
            combinations.pop()
        return

    def driver(self):
        candidates = [2, 3, 5, 7]
        combinations = []
        target_sum = 7

        self.find_combinations(0, candidates, combinations, target_sum)


obj = Solution()
obj.driver()
