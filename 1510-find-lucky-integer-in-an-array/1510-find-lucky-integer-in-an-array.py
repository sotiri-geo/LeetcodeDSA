class Solution:
    def findLucky(self, arr: List[int]) -> int:
        """
        We can do this in one pass by maintaining both a counter and a max
        """

        counter = {}
        ans = -1 

        for num in arr:

            counter[num] = counter.get(num, 0) + 1

        
        # do a second pass
        for key, value in counter.items():
            if key == value:
                ans = max(ans, key)

        return ans


        