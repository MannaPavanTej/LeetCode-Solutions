class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count=0
        maxi=0
        for ch in range(k):
            if s[ch] in "aeiouAEIOU":
                count+=1
        maxi=count
        for ch in range(k,len(s)):
            if s[ch] in "aeiouAEIOU":
                count+=1
            if s[ch-k] in 'aeiou':
                count-=1
            maxi=max(maxi,count)
        return maxi

