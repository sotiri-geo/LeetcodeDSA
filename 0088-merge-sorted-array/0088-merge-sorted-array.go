func merge(nums1 []int, m int, nums2 []int, n int)  {
    // Merge from the back to avoid extra allocations
    p1 := m - 1
    p2 := n - 1
    write := m + n - 1

    for p2 >= 0 {
        if p1 >= 0 && nums1[p1] > nums2[p2] {
            // largest value so far
            nums1[write] = nums1[p1] 
            p1--
        } else {
            nums1[write] = nums2[p2]
            p2--
        }
        write--
    }
}