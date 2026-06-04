class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        wavi = 0
        for i in range(num1, num2 + 1):
            str_i = str(i)
            for d in range(len(str_i)):
                if i < 100:
                    break
                if d != 0 and d != len(str_i) - 1:
                    if str_i[d] > str_i[d-1] and str_i[d] > str_i[d+1]:
                        wavi += 1
                    elif str_i[d] < str_i[d-1] and str_i[d] < str_i[d+1]:
                        wavi += 1
        return wavi