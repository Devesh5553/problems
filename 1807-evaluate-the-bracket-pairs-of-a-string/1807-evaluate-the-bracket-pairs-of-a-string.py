class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        know_dic = {}
        for key, value in knowledge:
            know_dic[key] = value
        res = ""
        i = 0
        while i < len(s):
            if s[i] == '(':
                curr = ""
                while s[i] != ')' and i < len(s):
                    i += 1
                    if s[i] is not ")":
                        curr += s[i]
                if curr in know_dic:
                    res += know_dic[curr]
                else:
                    res += "?"
            else:
                res += s[i]
            i += 1
        print(know_dic)
        return res
