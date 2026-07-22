class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i=0
        j=len(nums)-1
        ans=[0]*len(nums)
        k=len(nums)-1
        while i<=j:
            lef=nums[i]**2
            rig=nums[j]**2
            if lef < rig :
                ans[k]=rig
                j-=1
                k-=1
            else:
                ans[k]=lef
                i+=1
                k-=1
        return ans
