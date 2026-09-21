# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        check none base case

        find the height of left subtree
        find the height of right subtree

        find the absolute value difference between right and left heights
            check that the difference is not >= 1
        """

        def height(node):
            if not node:
                return 0
            
            return 1 + max(height(node.left), height(node.right))

        if not root:
            return True
        
        left_height = height(root.left)
        right_height = height(root.right)

        balance = abs(left_height - right_height)

        if balance <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        else:
            return False