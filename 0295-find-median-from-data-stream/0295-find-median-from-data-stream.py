import heapq

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