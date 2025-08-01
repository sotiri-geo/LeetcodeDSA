class NumArray:

    def __init__(self, nums: List[int]):
        # O(N + 1)
        self._prefix = [0]
        for num in nums:
            self._prefix.append(num + self._prefix[-1])
        

    def sumRange(self, left: int, right: int) -> int:
        return self._prefix[right + 1] - self._prefix[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)