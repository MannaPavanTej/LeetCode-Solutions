class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.strip()
        n=s.split()
        return len(n[-1])