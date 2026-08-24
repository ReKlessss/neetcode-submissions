class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_p, min_p = 0, prices[0]

        for i in range(len(prices)):
            min_p = min(prices[i], min_p)

            p = prices[i] - min_p

            max_p = max(max_p, p)

        return max_p