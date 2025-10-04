class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        Two pointer to track both the size of the array and whether the constraint is fulfuilled.
        In the event the constraint is broken, we need to fix it within inner loop.
        """
        left = right = 0 
        min_length = float('inf')
        curr_sum = 0

        for right in range(len(nums)):
            curr_sum += nums[right]

            while left <= right and curr_sum >= target:
                # move left pointer forward to minimise subarray size
                # Always a valid constraint in this block as
                # curr_sum >= target
                min_length = min(min_length, right - left + 1)
                # remove from left
                curr_sum -= nums[left]
                left += 1
        
        return min_length if min_length != float('inf') else 0
            