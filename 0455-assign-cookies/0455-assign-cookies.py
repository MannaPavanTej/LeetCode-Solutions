class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        child=0
        cook=0
        while child<len(g) and cook<len(s):
            if s[cook]>=g[child]:
                child+=1
            cook+=1
        return child