class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)

        # A square must have 4 equal sides
        if total % 4 != 0:
            return False

        side = total // 4

        # Try larger matchsticks first for faster backtracking
        matchsticks.sort(reverse=True)

        if matchsticks[0] > side:
            return False

        sides = [0] * 4

        def backtrack(index):
            if index == len(matchsticks):
                return all(s == side for s in sides)

            stick = matchsticks[index]

            for i in range(4):
                if sides[i] + stick <= side:
                    sides[i] += stick

                    if backtrack(index + 1):
                        return True

                    sides[i] -= stick

                # Avoid trying equivalent empty sides
                if sides[i] == 0:
                    break

            return False

        return backtrack(0)
        #Time and space complexity is O(4^ n) and O(n) respectively