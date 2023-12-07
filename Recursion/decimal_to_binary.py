class Solution(object):

    def convert(self, dec):
        if dec == 1 or dec == 0:
            return str(dec)
        return self.convert(int((int(dec) / 2))) + str((int(dec) % 2))

    def driver(self):
        dec = input("Enter the decimal number")
        print("Binary Form :-", self.convert(dec))


obj = Solution()
obj.driver()
