class Solution:
    def minPrice(self, prices: list[int], discounts: list[int]) -> float:
        prices.sort(reverse=True)
        discounts.sort(reverse=True)
        savings=sum(p*d for p,d in zip(prices,discounts))/100.0
        return sum(prices)-savings