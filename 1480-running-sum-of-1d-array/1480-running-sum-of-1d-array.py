class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        li=[]
        sum=0
        for i in nums:
            sum+=i
            li.append(sum)
        return li