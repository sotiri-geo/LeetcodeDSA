/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
 
// reverseN returns the new head, tail and next node after group ends
func reverseN(head *ListNode, n int) (*ListNode, *ListNode, *ListNode) {
    curr := head 
    prev := &ListNode{Next: head}
    count := 0 

    for range n {
        if curr == nil {
            break 
        }
        prev = curr
        curr = curr.Next 
        count++
    }
    
    // odd group length
    if count % 2 != 0 {
        return head, prev, curr
    }

    // Restart for even
    tail := head 
    prev = &ListNode{Next: head}
    curr = head 

    for range n {
        // exit if curr is nil pointer 
        if curr == nil {
            break
        }

        nxt := curr.Next
        curr.Next = prev 
        prev = curr 
        curr = nxt
    }
    // This makes sure that we don't kill the link
    tail.Next = curr

    return prev, tail, curr
 }


func reverseEvenLengthGroups(head *ListNode) *ListNode {
    // We need to keep the node before we perform reversal 
    sentinel := &ListNode{Next: head}
    group := 1
    prev, curr := sentinel, head

    for curr != nil {
        newHead, newTail, nxt := reverseN(curr, group)
        prev.Next = newHead
        prev = newTail
        curr = nxt
        group++
    }

    return sentinel.Next
}