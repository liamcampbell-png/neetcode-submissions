class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        set1 = set()
        L = 0
        result = 0
        for R in range(len(s)):
            while s[R] in set1:
                set1.remove(s[L])
                L += 1
            set1.add(s[R])
            result = max(result, R - L + 1)
        return result
