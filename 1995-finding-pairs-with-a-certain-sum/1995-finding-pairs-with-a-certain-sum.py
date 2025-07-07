from collections import Counter
class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self._counter = Counter(nums2)
        

    def add(self, index: int, val: int) -> None:
        # increment index
        prev = self.nums2[index]
        new = prev + val
        self.nums2[index] += val
        # Keep track of hashmap counter
        self._counter[prev] = max(self._counter[prev] - 1, 0) # bound below at 0
        self._counter[new] = self._counter.get(new, 0) + 1
        

    def count(self, tot: int) -> int:
        resp = 0
        # O(N) where N is the size of nums1
        for num in self.nums1:
            find = tot - num
            # We need to keep track of the number of times the desired compliment is seen
            if find in self._counter:
                resp += self._counter[find]
        return resp
        


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)