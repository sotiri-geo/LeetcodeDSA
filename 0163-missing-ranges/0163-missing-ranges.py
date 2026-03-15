class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        # We know that nums is sorted 
        # Base case
        ans = []
        if not nums:
            ans.append([lower, upper])
            return ans
        
        
        if lower < nums[0]:
            ans.append([lower, nums[0]-1])

        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] > 1:
                ans.append([nums[i-1]+1,nums[i]-1])
        
        # Handle the case where we have a gap at the end
        if nums[-1] < upper:
            ans.append([nums[-1]+1, upper])

        return ans