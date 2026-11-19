from collections import deque
from typing import List

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj = [[] for _ in range(n + 1)]

        # Build undirected graph
        for u, v, dist in roads:
            adj[u].append((v, dist))
            adj[v].append((u, dist))

        q = deque([1])
        visited = {1}
        res = float('inf')

        # BFS
        while q:
            node = q.popleft()

            for nei, dist in adj[node]:
                res = min(res, dist)

                if nei not in visited:
                    visited.add(nei)
                    q.append(nei)

        return res
        #time and space is O(V+E) and O(V+E) respectively