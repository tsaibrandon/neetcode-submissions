# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        create an output empty list
        create an empty deque

        if root is None:
            return output

        while deque is not empty:
            create another empty list

            for i in range of the lengthe of deque:
                if left is not None:
                    add the left nodes of the first value in the deque
                if right is not None:
                    add the right nodes of the first value in the deque
                
                pop left and add the value to the list

            append the list to the output list

        return the output
        """

        output = []
        q = deque()

        if root is None:
            return output

        q.append(root)
        
        while q:
            level = []

            for _ in range(len(q)):
                curr = q.popleft()

                if curr.left is not None:
                    q.append(curr.left)
                if curr.right is not None:
                    q.append(curr.right)

                level.append(curr.val)

            output.append(level)

        return output