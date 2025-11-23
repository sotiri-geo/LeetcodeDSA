func moveZeroes(nums []int)  {
   // We need to maintain two pointer  
   // We always perform a swap with p1 and p2 but p2 always needs to point 
   // to a zero value to guarentee at the end of walking through array, all zeros are moved 
   // to the end. 
   // potential edge case [0,0,1,2] we end up [1,0,0,2] and p1 points at index 2. 

   p1, p2 := 0, 0

   for p1 < len(nums) {
      if nums[p1] != 0 {
            // perform a swap
            nums[p1], nums[p2] = nums[p2], nums[p1]
            p1++
            p2++
      } else {
        // only move p1 forward in an attemp to find the first non-zero number
        // to perform a swap. This will keep p2 always pointing at a zero value or if there are no 
        // zero values then it will just perform swaps in place.
        p1++
      }
   }
}