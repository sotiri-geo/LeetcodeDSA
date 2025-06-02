from collections import Counter
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        Suppose that we look at the time till we can next process a char.
        We need to manage the following state variables:

        Frequency of tasks A-Z
        Some way to find out how many intervals has passed since the last task
        has been processed and see if we can select it.

        We can use that as a means of tracing back when it was last run. We assume at time
        t we push every character with their frequency on a heap.

        We can sort heap based off time interval which we track t = 1, t = 2 etc
        then we decrement the count of the task and only add back to the heap if count > 0.

        This is a greedy approach because we don't specifically choose a character based on any other
        property but its count. If multiple characters can be selected we just pick the first in heap.
        """

        
        counter = Counter(tasks)

        # heap needs to track time since last run 
        heap = [(0, count, task) for task, count in counter.items()]

        # Linear time
        heapq.heapify(heap)

        time = 0
        # Could we add the next time its allowed to run i.e. curr_time + n
        # We track time independently, so when time >= time_next_run we can process this

        while heap:
            time_next_run, count, task = heapq.heappop(heap)

            # process and decrement by 1
            if time >= time_next_run:
                if count - 1 > 0:
                    heapq.heappush(heap, (time_next_run + n + 1, count - 1, task))
            else:
                # ignore and let time elapse
                heapq.heappush(heap, (time_next_run, count, task))
            
            time += 1

        # Once all tasks have been exhausted in heap then return time
        return time

