from typing import List

class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:

        def isSubsequence(k):
            removed = set(removable[:k])
            j = 0

            for i in range(len(s)):
                if i in removed:
                    continue

                if j < len(p) and s[i] == p[j]:
                    j += 1

                if j == len(p):
                    return True

            return False

        left = 0
        right = len(removable)

        while left <= right:
            mid = (left + right) // 2

            if isSubsequence(mid):
                left = mid + 1
            else:
                right = mid - 1

        return right
        #TIme and space is O((n+m)* log(m+l)) and O(m) respectively