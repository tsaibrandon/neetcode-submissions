class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        profit = 0

        for i in range of prices:
            for j in range of i+1 to prices:
                if j > i:
                    profit = max of current profit vs new profit

        return profit
        """

        profit = 0

        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if prices[j] > prices[i]:
                    profit = max(profit, prices[j] - prices[i])

        return profit