from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        Each interval can either be idle or allow completion of a single task. 
        i.e. no parallel workstreams.

        Constraint: gap of at least n intervals between two tasks with same label
        so
        A _ _ A _ _ A
        """

        # greedy and pick the highest frequency
        counter = Counter(tasks)
        # consider only the frequency on a max heap, we don't care about task name
        heap = [-val for val in counter.values()]

        heapq.heapify(heap)

        # (time_ready, frequency) -> time_ready = time + n + 1 (i.e next time we can 
        # use it)
        cooldown_q = deque()

        time = 0

        while heap or cooldown_q:
            # check cooldown queue to see if we can add any back to heap
            if cooldown_q and cooldown_q[0][0] <= time:
                t, val = cooldown_q.popleft()
                heapq.heappush(heap, val)
            if heap:
                val = heapq.heappop(heap)
                if -val > 1:
                    # need to cooldown
                    cooldown_q.append((time + n + 1, val + 1))
            time += 1

        return time



            


