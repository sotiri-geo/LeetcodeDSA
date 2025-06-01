import heapq
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        We need to create a min heap to manage the next smallest head value from all the
        linked lists and add them to sentinel. 

        We first need to do an iteration across all list members and as we pop off
        we need to remove head
        """
        sentinel = ListNode()
        heap = []

        for i in range(len(lists)):  
            ll = lists[i]
            # Could be empty
            if ll:
                # Adding head of ll to recognise the next smallest
                heapq.heappush(heap, (ll.val, i))
        
        curr = sentinel
        # Now we have a min heap we can start popping and adding
        while heap:
            val, idx = heapq.heappop(heap)
            # add to sentinel
            # remove head from ll
            curr.next = lists[idx]
            # Move pointer
            curr = curr.next
            lists[idx] = lists[idx].next
            # Add the next node in linked list if not empty
            if lists[idx] is not None:
                heapq.heappush(heap, (lists[idx].val, idx))
        return sentinel.next


        