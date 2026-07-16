class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        arr = []
        for i in range(1, n + 1):
            arr.append(i)
        res = []
        def dfs(i, cur, size):
            if size == k:
                res.append(cur.copy())
                return
            if i >= len(arr) or len(cur) > k:
                return
            cur.append(arr[i])
            dfs(i + 1, cur, len(cur))

            cur.pop()
            dfs(i + 1, cur, len(cur))
        dfs(0, [], 0)
        return res
