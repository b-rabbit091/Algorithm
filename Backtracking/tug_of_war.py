"""
Suppose we have the following set of numbers: [3, 4, 5, 2, 1].

The goal is to divide these numbers into two subsets with the minimum difference between their sums.

Output:

    Subset 1: [3, 4]
    Subset 2: [5, 2, 1]
"""
class Solution(object):

    def find_permutation(self, index, candidates, res, subsets):

        n = len(candidates)

        if len(res) in [n // 2, n - n // 2]:
            subsets.append(res.copy())

        if index == n:
            return

        for i in range(index, len(candidates)):
            res.append(candidates[i])
            self.find_permutation(i + 1, candidates, res, subsets)
            res.pop()
        return

    def tug_of_war(self, candidates, subsets):

        total_sum = sum(candidates)
        min_diff = float('inf')
        res = None

        for subset in subsets:
            sum_of_subset = sum(subset)
            sumr = total_sum - sum_of_subset
            diff = abs(sum_of_subset - sumr)

            if diff < min_diff:
                min_diff = diff
                res = (subset, list(set(candidates) - set(subset)))

        return res

    def driver(self):
        candidates = [23, 45, -34, 12, 0, 98, -99, 4, 189, -1, 4]
        res = []
        index = 0
        subsets = []

        self.find_permutation(index, candidates, res, subsets)
        print(self.tug_of_war(candidates, subsets))


obj = Solution()
obj.driver()
