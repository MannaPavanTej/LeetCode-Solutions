class Solution:
    def reverseDegree(self, s: str) -> int:
        total_sum = 0
        for i, ch in enumerate(s):
            alphabet_pos = ord('z') - ord(ch) + 1
            string_pos = i + 1
            total_sum += alphabet_pos * string_pos
        return total_sum