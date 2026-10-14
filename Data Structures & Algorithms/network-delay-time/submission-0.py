class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph=[[float('inf')]*n for _ in range(n)]
        for source, target, weight in times:
            graph[source-1][target-1]= weight
        distances= [float('inf')]*n
        distances[k - 1] = 0
      
        # Track visited nodes
        visited = [False] * n
      
        # Dijkstra's algorithm: process all n nodes
        for _ in range(n):
            # Find the unvisited node with minimum distance
            min_node = -1
            for node in range(n):
                if not visited[node] and (min_node == -1 or distances[min_node] > distances[node]):
                    min_node = node
          
            # Mark the selected node as visited
            visited[min_node] = True
          
            # Update distances to all neighbors of the selected node
            for neighbor in range(n):
                distances[neighbor] = min(distances[neighbor], 
                                         distances[min_node] + graph[min_node][neighbor])
      
        # Find the maximum distance (time for signal to reach all nodes)
        max_distance = max(distances)
      
        # If any node is unreachable, return -1; otherwise return the max distance
        return -1 if max_distance == float('inf') else max_distance
        #Time and space complexity is O(n^ 2) and O(n^2 ) respectively