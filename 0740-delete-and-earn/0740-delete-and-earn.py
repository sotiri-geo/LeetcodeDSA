from collections import Counter
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        # sort points for points[v] = v * count[v]
        points = [0] * (max(nums) + 1)
        counter = Counter(nums)
        # fill in points
        for k, v in counter.items():
            points[k] = k * v
        # edge cases
        if not nums:
            return 0
        if len(points) == 1:
            return points[0]

        # Now similar to house robber problem
        dp = [0] * len(points)
        dp[0] = points[0]
        dp[1] = max(points[0], points[1]) # better of the two
        
        for i in range(2, len(points)):
            # recurrence relation
            # either skip (take prev) or take current
            dp[i] = max(dp[i - 1], dp[i - 2] + points[i])
            
        return dp[-1]

