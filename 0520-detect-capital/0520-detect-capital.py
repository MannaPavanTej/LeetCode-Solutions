class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.isupper():
            return True
        for i in range(1,len(word)):
            if word[i].isupper():
                return False
        return True
        