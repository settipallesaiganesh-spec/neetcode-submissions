from typing import List

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)

        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            points, brainpower = questions[i]

            next_index = i + brainpower + 1

            solve = points + dp[min(next_index, n)]
            skip = dp[i + 1]

            dp[i] = max(solve, skip)

        return dp[0]
        #time and space is O(n) and O(n) respectively