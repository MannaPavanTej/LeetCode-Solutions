class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi=nums[0]
        s=0
        for num in nums:
            s+=num
            maxi=max(maxi,s)
            if s<0:
                s=0
        return maxi