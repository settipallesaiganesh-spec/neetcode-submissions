class Solution:
    def checkRecord(self, n: int) -> int:
        MOD=10**9+7
        dp=[[0]*3 for _ in range(2)]
        dp[0][0]=1
        for _ in range(n):
            next_dp=[[0]*3 for _ in range(2)]
            for absences in range(2):
                for late in range(3):
                    count=dp[absences][late]
                    if count == 0:
                        continue

                    # Present: resets consecutive late days
                    next_dp[absences][0] = (
                        next_dp[absences][0] + count
                    ) % MOD

                    # Late: allowed only if fewer than 2 consecutive L's
                    if late < 2:
                        next_dp[absences][late + 1] = (
                            next_dp[absences][late + 1] + count
                        ) % MOD

                    # Absent: allowed only once
                    if absences == 0:
                        next_dp[1][0] = (
                            next_dp[1][0] + count
                        ) % MOD

            dp = next_dp

        return sum(sum(row) for row in dp) % MOD
        #TIme and space is O(n) and O(1) respectively