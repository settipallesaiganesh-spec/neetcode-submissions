class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        root.val = 0
        queue = [root]

        while queue:
            level_sum = 0
            next_level = []

            for node in queue:
                if node.left:
                    next_level.append(node.left)
                    level_sum += node.left.val

                if node.right:
                    next_level.append(node.right)
                    level_sum += node.right.val

            for node in queue:
                child_sum = 0

                if node.left:
                    child_sum += node.left.val

                if node.right:
                    child_sum += node.right.val

                if node.left:
                    node.left.val = level_sum - child_sum

                if node.right:
                    node.right.val = level_sum - child_sum

            queue = next_level

        return root
        #Time and space is O(n) and O(n) respectively