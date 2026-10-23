import heapq
from typing import List
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        MOD=10**9+7
        engineers=sorted(zip(efficiency,speed),reverse=True)
        min_heap=[]
        speed_sum=0
        max_performance=0
        for eff, spd in engineers:
            heapq.heappush(min_heap,spd)
            speed_sum+=spd
            if len(min_heap) > k:
                speed_sum -= heapq.heappop(min_heap)

            performance = speed_sum * eff
            max_performance = max(max_performance, performance)

        return max_performance % MOD
        #TIme and space is O(n*logn) and O(n+k) respectively