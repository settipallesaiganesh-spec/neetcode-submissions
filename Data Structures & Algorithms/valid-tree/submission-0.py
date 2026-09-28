class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        def find(node: int)->int:
            if parent[node]!= node:
                parent[node]= find(parent[node])
            return parent[node]
        parent=list(range(n))

        num_components=n
        for node_a, node_b in edges:
            root_a=find(node_a)
            root_b=find(node_b)
            if root_a== root_b:
                return False
            parent[root_a]=root_b
            num_components-=1
        return num_components==1
        #Time and space complexity is O(n* alpha(n)) and O(n ) respectively