class Solution(object):

    def reverse_text(self, text):
        if text == "" or len(text) == 1:
            return text

        return self.reverse_text(text[1:]) + text[0]

    def rev_driver(self):
        text = input("Enter string to be reversed")
        print("Reversed string:- ", self.reverse_text(text))


obj = Solution()
obj.rev_driver()
