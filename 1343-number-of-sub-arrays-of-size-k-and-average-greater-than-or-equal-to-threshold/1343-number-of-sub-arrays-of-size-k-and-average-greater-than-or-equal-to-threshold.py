class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count=0
        s=0
        target_sum = k * threshold
        for i in range(k):
            s=s+arr[i]
        if s>=target_sum:
            count+=1
        for i in range (k,len(arr)):
            s=s+arr[i]-arr[i-k]
            if s>=target_sum:
                count+=1
        return count