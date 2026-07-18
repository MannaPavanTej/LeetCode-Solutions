class Solution:
    def firstUniqChar(self, s: str) -> int:
        d={}
        for i in s:
            d[i]=d.get(i,0)+1
        for key,value in d.items():
            if value==1:
                return s.index(key)
        return -1