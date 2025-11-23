func getCommon(nums1 []int, nums2 []int) int {
    // Define a pointer at the start of both slices
    p1, p2 := 0, 0

    // We need to traverse both slices from the start
    for (p1 < len(nums1)) && (p2 < len(nums2)) {
        if nums1[p1] == nums2[p2] {
            // We have found min int common it both so return
            return nums1[p1]
        }
        if nums1[p1] < nums2[p2] {
            // inc p1   
            p1++
            continue
        }
        // Else we need to increment p2
        p2++
    }

    // If we cannot find a common min int in both arrays
    return -1
}