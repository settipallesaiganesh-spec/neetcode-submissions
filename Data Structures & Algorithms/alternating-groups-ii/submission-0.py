class Solution:
    def numberOfAlternatingGroups(self, colors: list[int], k: int) -> int:
        n = len(colors)
        count = 0
        streak = 1

        for i in range(1, n + k - 1):
            if colors[i % n] != colors[(i - 1) % n]:
                streak += 1
            else:
                streak = 1

            if streak >= k:
                count += 1

        return count
        #time and space is O(n) and O(1) respectively