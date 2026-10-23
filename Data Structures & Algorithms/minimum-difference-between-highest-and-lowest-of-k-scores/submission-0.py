from typing import List
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        result=float('inf')
        for i in range(len(nums)-k+1):
            result=min(result,nums[i+k-1]-nums[i])
        return result 
        #TIme and space is O(n*logn) and O(1) respectively