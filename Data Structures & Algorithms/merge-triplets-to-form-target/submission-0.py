class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x,y,z=target
        a=b=c=False
        for t in triplets:
            if t[0]<=x and t[1]<=y and t[2]<=z:
                if t[0]==x:
                    a=True
                if t[1]==y:
                    b=True
                if t[2]==z:
                    c=True
        return a and b and c
        #TIme and space is O(n) and O(1) respectively 