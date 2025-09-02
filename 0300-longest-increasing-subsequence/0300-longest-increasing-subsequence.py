from functools import cache

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        subsequence means the nums do not need to be contiguous
        Stricly increasing means for i < j => nums[i] < nums[j]

        state variable
        index -> track where we are
        prev -> init at -inf but have this as our constraint
        """ 
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

        return dp(0, float('-inf'))
