from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Create a graph and then make it cyclical in order to find connected component 
        and the size of the connected component.
        """
        nodes = set(nums)
        
        def findRoot(num):
            if num - 1 not in nodes:
                return num
            return findRoot(num - 1)

        def findLongest(num):
            if num not in nodes:
                return 0
            seen.add(num)
            return 1 + findLongest(num + 1)

        seen = set()
        ans = 0

        for num in nums:
            if num not in seen:
                root = findRoot(num)
                ans = max(ans, findLongest(root))
        
        return ans

