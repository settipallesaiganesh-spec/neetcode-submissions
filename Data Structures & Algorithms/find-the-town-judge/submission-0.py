class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_count=[0]*(n+1)
        trusted_by= [0]*(n+1)
        for a,b in trust:
            trust_count[a]+=1
            trusted_by[b]+=1
        for person in range(1,n+1):
            if trust_count[person]==0 and trusted_by[person]==n-1:
                return person
        return -1
        #Time and space complexity is O(n+trust.length) and O(n) respectively