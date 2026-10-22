from typing import List
class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        n=len(nums)
        total=sum(nums)
        for k in range(1,n//2+1):
            if total*k%n ==0:
                target=total*k//n
                dp = [set() for _ in range(k + 1)]
                dp[0].add(0)

                for num in nums:
                    for size in range(k, 0, -1):
                        for s in dp[size - 1]:
                            dp[size].add(s + num)

                if target in dp[k]:
                    return True

        return False
        #TIme and space is O(n^2* no of reachable sums) and Space depends on no of reachable sums stored in the dp sets 