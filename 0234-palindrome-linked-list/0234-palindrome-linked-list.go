
import (
	"fmt"
	"slices"
)

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func isPalindrome(head *ListNode) bool {
    // assign values into an array 
    values := []int{}

    curr := head 

    for curr != nil {
        values = append(values, curr.Val)
        curr = curr.Next
    }
    i := 0
    for _, revVal := range slices.Backward(values) {
        if revVal != values[i] {
            return false
        }
        i++ 
    }

    return true
}