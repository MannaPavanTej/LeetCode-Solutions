class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        # st=[]
        # temp=[]*len(target)
        # for i in range(1,n+1):
        #     temp.append(i)
        #     if  temp!=target:
        #         if i in temp and i in target :
        #             st.append("Push")

        #         else:
        #             temp.pop()
        #             st.append("Pop")
        # return st
        st = []
        target_idx = 0
        
        for i in range(1, n + 1):
            if target_idx == len(target):
                break  # Stop early once target is completely built
            
            st.append("Push")  # Every stream number is pushed first
            
            if i == target[target_idx]:
                target_idx += 1  # Keep it in stack, move to next target number
            else:
                st.append("Pop")  # Not in target, pop it immediately
                
        return st