# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # We want to insert the value such that we keep the property of the
        # binary tree.
        # So we have either a value between current and left node. Or we have value 
        # between current and right node. We will need to inspect and recreate
        
        def dfs(node):
            if not node:
                return TreeNode(val)

            # Case where not leaf node
            if val < node.val:
                node.left = dfs(node.left)
            if val > node.val:
                node.right = dfs(node.right)
            return node
        
        return dfs(root)