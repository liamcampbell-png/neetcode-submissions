class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Core idea: One pass, track the minimum price seen so far and the max profit you could get at each point
        minPrice = float('inf')
        maxProfit = 0
        for price in prices:
            if price < minPrice: 
                minPrice = price
            elif price - minPrice > maxProfit:
                maxProfit = price - minPrice
        return maxProfit
