"""
Input: M = 254, K = 1
Output: 524
Explanation: Swap 5 with 2 so number becomes 524

Input: M = 254, K = 2
Output: 542
Explanation: Swap 5 with 2 so number becomes 524, Swap 4 with 2 so number becomes 542

Input: M = 68543, K = 1
Output: 86543
Explanation: Swap 8 with 6 so number becomes 86543
"""


class Solution(object):

    def find_max_number(self, generated_number):
        largest_number = float('-inf')

        for gn in generated_number:
            if gn > largest_number:
                largest_number = gn
        return largest_number

    def swap_numbers(self, c, M, i, swaps, generated_number):

        if swaps >= -1:
            for j in range(0, len(M)):
                k = M[j]
                temp = M.copy()
                temp[j] = c
                temp[i] = k

                t = int(''.join(map(str, temp)))
                generated_number.append(t)

                self.swap_numbers(temp[j], temp.copy(), j, swaps - 1, generated_number)
            return
        return

    def find_permutation(self, M, s, generated_number):
        for i in range(0, len(M)):
            c = M[i]
            self.swap_numbers(c, M, i, s, generated_number)
        return

    def driver(self):
        input_number = [1, 4, 9, 9, 9, 4, 8, 2, 9, 0, 9]
        swaps_allowed = 4
        generated_number = list()
        self.find_permutation(input_number, swaps_allowed, generated_number)
        largest_number = self.find_max_number(generated_number)
        print(largest_number)


obj = Solution()
obj.driver()
