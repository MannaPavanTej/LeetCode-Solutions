class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        li=[]
        maxi=max(nums)
        mini=min(nums)
        for i in range(mini,maxi+1):
            if i not in nums:
                li.append(i)
        return li
