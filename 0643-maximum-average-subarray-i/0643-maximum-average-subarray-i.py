class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxi=float('-inf')
        s=0
        for i in range(k):
            s=s+nums[i]
        maxi=s
        for i in range(k,len(nums)):
            s=s+nums[i]-nums[i-k]
            maxi=max(s, maxi)
        return maxi/k

