class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        We need to do a modulo len(nums) with k. Because if k 
        is greater than len(nums) we need to go round again.
        """
        shift = k % len(nums)
        # No rotation required
        if shift == 0: 
            return

        nums[:-shift], nums[-shift:] = nums[-shift:], nums[:-shift]