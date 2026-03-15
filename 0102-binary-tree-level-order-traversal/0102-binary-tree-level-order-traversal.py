from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # We need to traverse using bfs
        # To keep the level ordering
        
        # This is the edge case when the binary tree is empty
        if not root:
            return []

        queue = deque([root])
        ans = []

        while queue:
            
            row_length = len(queue)
            row = []
            for _ in range(row_length):
                top = queue.popleft()
                row.append(top.val)

                if top.left is not None:
                    queue.append(top.left)
                if top.right is not None:
                    queue.append(top.right)
                
            ans.append(row)
        return ans
