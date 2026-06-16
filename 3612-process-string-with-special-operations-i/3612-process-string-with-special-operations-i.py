class Solution:
    def processStr(self, s: str) -> str:
        res = ""
        for c in range(len(s)):
            if s[c] == "*" and res:
                res = res[:-1]
            elif s[c] == "#":
                res += res
            elif s[c] == "%":
                res = res[::-1]
            elif 97 <= ord(s[c]) <= 122:
                res += s[c]
            print(res)
        return res