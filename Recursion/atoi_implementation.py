"""
The atoi() function takes a string (which represents an integer) as an argument and returns its value.
Input : "112"
Output : 112
"""


class Solution(object):

    def atoi_implement(self, input_str):
        if len(input_str) == 0:
            return 0
        return int(input_str[0])*10**(len(input_str)-1) + self.atoi_implement(input_str[1:])

    def driver(self):
        input_str = input("Enter a number:- ")
        print(self.atoi_implement(input_str))


obj = Solution()
obj.driver()
