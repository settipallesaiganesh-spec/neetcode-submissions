class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        changes=[0]*1001
        for passengers, start, end in trips:
            changes[start]+=passengers
            changes[end]-=passengers
        current=0
        for i in range(1001):
            current+= changes[i]
            if current>capacity:
                return False
        return True