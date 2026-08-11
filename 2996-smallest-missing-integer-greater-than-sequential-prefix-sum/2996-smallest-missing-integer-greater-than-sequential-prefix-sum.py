class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        presum=nums[0]
        for i in range(1,len(nums)):
            if nums[i] == nums[i - 1] + 1:
                presum+=nums[i]
            else:
                break
        num_set=set(nums)
        while presum in num_set:
            presum+=1
        return presum