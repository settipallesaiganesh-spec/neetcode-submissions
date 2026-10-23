class Solution:
    def clearDigits(self, s: str) -> str:
        stack=[]
        for ch in s:
            if ch.isdigit():
                stack.pop()
            else:
                stack.append(ch)
        return "".join(stack)
        #TIme and space is O(n) and O(n) respectively