from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy1 = float('inf')
        profit1 = 0
        buy2 = float('inf')
        profit2 = 0
        for price in prices:
            # first buy: lowest price so far
            buy1 = min(buy1, price)
            # first sell: best profit from first transaction
            profit1 = max(profit1, price - buy1)
            # second buy: effective cost considering profit1
            buy2 = min(buy2, price - profit1)
            # second sell: best profit from two transactions
            profit2 = max(profit2, price - buy2)
        return profit2
prices = list(map(int,input("enter the numbers:").split()))
sol = Solution()
print(sol.maxProfit(prices))  

