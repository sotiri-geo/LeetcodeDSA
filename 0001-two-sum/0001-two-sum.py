class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        We can actually go from the reverse and have a mapping defined st

        val -> index

        We can guarentee this because there exists only one solution
        """
        seen = {}

        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in seen:
                cidx = seen[compliment]
                return [i, cidx] 
            
            seen[nums[i]] = i