# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # edge case of empty tree
        if not root:
            return []
        stack = []
        ans = []
        stack.append(root)

        while stack:
            top = stack.pop()
            ans.append(top.val)
            # append right elements first so that they come last
            # stack is a LIFO 
            if top.right:
                stack.append(top.right)
            if top.left:
                stack.append(top.left)

        return ans

