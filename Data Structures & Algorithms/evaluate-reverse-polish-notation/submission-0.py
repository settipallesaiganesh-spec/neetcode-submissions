class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for token in tokens:
            if token=="+" or token=="-" or token=="*" or token=="/":
                b=stack.pop()
                a=stack.pop()
                if token=="+":
                    result=a+b
                elif token=="-":
                    result=a-b
                elif token=="*":
                    result=a*b
                else:
                    result=int(a/b)
                stack.append(result)
            else:
                stack.append(int(token))
        return stack[-1]
        #TIme and space is O(n) and O(n) respectively