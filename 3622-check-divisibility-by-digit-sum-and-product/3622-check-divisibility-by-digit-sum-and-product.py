class Solution:
    def checkDivisibility(self, n: int) -> bool:
        org=n
        sum=0
        pro=1
        while org!=0:
            rem=org%10
            sum=sum+rem
            pro=pro*rem
            org=org//10
        total=sum+pro
        if n%total==0:
            return True
        else:    
            return False