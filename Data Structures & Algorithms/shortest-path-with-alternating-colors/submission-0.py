from collections import deque
from typing import List

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red = [[] for _ in range(n)]
        blue = [[] for _ in range(n)]

        for u, v in redEdges:
            red[u].append(v)

        for u, v in blueEdges:
            blue[u].append(v)

        # dist[node][0] = shortest path ending with red
        # dist[node][1] = shortest path ending with blue
        dist = [[float('inf')] * 2 for _ in range(n)]

        q = deque()

        # Start with both possible previous colors
        dist[0][0] = 0
        dist[0][1] = 0
        q.append((0, 0))
        q.append((0, 1))

        while q:
            node, last_color = q.popleft()

            # If last edge was red, use blue edges
            if last_color == 0:
                for nei in blue[node]:
                    if dist[nei][1] == float('inf'):
                        dist[nei][1] = dist[node][0] + 1
                        q.append((nei, 1))

            # If last edge was blue, use red edges
            else:
                for nei in red[node]:
                    if dist[nei][0] == float('inf'):
                        dist[nei][0] = dist[node][1] + 1
                        q.append((nei, 0))

        # Minimum distance using either ending color
        res = []

        for r, b in dist:
            ans = min(r, b)
            res.append(-1 if ans == float('inf') else ans)

        return res
        #time and space is O(n+R+B) and O(n+r+B) respectively