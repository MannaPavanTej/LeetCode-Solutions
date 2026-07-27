class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(0,len(nums)):
            min_index=i
            ele=nums[i]
            for j in range(i+1,len(nums)):
                if nums[j]<ele:
                    min_index=j
                    ele=nums[j]
            nums[min_index],nums[i]=nums[i],nums[min_index]
        return nums