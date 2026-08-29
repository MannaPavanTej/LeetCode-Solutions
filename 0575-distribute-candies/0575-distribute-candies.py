class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        # n=len(candyType)//2
        # var=set(candyType)
        # eat=len(var)
        # if n>=eat:
        #     return eat
        # else:
        #     return n
        return min(len(set(candyType)), len(candyType) // 2)
