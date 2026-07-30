class Solution:
    def calPoints(self, operations: List[str]) -> int:
        st=[]
        for i in operations:

            if i =="C":
                st.pop()
            elif i == "D":
                st.append(2*st[-1])
            elif i =="+":
                st.append(st[-2]+st[-1])
            else:
                st.append(int(i))
        return sum(st)