class Solution:
    def minimumPushes(self, word: str) -> int:
        n=len(word)
        push=0
        for i in range(n):
            cost=(i//8)+1
            push+=cost
        return push