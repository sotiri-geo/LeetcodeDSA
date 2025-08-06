# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        We need to group k elements together. 

        We need to solve the problem of reversing. Then solve the problem of attaching
        them to separate groups. Means we need a pointer to the first value in the group
        cause this will be the last value after reversing and then well need to attach it
        """

        def reverse(head, k):
            """Reversing k nodes and returns the new last node"""
            curr = last = head
            prev = None

            while k > 0:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
                k -= 1

            first = prev
            return first, last , curr
        
        curr = head
        total_nodes = 0
        while curr:
            curr = curr.next
            total_nodes += 1

        # base case
        if total_nodes < k:
            return head
        
        # init reverse
        first, last, nxt = reverse(head, k)
        sentinel = ListNode()
        sentinel.next = first

        for _ in range(1, total_nodes // k):
            f, l, n = reverse(nxt, k)
            last.next = f
            # update vars
            first = f
            last = l
            nxt = n

        # attach rest if k not a direct multiple 
        if nxt:
            last.next = nxt
        return sentinel.next
        

        

        
        