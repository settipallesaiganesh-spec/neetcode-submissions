from collections import deque
from typing import List

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        q = deque()
        water = 0

        # Add all land cells to the queue
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    q.append((r, c))
                else:
                    water += 1

        # No land or no water
        if not q or water == 0:
            return -1

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        dist = -1

        # Multi-source BFS
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                        grid[nr][nc] = 1
                        q.append((nr, nc))

            dist += 1

        return dist
        #time and space is O(n^2) and O(n^2) respectively