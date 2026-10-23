from typing import List
from  bisect import bisect_right,bisect_left

class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        starts=sorted(start for start, end in flowers)
        ends=sorted(end for start, end in flowers)
        result=[]
        for time in people:
            bloomed=bisect_right(starts, time)
            finished=bisect_left(ends, time )
            result.append(bloomed-finished)
        return result
        #TIme and space is O(n*logn + m*logn) and O(n+m) respectively