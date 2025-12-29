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

    curr := head
    var beginning, end *ListNode
    position := 1
    
    for curr != nil {
        if position == k {
            beginning = curr
            end = head // start tracking from head
        } else if beginning != nil {
            end = end.Next
        }
        curr = curr.Next
        position++
    }

    // swap 
    beginning.Val, end.Val = end.Val, beginning.Val
    return head
}