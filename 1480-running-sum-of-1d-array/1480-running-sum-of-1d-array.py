class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        """ 
        The running sum, we need a prefix sum
        """
        prefix = [0]

        for i in range(len(nums)):
            prefix.append(prefix[i] + nums[i])

        return prefix[1:]