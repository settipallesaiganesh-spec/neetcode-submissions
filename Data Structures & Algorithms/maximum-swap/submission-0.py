class Solution:
    def maximumSwap(self, num: int) -> int:
        digits=list(str(num))
        last={}
        for i,digit in enumerate(digits):
            last[int(digit)]=i
        for i, digit in enumerate(digits):
            current = int(digit)

            for d in range(9, current, -1):
                if d in last and last[d] > i:
                    j = last[d]
                    digits[i], digits[j] = digits[j], digits[i]
                    return int(''.join(digits))

        return num
        #TIme and space is O(n) and O(n) respectively
