class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        s=0
        mini=float('inf')
        for right in range(0,len(nums)):
            s=s+nums[right]
            while s>= target:
                s=s-nums[left]
                mini=min(mini,right-left+1)
                left+=1
        if mini==float('inf'):
            return 0
        else:
            return mini