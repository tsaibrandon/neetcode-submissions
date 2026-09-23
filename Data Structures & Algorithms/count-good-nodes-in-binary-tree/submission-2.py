# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        def dfs function with node, largest value:
            output = 0

            if node is None:
                return None
            
            if node >= largest:
                add 1 to output

            largest = max of largest, current value
            
            left = dfs(node.left, largest)
            right = dfs(node.right, largest)

            return output + left + right

        dfs(root, root.val)
        """

        def dfs(node, largest):
            output = 0

            if node is None:
                return output

            if node.val >= largest:
                output += 1

            largest = max(largest, node.val)
            
            left = dfs(node.left, largest)
            right = dfs(node.right, largest)

            return output + left + right
        
        return dfs(root, root.val)
