class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        i, j = len(a)-1, len(b)-1
        carry = 0
        while i >=0 or j >= 0 or carry > 0:
            val1 = int(a[i]) if i >= 0 else 0
            val2 = int(b[j]) if j >= 0 else 0
            total = val1 + val2 + carry
            res.append(str(total%2))
            carry = total//2
            i-=1
            j-=1
        return ''.join(res[::-1])