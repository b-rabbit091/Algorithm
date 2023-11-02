"""
If n = 1, balanced paranthesis with 1 opening brancket i.e ()
if n=2 , balanced paranthesis with 2 opening brancket i.e ()() , (())
and soon

"""



class Solution(object):

    def check_if_parenthesis_balanced(self, string, res):
        stack = []
        for bracket in string:
            if bracket == '(':
                stack.append('(')
            elif bracket == ')':
                if len(stack) == 0:
                    return
                top_br = stack[-1]
                if top_br != '(':
                    return
                else:
                    stack.pop()

        if len(stack) == 0:
            res.append(string)

    def generate_parentheses(self, string, res, n):
        if len(string) == 2 * n:
            self.check_if_parenthesis_balanced(string, res)
            return

        for i in ['(', ')']:
            string = string + i
            self.generate_parentheses(string, res, n)
            string = string[:-1]

        return

    def driver(self):
        n = 1
        string = ''
        res = []
        self.generate_parentheses(string, res, n)
        print(res)


obj = Solution()
obj.driver()
