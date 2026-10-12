class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n=len(edges)
        parent=[i for i in range(n+1)]
        rank=[1]*(n+1)
        def find(x):
            while x!=parent[x]:
                parent[x]=parent[parent[x]]
                x=parent[x]
            return x
        def union(x,y):
            p1=find(x)
            p2=find(y)
            if p1==p2:
                return False
            if rank[p1]>rank[p2]:
                parent[p2]=p1
                rank[p1]+=rank[p2]
            else:
                parent[p1]=p2
                rank[p2]+=rank[p1]
            return True
        for a,b in edges:
            if not union(a,b):
                return [a,b]
        #TIme and space is O(n (alpha (n))) and O(n) respectively