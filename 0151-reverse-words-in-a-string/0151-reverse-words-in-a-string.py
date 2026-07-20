class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.strip()
        word=s.split()
        p1=0
        p2=len(word)-1
        while p1<p2:
            word[p1],word[p2]=word[p2],word[p1]
            p1+=1
            p2-=1
        return ' '.join(word)