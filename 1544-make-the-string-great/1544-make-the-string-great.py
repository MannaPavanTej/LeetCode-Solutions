class Solution:
    def makeGood(self, s: str) -> str:
        st=[]
        for i in s:
            if st!=[] and st[-1] != i and st[-1].lower() == i.lower():
                st.pop()
            else:
                st.append(i)
        return ''.join(st)