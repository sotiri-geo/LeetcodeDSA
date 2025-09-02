class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        Attempting to use binary search with keeping a mono inc stack
        called sub, which tracks the increasing subsequence.
        """
        # [2, 5, 6] - 4
        def bs(sub: list[int], num: int) -> int:
            left = 0 
            right = len(sub)
            while left < right:
                mid = (left + right) // 2
                if sub[mid] < num:
                    left = mid + 1
                else:
                    # this means righ will always hold the lowerbound
                    # i.e the value st sub[right] >= num
                    right = mid            
            return left
            

        sub = []

        for num in nums:
            if not sub or sub[-1] < num:
                sub.append(num)
                continue
            
            # find the index to replace value
            # OLog(N)
            idx = bs(sub, num)
            prev = sub[idx]
            sub[idx] = num # replace
        return len(sub)

