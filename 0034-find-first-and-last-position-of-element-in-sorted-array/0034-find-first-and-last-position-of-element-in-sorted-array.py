class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l=0
        r=len(nums)-1
        res1=-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target :
                res1=mid
                r=mid-1
            elif nums[mid]>target:
                r=mid-1
            else:
                l=mid+1
        l=0
        r=len(nums)-1
        res2=-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target :
                res2=mid
                l=mid+1
            elif nums[mid]>target:
                r=mid-1
            else:
                l=mid+1
        return [res1,res2]