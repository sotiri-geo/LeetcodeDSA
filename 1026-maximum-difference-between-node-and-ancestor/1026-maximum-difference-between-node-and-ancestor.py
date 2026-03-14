# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        ans = 0

        # We need to traverse down the tree whist holding 
        # the max we've seen so far
        
        ans = 0

        def dfs(node, mx, mn):
            nonlocal ans
            if not node:
                return 

            mx = max(mx, node.val)
            mn = min(mn , node.val)
            ans = max(ans, abs(mx - mn))
            left = dfs(node.left, mx, mn)
            right = dfs(node.right, mx, mn)
            
        dfs(root, float('-inf'),float('inf'))
        return ans
