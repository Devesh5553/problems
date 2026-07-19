class Solution:
    def smallestSubsequence(self, s: str) -> str:
        freq = defaultdict(int)
        seen = set()
        for c in s:
            freq[c] += 1
        stack = []
        for c in s:
            freq[c] -= 1
            if c in seen:
                continue
            while stack and ord(c) < ord(stack[-1]) and freq[stack[-1]] > 0:
                remove = stack.pop()
                seen.remove(remove)
            seen.add(c)                
            stack.append(c)
        return "".join(stack)