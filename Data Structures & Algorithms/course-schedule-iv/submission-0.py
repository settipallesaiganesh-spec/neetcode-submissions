class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        n=numCourses
        isPrerequisite=[[False]*n for _ in range(n)]
        for a,b in prerequisites:
            isPrerequisite[a][b]=True
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if isPrerequisite[i][k] and isPrerequisite[k][j]:
                        isPrerequisite[i][j]=True
        answer=[]
        for u,v in queries:
            answer.append(isPrerequisite[u][v])
        return answer 
        #TIme and space is O(n^3+ q) and O(n^2) respectively