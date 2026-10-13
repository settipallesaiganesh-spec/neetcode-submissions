import heapq
from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        max_heap = [(-freq, char) for char, freq in count.items()]
        heapq.heapify(max_heap)

        res = []
        prev_freq, prev_char = 0, ""

        while max_heap:
            freq, char = heapq.heappop(max_heap)
            res.append(char)

            if prev_freq < 0:
                heapq.heappush(max_heap, (prev_freq, prev_char))

            freq += 1
            prev_freq, prev_char = freq, char

        if len(res) != len(s):
            return ""

        return "".join(res)
    #TIme and space is O(n*logk ) and O(n+k) respectively