// getCommon returns the min integer value common in both nums1 and nums2
// else returns -1 if no common integer exits
func getCommon(nums1 []int, nums2 []int) int {
    p1, p2 := 0, 0

    for (p1 < len(nums1)) && (p2 < len(nums2)) {
        if nums1[p1] == nums2[p2] {
            return nums1[p1]
        }
        if nums1[p1] < nums2[p2] {
            p1++
        } else {
            p2++
        }
    }

    return -1
}