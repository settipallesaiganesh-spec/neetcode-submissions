class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adj=[[] for _ in range(n)]
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        def dfs(node, parent):
            time=0
            for nei in adj[node]:
                if nei==parent:
                    continue
                child_time=dfs(nei,node)
                if child_time>0 or hasApple[nei]:
                    time+=child_time+2
            return time
        return dfs(0,-1)
        #TIme and space is O(n) and O(n) respectively