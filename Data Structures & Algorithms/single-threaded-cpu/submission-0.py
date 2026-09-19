import heapq
from typing import List
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n=len(tasks)
        tasks=[(tasks[i][0],tasks[i][1],i)for i in range(n)]
        tasks.sort()
        heap=[]
        ans=[]
        time=0
        i=0
        while i<n or heap:
            if not heap and time<tasks[i][0]:
                time= tasks[i][0]
            while i<n and tasks[i][0]<=time:
                enqueue,process,index= tasks[i]
                heapq.heappush(heap,(process,index))
                i+=1
            process, index= heapq.heappop(heap)
            time+= process
            ans.append(index)
        return ans 
        #Time and space is O(N*logn ) and O(n) respectively
