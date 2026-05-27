class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L = 0
        counts = {}
        maxFreq = 0
        result = 0
        for R in range(len(s)):
            counts[s[R]] = counts.get(s[R], 0) + 1
            maxFreq = max(maxFreq, counts[s[R]])
            if (R - L + 1) - maxFreq > k:
                counts[s[L]] -= 1
                L += 1
            result = max(result, R - L + 1)
        return result