# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        """
        We need to leverage the fact this is a binary search tree.

        leftChild < parent < rightChild

        Makes sense to compare children against parent. 
        """

        ordered = []

        def dfs(node):
            nonlocal min_diff
            if not node:
                return 

            # traverse tree
            dfs(node.left)
            ordered.append(node.val)
            dfs(node.right)

        dfs(root)
        min_diff = float('inf')

        for i in range(1, len(ordered)):
            min_diff = min(min_diff, abs(ordered[i] - ordered[i - 1]))
        return min_diff

        