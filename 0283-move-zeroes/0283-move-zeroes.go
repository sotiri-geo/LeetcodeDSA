func moveZeroes(nums []int)  {
    p2 := 0

    // idiomatic go when you only require index from array use range
    for p1 := range nums {
        if nums[p1] != 0 {
            nums[p1], nums[p2] = nums[p2], nums[p1]
            p2++
        }
    }
}