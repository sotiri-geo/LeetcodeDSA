class Solution:
    def maximumLengthOfRanges(self, nums: List[int]) -> List[int]:
        """
        Default to each element being a max in at a subarray containing itself.
        Then we can decide to update based of mono stack.

        If we construct a decreasing mono stack we know the largest value we've seen
        is at the bottom of stack.

        The trick is to calculate the range for each element that gets popped off.

        As we pop an element j off the stack if the stack is non empty, the top of stack 
        should contain a value nums[stack[-1]] > nums[j] (as its monotonic decreasing) and we know 
        the value nums[i] is greater than nums[j] as well. So here we found its bound for the
        subarray for which nums[j] is maximal.

        nums[stack[-1]] > nums[j]
        nums[i] > nums[j]

        bounded to left = stack[-1]
        bounded to right = i

        subarray size = i - stack[-1] - 1

        Edge case is when there is no element left on the stack after we pop, hence its maximal
        up to i.
        """
        res = [1]*len(nums)
        nums.append(float('inf'))
        stack = []
        for i, num in enumerate(nums):
            while stack and nums[stack[-1]] < num:
                j = stack.pop()
                res[j] = i - stack[-1] - 1 if stack else i
            stack.append(i)
        return res
        