class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n=len(grid)
        NEG_INF=float('-inf')
        dp=[[NEG_INF]*n for _ in range(n)]
        dp[0][0]=grid[0][0]
        for k in range(1,2*n - 1):
            curr = [[NEG_INF] * n for _ in range(n)]

            for r1 in range(max(0, k - n + 1), min(n, k + 1)):
                for r2 in range(max(0, k - n + 1), min(n, k + 1)):

                    c1 = k - r1
                    c2 = k - r2

                    if grid[r1][c1] == -1 or grid[r2][c2] == -1:
                        continue

                    best = NEG_INF

                    # Both move down or right
                    for pr1 in (r1, r1 - 1):
                        for pr2 in (r2, r2 - 1):
                            if pr1 >= 0 and pr2 >= 0:
                                best = max(best, dp[pr1][pr2])

                    if best == NEG_INF:
                        continue

                    cherries = grid[r1][c1]
                    if r1 != r2:
                        cherries += grid[r2][c2]

                    curr[r1][r2] = best + cherries

            dp = curr

        return max(0, dp[n - 1][n - 1])
        #TIme and space is O(n^3) and O(n^2) respectively
