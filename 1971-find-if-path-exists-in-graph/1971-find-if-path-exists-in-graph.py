class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj=defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        d=deque([source])
        visited=[False]*n
        visited[source]=True
        while d:
            ele=d.popleft()
            if ele==destination:
                return True
            for nei in adj[ele]:
                if visited[nei]==False:
                    d.append(nei)
                    visited[nei]=True
        return False