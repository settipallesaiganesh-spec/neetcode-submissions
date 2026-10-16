from collections import deque
from typing import List
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n==1:
            return [0]
        adj=[[] for _ in range(n)]
        degree=[0]*n
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
            degree[a] += 1
            degree[b] += 1

        queue = deque()

        for i in range(n):
            if degree[i] == 1:
                queue.append(i)

        remaining = n

        while remaining > 2:
            size = len(queue)
            remaining -= size

            for _ in range(size):
                node = queue.popleft()

                for neighbor in adj[node]:
                    degree[neighbor] -= 1

                    if degree[neighbor] == 1:
                        queue.append(neighbor)

        return list(queue)
        #TIme and space is O(n) and O(n) respectively