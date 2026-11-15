
class Solution:
    def minDeletions(self, s: str) -> int:

        freq = [0] * 26

        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        used = set()
        deletions = 0

        for count in freq:
            while count > 0 and count in used:
                count -= 1
                deletions += 1

            used.add(count) if count > 0 else None

        return deletions
        #time and space is O(n) and O(1) respectively