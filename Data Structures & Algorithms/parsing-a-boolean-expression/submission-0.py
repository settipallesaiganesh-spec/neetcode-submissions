class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack=[]
        for ch in expression:
            if ch==')':
                values=[]
                while stack[-1]!='(':
                    values.append(stack.pop())
                stack.pop()
                operator=stack.pop()
                if operator == '!':
                    result = values[0] == 'f'
                elif operator == '&':
                    result = all(val == 't' for val in values)
                else:
                    result = any(val == 't' for val in values)

                stack.append('t' if result else 'f')

            elif ch != ',':
                stack.append(ch)

        return stack[-1] == 't'
        #TIme and space is O(n) and O(n) respectively