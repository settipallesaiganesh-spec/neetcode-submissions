class Solution:
    def reverse(self, x: int) -> int:
        MAX=2**31-1
        MIN=-(2**31)
        res=0
        sign=-1 if x<0 else 1
        x=abs(x)
        while x>0:
            digit=x%10
            x//=10
            if res>MAX//10 or(res==MAX//10 and digit >7):
                return 0
            res=res*10+digit
        return sign *res
        #TIme and space is O(1) and O(1) respectively