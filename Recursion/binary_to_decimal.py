class Solution(object):

    def convert(self, bi):
        if bi == "" or len(bi) == 0:
            return 0
        return int(bi[0]) * int(2 ** (len(bi) - 1)) + int(self.convert(bi[1:]))

    def driver(self):
        bi = input("Enter the binary number")
        print("Decimal form:-",self.convert(bi))


obj = Solution()
obj.driver()
