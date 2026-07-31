class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        d={'}':'{',']':'[',')':'('}
        for i in  s:
            if i in "({[":
                st.append(i)
            else:
                if st==[] or d[i]!=st[-1]:
                    return False
                st.pop()
        if st==[]:
            return True
        else:
            return False
