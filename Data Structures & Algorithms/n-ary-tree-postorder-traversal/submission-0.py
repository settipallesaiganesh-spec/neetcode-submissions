
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []

        result = []
        stack = [root]

        while stack:
            node = stack.pop()
            result.append(node.val)

            # Push all children onto the stack
            for child in node.children:
                if child:
                    stack.append(child)

        return result[::-1]
        #time and space is O(n) and O(n) respectively