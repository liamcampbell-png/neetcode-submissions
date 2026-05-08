class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = 0
        set1 = set(nums)
        for i in set1:
            if i - 1 not in set1:
                length = 1
                while (i+length) in set1:
                    length += 1
                count = max(length, count)
        return count
