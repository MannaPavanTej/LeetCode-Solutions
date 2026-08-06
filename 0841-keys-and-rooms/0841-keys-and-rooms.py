class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        ans=[]
        d=deque([0])
        visited=[False]*len(rooms)
        visited[0]=True
        while d:
            ele=d.pop()
            ans.append(ele)
            for nei in rooms[ele]:
                if visited[nei]==False:
                    d.append(nei)
                    visited[nei]=True
        for i in visited:
            if i==False:
                return False
            
        return True