from typing import List
class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        class DSU:
            def __init__(self,n):
                self.parent=list(range(n+1))
                self.rank=[1]*(n+1)
                self.components=n
            def find(self,x):
                if self.parent[x]!=x:
                    self.parent[x]=self.find(self.parent[x])
                return self.parent[x]
            def union(self, x, y):
                root_x = self.find(x)
                root_y = self.find(y)

                if root_x == root_y:
                    return False

                if self.rank[root_x] < self.rank[root_y]:
                    root_x, root_y = root_y, root_x

                self.parent[root_y] = root_x
                self.rank[root_x] += self.rank[root_y]
                self.components -= 1
                return True

        alice = DSU(n)
        bob = DSU(n)
        removed = 0

        # Process shared edges first
        for edge_type, u, v in edges:
            if edge_type == 3:
                merged_alice = alice.union(u, v)
                merged_bob = bob.union(u, v)

                if not merged_alice:
                    removed += 1

        # Process Alice-only and Bob-only edges
        for edge_type, u, v in edges:
            if edge_type == 1:
                if not alice.union(u, v):
                    removed += 1

            elif edge_type == 2:
                if not bob.union(u, v):
                    removed += 1

        # Both graphs must be connected
        if alice.components != 1 or bob.components != 1:
            return -1

        return removed
        #TIme and space is O( E* alpha (n)) and O(n) respectively