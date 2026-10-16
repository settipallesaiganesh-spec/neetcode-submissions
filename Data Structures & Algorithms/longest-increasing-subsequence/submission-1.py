from typing import List
import bisect
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis=[]
        for num in nums:
            index=bisect.bisect_left(lis,num)
            if index==len(lis):
                lis.append(num)
            else:
                lis[index]=num
        return len(lis)
        #Time and space is O(n*logn ) and O(n) respectively