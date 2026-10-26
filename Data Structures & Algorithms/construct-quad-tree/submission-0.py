

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def dfs(r,c,size):
            same=True
            val=grid[r][c]
            for i in range(r,r+size):
                for j in range(c,c+size):
                    if grid[i][j]!=val:
                        same=False
                        break
                if not same:
                    break
            if same:
                return Node(bool(val), True, None, None, None, None)

            # Divide the grid into four quadrants
            half = size // 2

            topLeft = dfs(r, c, half)
            topRight = dfs(r, c + half, half)
            bottomLeft = dfs(r + half, c, half)
            bottomRight = dfs(r + half, c + half, half)

            return Node(
                True, False,
                topLeft, topRight,
                bottomLeft, bottomRight
            )

        return dfs(0, 0, len(grid))
        #TIme and space is O(n^2* logn) and O(logn) respectively