import heapq

"""
minH - 3 4

maxH - 2

Goal is to start from the left side, then move it right, then only pop off the smallest element from min heap (right side) if the right side is bigger. This way we always know when there an odd number of elements, the median is the root of the max heap
"""

class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.max_heap, -num)

        # balancing step, add to min heap
        heapq.heappush(self.min_heap, -self.max_heap[0])
        heapq.heappop(self.max_heap)

        # if we've added too much to the right, we balance size
        if len(self.min_heap) > len(self.max_heap):
            # maintain size
            heapq.heappush(self.max_heap, -self.min_heap[0])
            heapq.heappop(self.min_heap)

        

    def findMedian(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            # odd number
            return -self.max_heap[0]
        left = -self.max_heap[0]
        right = self.min_heap[0]
        return (left + right) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()