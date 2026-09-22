class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n=len(s)
        words=set(dictionary)
        dp=[0]*(n+1)
        for i in range(n-1,-1,-1):
            dp[i]=1+dp[i+1]
            for j in range(1,n):
                if s[i:j+1]in words:
                    dp[i]= min(dp[i], dp[j+1])
        return dp[0]
        #TIme and space is O(n^3) and O(n+D) respectively