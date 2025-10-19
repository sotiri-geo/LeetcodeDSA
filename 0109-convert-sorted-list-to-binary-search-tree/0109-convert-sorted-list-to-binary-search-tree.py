# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        """
        Convert first the LL into a list and then apply the normal procedure
        of transforming a sorted list into a BST.
        """

        nums = []

        while head:
            nums.append(head.val)
            head = head.next

        # edge case of empty linkedlist
        if len(nums) == 0:
            return

        def convert(nums):
            if len(nums) == 0:
                return 
            
            # centre of bst from a sorted array is its middle element 
            mid = len(nums) // 2
            node = TreeNode(nums[mid])

            node.left = convert(nums[:mid])
            node.right = convert(nums[mid + 1:])

            return node

        return convert(nums)

        