class Solution:
    def countAndSay(self, n: int) -> str:
        def separate_digits(s):
            result = []
            count = 1

            for i in range(1, len(s)):
                if s[i] == s[i - 1]:
                    count += 1
                else:
                    result.append([int(s[i - 1]), count])
                    count = 1

            if s:
                result.append([int(s[-1]), count])
            return result

        def concat(arr):
            res = ""
            for i, j in arr:
                res += str(j) + str(i)
            return res
        
        ans = "1"
        for _ in range(n - 1):
            arr = separate_digits(ans)
            ans = concat(arr)
        return ans
        

