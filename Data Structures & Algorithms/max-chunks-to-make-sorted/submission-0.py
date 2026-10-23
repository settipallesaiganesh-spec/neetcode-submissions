from typing import List
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        chunks=0
        max_value=0
        for i in range(len(arr)):
            max_value=max(max_value,arr[i])
            if max_value ==i:
                chunks+=1
        return chunks
        #TIme and space is O(n) and O(1) respectively