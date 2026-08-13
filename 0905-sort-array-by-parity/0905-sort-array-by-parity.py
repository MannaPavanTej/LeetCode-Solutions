class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        odd=[]
        eve=[]
        for i  in  nums:
            if i%2==0:
                eve.append(i)
            else:
                odd.append(i)
        return eve+odd