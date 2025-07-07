import heapq

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        """
        we need to first pick the earliest day by sorting
        
        Then for a given day we need to push all those that start today 
        Then we pop those that are expired. Then attent one event today.
        """
        events.sort()
        heap = [] # sorted by end day, always take the latest end day so far
        day = i = ans = 0
        n = len(events)

        while i < n or heap:
            
            while i < n and events[i][0] <= day:
                # push to heap end day
                heapq.heappush(heap, events[i][1])
                i += 1
            
            # pop any expired days
            # This would happen when you have too many overlapping events e.g.
            # [1,2], [1,2], [1,2] <- one of these would get dropped
            while heap and heap[0] < day:
                heapq.heappop(heap)
            
            if heap:
                # take one
                heapq.heappop(heap)
                ans += 1

            day += 1

        return ans 
            