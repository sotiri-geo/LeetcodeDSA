/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func swapNodes(head *ListNode, k int) *ListNode {
    // perform a single loop and find the Kth value and the
    // N - Kth value. Lets try do this in a single path

    sentinel := &ListNode{Next: head}
    prev := sentinel
    curr := head
    var beginning *ListNode
    position := 1
    
    for curr != nil {
        if position == k {
            beginning = curr
        }
        if position >= k {
            prev = prev.Next
        }
        curr = curr.Next
        position++
    }

    end := prev 

    // swap 
    beginning.Val, end.Val = end.Val, beginning.Val
    return sentinel.Next
}