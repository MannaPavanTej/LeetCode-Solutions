class Solution:
    def minOperations(self, s: str) -> int:
        temp = s  
        
        n = len(s)
        d_s = s + s
        min_total_ops = float('inf')
        
        for r in range(n):
            inc_ops = 0
            for i in range(n // 2):
                c1 = ord(d_s[r + i]) - 97
                c2 = ord(d_s[r + n - 1 - i]) - 97
                
                diff = abs(c1 - c2)
                inc_ops += min(diff, 26 - diff)
                
            min_total_ops = min(min_total_ops, r + inc_ops)
            
        return min_total_ops