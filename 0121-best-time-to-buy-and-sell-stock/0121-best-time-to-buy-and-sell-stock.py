class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        mini=prices[0]
        for i in range (1,len(prices)):
            curr=prices[i]-mini
            if curr>profit:
                profit=curr
            mini=min(prices[i],mini)
        return profit