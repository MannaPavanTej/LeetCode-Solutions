class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # d={}
        # for i in nums:
        #     d[i]=d.get(i,0)+1
        # print(d)
        # return max(d,key=d.get)
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num
                count = 1
            elif candidate == num:
                count += 1
            else:
                count -= 1

        return candidate