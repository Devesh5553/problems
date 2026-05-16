class Solution:
    def frequencySort(self, s: str) -> str:
        freq = defaultdict(int)
        res = ""
        for c in s:
            freq[c] += 1
        for key, value in sorted(freq.items(), key=lambda x: x[1], reverse = True):
            res += key * value
        return res