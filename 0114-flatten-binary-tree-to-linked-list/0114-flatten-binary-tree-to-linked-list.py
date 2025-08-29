# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        ordered = []

        def dfs(node):
            nonlocal ordered
            if not node:
                return 
            
            ordered.append(node)
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        # change order
        for i in range(len(ordered) - 1):
            curr_node, next_node = ordered[i], ordered[i + 1]
            curr_node.right = next_node
            curr_node.left = None

        