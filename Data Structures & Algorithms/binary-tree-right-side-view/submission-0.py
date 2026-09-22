# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        create an output list
        create an empty deque

        if root is None:
            return output
        
        append the root node to the q

        while q is not empty:
            for _ in the range of the q:
                curr = q.popleft()

                if curr.left is not None:
                    append the left node
                if curr.right is not None:
                    append the right node
                
            append curr.val to output list

        return output
        """

        output = []
        q = deque()

        if root is None:
            return output

        q.append(root)

        while q:
            for _ in range(len(q)):
                curr = q.popleft()

                if curr.left is not None:
                    q.append(curr.left)
                if curr.right is not None:
                    q.append(curr.right)
                
            output.append(curr.val)
        
        return output