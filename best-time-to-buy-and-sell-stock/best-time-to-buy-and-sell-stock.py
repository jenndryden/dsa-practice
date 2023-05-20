class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = prices[0]
        result = 0 


        for price in prices:
            if price < min:
                min = price 
            result = max(result, price - min)

        return result