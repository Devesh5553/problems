class Solution:
    def reverseParentheses(self, s):
        stk = []
        for c in s:
            if c == ")":
                temp = []
                while stk:
                    char = stk.pop()
                    if char == "(":
                        break
                    temp.append(char)
                stk.extend(temp)
            else:
                stk.append(c)
            print(stk)
        return "".join(stk)