class Solution:
    def knightDialer(self, n: int) -> int:
        MOD = 10**9 + 7

        moves = [
            [4, 6],       # 0
            [6, 8],       # 1
            [7, 9],       # 2
            [4, 8],       # 3
            [0, 3, 9],    # 4
            [],           # 5
            [0, 1, 7],    # 6
            [2, 6],       # 7
            [1, 3],       # 8
            [2, 4]        # 9
        ]

        dp = [1] * 10

        for _ in range(n - 1):
            next_dp = [0] * 10

            for digit in range(10):
                for neighbor in moves[digit]:
                    next_dp[neighbor] = (next_dp[neighbor] + dp[digit]) % MOD

            dp = next_dp

        return sum(dp) % MOD