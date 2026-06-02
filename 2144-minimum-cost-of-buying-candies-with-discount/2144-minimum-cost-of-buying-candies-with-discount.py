class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        res = 0
        n = 0
        cost.sort(reverse = True)
        r  = 0
        while r < len(cost):
            res += cost[r]
            r += 1
            n += 1
            if n % 2 == 0:
                r += 1
            print(res)
        return res