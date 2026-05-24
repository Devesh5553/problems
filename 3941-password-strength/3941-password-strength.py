class Solution:
    def passwordStrength(self, password: str) -> int:
        seen = set()
        score = 0
        for c in password:
            if 97 <= ord(c) <= 122 and c not in seen:
                score += 1
            elif 65 <= ord(c) <= 90 and c not in seen:
                score += 2
            elif c in "!@$#" and c not in seen:
                score += 5
            elif 48 <= ord(c) <= 57 and c not in seen:
                score += 3
            seen.add(c)
        return score
