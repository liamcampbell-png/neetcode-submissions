class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        for i in prices:
            if i < prices[0]:
                prices[0] = i
            ans = max(ans, i - prices[0])
        return ans