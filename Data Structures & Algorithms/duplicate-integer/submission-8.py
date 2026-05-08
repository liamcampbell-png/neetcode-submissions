class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numSet = set()
        for i in nums:
            numSet.add(i)
        if len(numSet) == len(nums):
            return False
        else:
            return True
