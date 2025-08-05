# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        We need to add the two numbers and then carry. Also we need to consider the scenario
        when they are not equal lengths.
        """
        sentinel = ListNode()

        curr = sentinel 

        carry = 0

        while l1 and l2:
            total = l1.val + l2.val + carry
            next_node = ListNode(val=total % 10)
            curr.next = next_node
            carry = total // 10

            # walk to next node
            curr = curr.next
            l1 = l1.next
            l2 = l2.next

        # Need to exhaust remaining nodes if applicable
        # only one of these expressions will be true
        while l1:
            total = l1.val + carry 
            next_node = ListNode(val=total % 10)
            curr.next = next_node
            carry = total // 10

            curr = curr.next
            l1 = l1.next
            
        while l2:
            total = l2.val + carry 
            next_node = ListNode(val=total % 10)
            curr.next = next_node
            carry = total // 10

            curr = curr.next
            l2 = l2.next

        if carry:
            # one more 1
            curr.next = ListNode(val=1)
            
        return sentinel.next
            
