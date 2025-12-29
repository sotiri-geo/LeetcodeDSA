/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func isPalindrome(head *ListNode) bool {
    // assign values into an array 
    var values []int

    // Idiomatic go code for iterating across linkedList
    for curr := head; curr != nil; curr = curr.Next {
        values = append(values, curr.Val)
    }

    // Use two pointers to validate palindrome
    for i, j := 0, len(values) - 1; i < j; i, j = i + 1, j - 1 {
        if values[i] != values[j] {
            return false
        }
    }

    return true
}