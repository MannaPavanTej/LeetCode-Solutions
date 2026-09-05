class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans=[]
        
        for i in range(left,right+1):
            org=i
            self_driveing=True
            while org!=0:
                rem=org%10
                if rem==0 or i%rem!=0:
                    #org=org//10
                    self_driveing=False
                    break
                org//=10
            if self_driveing:
                ans.append(i)
        return ans