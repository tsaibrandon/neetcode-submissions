# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        global count variable = 0
        global result variable = 0
        
        def dfs(node):
            curr = node
            
            if count == k:
                return
            if the tree is empty:
                return None
            
            dfs(node.left)

            if count < k:
                count add 1
                
                if count == k:
                    result = node.val

            dfs(node.right)

        dfs(root)
        return result
        """
        self.count = 0
        self.result = 0

        def dfs(node):
            curr = node

            if self.count == k:
                return
            if curr is None:
                return
            
            dfs(node.left)

            if self.count < k:
                self.count += 1

                if self.count == k:
                    self.result = node.val
            
            dfs(node.right)
        
        dfs(root)
        return self.result
