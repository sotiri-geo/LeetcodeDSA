class Solution:
    def maximumLengthOfRanges(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums)
        nums.append(float('inf'))
        stack = []
        for i, num in enumerate(nums):
            while stack and nums[stack[-1]] < num:
                j = stack.pop()
                res[j] = i - stack[-1] - 1 if stack else i
            stack.append(i)
        return res
        