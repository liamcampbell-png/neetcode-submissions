class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapNums = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in mapNums:
                return [mapNums[complement], i]
            else:
                mapNums[nums[i]] = i
            
            