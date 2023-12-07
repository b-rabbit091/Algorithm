class Solution(object):

    def check_palindrome(self, text):

        if len(text) == 1 or len(text) == 0:
            return True
        if text[0] == text[-1]:
            return self.check_palindrome(text[1:len(text) - 1])
        return False

    def driver(self):
        text = input("Enter a word to check palindrome :- ")
        print(self.check_palindrome(text))


obj = Solution()
obj.driver()
