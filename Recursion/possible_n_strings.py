"""
Print all possible strings of length k that can be formed from a set of n characters.

Input:
set[] = {'a', 'b'}, k = 3

Output:
aaa
aab
aba
abb
baa
bab
bba
bbb
"""


class Solution(object):

    def find_possible_strings(self, formed_str, candidates, k, res):

        if len(formed_str) == k:
            res.append(formed_str)
            return

        for i in range(0, len(candidates)):
            formed_str = formed_str + candidates[i]
            self.find_possible_strings(formed_str, candidates, k, res)
            formed_str = formed_str[:-1]
        return

    def driver(self):
        # candidates = ['a', 'b']
        # k = 1
        candidates = []

        no_of_candidates = int(input("How many candidates you wish to enter ?"))
        for i in range(no_of_candidates):
            candidates.append(input(f'Enter {i + 1}th candidate:- '))

        k = int(input("What should be the lenght of formed string:- "))

        formed_str = ''
        res = []

        self.find_possible_strings(formed_str, candidates, k, res)
        print("Possible strings are:- ", res)


obj = Solution()
obj.driver()
