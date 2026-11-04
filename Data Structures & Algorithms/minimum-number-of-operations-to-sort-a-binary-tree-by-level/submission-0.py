
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        from collections import deque

        q = deque([root])
        ans = 0

        while q:
            n = len(q)
            arr = []

            for _ in range(n):
                node = q.popleft()
                arr.append(node.val)

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            sorted_arr = sorted(arr)

            pos = {val: i for i, val in enumerate(sorted_arr)}
            visited = [False] * n

            for i in range(n):
                if visited[i] or pos[arr[i]] == i:
                    continue

                cycle_size = 0
                j = i

                while not visited[j]:
                    visited[j] = True
                    j = pos[arr[j]]
                    cycle_size += 1

                ans += cycle_size - 1

        return ans
        #Time and space is O(N*logW) and O(n) respectively
