class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()      
        n = ""
        for ch in s:
            if ch.isalnum():
                n += ch
        p1=0
        p2=len(n)-1
        while p1<p2:
            if  n[p1] != n[p2]:
                return(False)
                break
            p1 += 1
            p2 -= 1
        else:
            return(True)