from typing import List
from collections import deque
class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def topoSort(conditions):
            graph=[[] for _ in range(k+1)]
            indegree = [0] * (k + 1)

            for a, b in conditions:
                graph[a].append(b)
                indegree[b] += 1

            queue = deque()

            for i in range(1, k + 1):
                if indegree[i] == 0:
                    queue.append(i)

            order = []

            while queue:
                node = queue.popleft()
                order.append(node)

                for nei in graph[node]:
                    indegree[nei] -= 1

                    if indegree[nei] == 0:
                        queue.append(nei)

            if len(order) != k:
                return []

            return order

        rows = topoSort(rowConditions)
        cols = topoSort(colConditions)

        if not rows or not cols:
            return []

        rowPos = {}
        colPos = {}

        for i in range(k):
            rowPos[rows[i]] = i
            colPos[cols[i]] = i

        matrix = [[0] * k for _ in range(k)]

        for num in range(1, k + 1):
            matrix[rowPos[num]][colPos[num]] = num

        return matrix
        #Time and space is O(k+ Er + Ec+ k^2) and O(k+ Er+Ec + k^2) respectively
