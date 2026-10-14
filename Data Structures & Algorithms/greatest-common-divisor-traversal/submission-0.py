from typing import List

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        n=len(nums)
        if n==1:
            return True
        if 1 in nums:
            return False
        parent = list(range(n))
        rank = [0] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            root_x = find(x)
            root_y = find(y)

            if root_x == root_y:
                return

            if rank[root_x] < rank[root_y]:
                parent[root_x] = root_y
            elif rank[root_x] > rank[root_y]:
                parent[root_y] = root_x
            else:
                parent[root_y] = root_x
                rank[root_x] += 1

        factor_index = {}

        for i, num in enumerate(nums):
            factor = 2

            while factor * factor <= num:
                if num % factor == 0:
                    if factor in factor_index:
                        union(i, factor_index[factor])
                    else:
                        factor_index[factor] = i

                    while num % factor == 0:
                        num //= factor

                factor += 1

            if num > 1:
                if num in factor_index:
                    union(i, factor_index[num])
                else:
                    factor_index[num] = i

        root = find(0)

        for i in range(1, n):
            if find(i) != root:
                return False

        return True
        #Time and space is O(n*(sqrt(m) and alpha(n)))
