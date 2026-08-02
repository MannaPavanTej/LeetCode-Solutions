class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum_=0
        pro=1
        temp=n
        while n>0:
            rem=n%10
            sum_=sum_+rem
            pro=pro*rem
            n=n//10
        return pro-sum_