# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """We can identify a leaf node if it had null children"""
        ans = 0

        def dfs(node, depth):
            nonlocal ans
            if not node:
                ans = max(ans, depth)
                return 

            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 0)
        return ans