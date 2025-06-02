import heapq

"""
We always want to maintain the middle

Two heaps, the min heap is on the right, max heap on the left

max heap ---- min heap

   3 6   ----  6 7

when its odd we always take the value from the larger heap i.e. min or max heap

7 - 6
"""

class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        self.size = 0

    def addNum(self, num: int) -> None:
        self.size += 1
        if not self.min_heap:
            heapq.heappush(self.min_heap, num)
        elif not self.max_heap:
            heapq.heappush(self.max_heap, -num)
        else:
            # both have values
            if num < self.min_heap[0]:
                # move to left
                heapq.heappush(self.max_heap, -num)
            else:
                heapq.heappush(self.min_heap, num)
            self.sort_heaps()
            
        self.resize_heaps()
        
    def sort_heaps(self):
        # compare top and bottom: O(1)
        left = -self.max_heap[0]
        right = self.min_heap[0]
        if left > right:
            # pull right to left
            left = -heapq.heappop(self.max_heap) 
            heapq.heappush(self.min_heap, left)
        elif right < left:
            right = heapq.heappop(self.min_heap) 
            heapq.heappush(self.max_heap, -right)

    def resize_heaps(self):
        if len(self.min_heap) > len(self.max_heap) + 1:
            val = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -val)
        elif len(self.max_heap) > len(self.min_heap) + 1:
            val = heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, -val)

    def findMedian(self) -> float:
        if self.size % 2 == 0:
            # middle value
            left = -self.max_heap[0]
            right = self.min_heap[0]
            return (left + right) / 2
        else:
            if len(self.min_heap) > len(self.max_heap):
                return self.min_heap[0]
            else:
                return -self.max_heap[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()