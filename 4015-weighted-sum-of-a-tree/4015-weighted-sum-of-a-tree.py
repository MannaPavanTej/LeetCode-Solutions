class Solution:
    def weightedSum(self, parent: list[int], nums: list[int]) -> int:
        def fun(arr, parent, x):
            if arr[x] == 0:
                # print(arr)
                # print(arr[x], "*", parent[arr[x]], x)
                arr[x] = fun(arr, parent, parent[x])+1
            return arr[x]
            
        ans = 0
        n = len(nums)
        arr = [0]*len(nums)
        arr[0] = 1
        for i in range(1, n):
            if arr[i] == 0:
                # print(parent[i], arr[i])
                arr[i] = fun(arr, parent, parent[i])+1
        h = max(arr)
        # print(h, arr)
        for i in range(n):
            ans += nums[i]*(h-arr[i]+1)
        return ans