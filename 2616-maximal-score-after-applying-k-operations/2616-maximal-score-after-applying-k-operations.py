import heapq
import math

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        score = 0

        # max_heap
        heap = [-n for n in nums]

        heapq.heapify(heap)

        while k > 0:
            top = heapq.heappop(heap)
            score += -top
            replace = math.ceil(-top / 3)
            heapq.heappush(heap, -replace)
            k -= 1
        
        return score



        