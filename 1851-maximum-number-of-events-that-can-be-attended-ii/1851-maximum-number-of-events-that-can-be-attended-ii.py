from functools import cache
class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        """
        Aim to sort the events by start and end time
        then we need to somehow figure out how to pick the best event
        with a limit of k.

        The key to using dynamic programming would be if we consider the current
        event or skip it and then have the option of taking another event.
        """
        
        events.sort(key=lambda x: x[0])

        n = len(events)

        def bs(idx):
            """finds the next accepted events index based off the current
            index end date."""
            left = idx + 1
            right = n
            # end date. needs to be next start date
            target = events[idx][1]


            while left < right:
                mid = (left + right) // 2
                if events[mid][0] <= target:
                    left = mid + 1
                else:
                    right = mid
            return left
            

        @cache
        def dp(i, count):
            if i == n or count == 0:
                return 0

            # search end time with binary search with the next start date 
            # following the end time of the current event being on left
            skip = dp(i + 1, count)
            
            next_idx = bs(i)
            take = events[i][2] + dp(next_idx, count - 1)
            return max(take, skip)

        return dp(0, k)

            