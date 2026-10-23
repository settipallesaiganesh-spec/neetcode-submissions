from typing import List
from collections import deque
class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n=len(colors)
        graph=[[]for _ in range(n)]
        indegree=[0]*n
        for u,v in edges:
            graph[u].append(v)
            indegree[v]+=1
        dp=[[0]*26 for _ in range(n)]
        queue=deque()
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
                dp[i][ord(colors[i]) - ord('a')] = 1

        visited = 0
        result = 0

        while queue:
            node = queue.popleft()
            visited += 1

            result = max(result, max(dp[node]))

            for nei in graph[node]:
                for c in range(26):
                    dp[nei][c] = max(
                        dp[nei][c],
                        dp[node][c] + (1 if c == ord(colors[nei]) - ord('a') else 0)
                    )

                indegree[nei] -= 1

                if indegree[nei] == 0:
                    queue.append(nei)

        if visited != n:
            return -1
        return result
        #TIme and space is O(n+m+26n) and O(n+m+ 26n) respectively