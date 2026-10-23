class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp=[0]*26
        for ch in s:
            curr=ord(ch)-ord('a')
            best=0
            left=max(0,curr-k)
            right=min(25,curr+k)
            for i in range(left, right+1):
                best=max(best,dp[i])
            dp[curr]=best+1
        return max(dp)
        #TIme and space is O(n) and O(1) respectively