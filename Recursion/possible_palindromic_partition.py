"""

Outputs the possible palindromic partitions:

Ex: input : geeks
    Output :  [ee]

    input : nitin
    output : [nitin,iti]

"""


def is_palindrome(substr):
    return substr == substr[::-1]


class Solution(object):
    def solve_permutation(self, substr, low, high, text, res):

        if len(substr) > 1 and is_palindrome(substr):
            res.add(substr)

        if low == 1 or high == len(text) + 1:
            return

        for i in range(low, high):
            c = text[i:high]
            self.solve_permutation(c, i, high + 1, text, res)
        return

    def driver(self):
        text = input("Enter a word:- ")
        low = 0
        high = 1
        res = set()

        self.solve_permutation('', low, high, text, res)
        print(res)


obj = Solution()
obj.driver()
