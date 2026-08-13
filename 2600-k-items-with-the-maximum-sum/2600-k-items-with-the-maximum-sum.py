class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        if k <= numOnes:
                return k
            
        elif k <= numOnes + numZeros:
            return numOnes
        
        else:# If we must pick -1s for the remainder of k
            return numOnes - (k - numOnes - numZeros) 