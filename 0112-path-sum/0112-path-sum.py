# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # We need to traverse to the root node whilst keeping track of 
        # current sum. Then when we are at a leaf node we can assert if our 
        # current sum is equal to targetSum

        def dfs(node, curr):
            if not node:
                return False
            
            # Check leaf node 
            if node.left is None and node.right is None:
                return curr + node.val == targetSum

            curr += node.val

            left = dfs(node.left, curr)
            right = dfs(node.right, curr)

            return left or right

        return dfs(root, 0)
        