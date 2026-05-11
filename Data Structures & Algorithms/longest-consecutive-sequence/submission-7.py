class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setUnique = set()
        maxLength = 1
        if len(nums) == 0:
            return 0
        for i in nums:
            setUnique.add(i)
        for i in setUnique:
            if (i - 1) not in setUnique:
                start = i
                curLength = 1
                while start + 1 in setUnique:
                    curLength += 1
                    start += 1
                    maxLength = max(maxLength, curLength)
        return maxLength 
                