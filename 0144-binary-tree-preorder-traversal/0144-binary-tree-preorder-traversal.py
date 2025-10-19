# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Preorder traveral is to visit the parent and then the children

            4
          /  \
        1      5

        [4, 1, 5]
        We should first make logic call in current node then recursively call left
        and right children.
        """

        if root is None:
            return []

        ans = []
        ans.append(root.val)
        # left and right calls
        ans += self.preorderTraversal(root.left)
        ans += self.preorderTraversal(root.right)

        return ans


        