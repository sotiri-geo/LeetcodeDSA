# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        preorder we get the parent first before the children. So to identify parent 
        we first need to use the preorder. Then find that value in the inorder map
        and every value to the left of it will be in the left subtree and every value
        to the right will be in the right subtree.
        
        preorder = [3, 9, 20]
        inorder = [9, 3, 20]

        3 -> left sub tree starts at 9 
        """
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        preorderIdx = 0
        def dfs(left, right):
            nonlocal preorderIdx

            if left > right:
                return None
            
            rootValue = preorder[preorderIdx]
            root = TreeNode(rootValue)

            preorderIdx += 1
            # Get the index value of the inorder value
            inorderIdx = inorder_map[rootValue]
            # left side of inorder is left subtree, right side is right subtree
            root.left = dfs(left, inorderIdx - 1)
            root.right = dfs(inorderIdx + 1, right)

            return root
        
        return dfs(0, len(preorder) - 1)