class Solution(object):

    def find_sum(self, n):
        if n == 0:
            return 0

        return n + self.find_sum(n - 1)

    def driver(self):
        n = int(input("Enter the number:- "))
        print("The sum is:- ", self.find_sum(n))


obj = Solution()
obj.driver()
