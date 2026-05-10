class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        leftArray = [1] * n 
        rightArray = [1] * n 
        for i in range(1, n):
            leftArray[i] = leftArray[i - 1] * nums[i - 1] 
        for i in range(n - 2, -1, -1):
            rightArray[i] = rightArray[i + 1] * nums[i + 1]

        result = [leftArray[i] * rightArray[i] for i in range(n)]
        return result
