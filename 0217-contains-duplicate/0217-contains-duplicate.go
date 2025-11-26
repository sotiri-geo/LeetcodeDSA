// containsDuplicate returns true if there exists at least one num in nums 
// such that it is repeated two or more times.
func containsDuplicate(nums []int) bool {
    seen := map[int]struct{}{}

    for _, num := range nums {
        if _, exists := seen[num]; exists {
            return true
        }
        seen[num] = struct{}{}
    }
    return false
}