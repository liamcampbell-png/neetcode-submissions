class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqCounter = {}
        for i in range(len(nums)):
            freqCounter[nums[i]] = freqCounter.get(nums[i],0) + 1
        bucketList = [[] for _ in range(len(nums) + 1)]

        for num, freq in freqCounter.items():
            bucketList[freq].append(num)
        result = []

        for i in range(len(bucketList) - 1, -1, -1):
            for num in bucketList[i]:
                result.append(num)
                if len(result) == k:
                    return result
    
