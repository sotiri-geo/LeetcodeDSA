class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        left = 0
        ans = float('inf')
        curr = 0
        for right in range(len(nums)):
            curr += nums[right]
            while curr >= target:
                ans = min(right - left + 1, ans)
                curr -= nums[left]
                left += 1
        
        return ans if ans != float('inf') else 0
         