from collections import defaultdict
from typing import List

class Solution:
    def calcEquation(
        self,
        equations: List[List[str]],
        values: List[float],
        queries: List[List[str]]
    ) -> List[float]:

        graph = defaultdict(list)

        # Build the graph
        for i in range(len(equations)):
            a, b = equations[i]
            graph[a].append((b, values[i]))
            graph[b].append((a, 1 / values[i]))

        def dfs(src, dst, visited):
            if src not in graph or dst not in graph:
                return -1.0

            if src == dst:
                return 1.0

            visited.add(src)

            for neighbor, weight in graph[src]:
                if neighbor not in visited:
                    result = dfs(neighbor, dst, visited)

                    if result != -1.0:
                        return weight * result

            return -1.0

        result = []

        for a, b in queries:
            result.append(dfs(a, b, set()))

        return result
