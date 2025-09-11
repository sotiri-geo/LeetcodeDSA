from functools import cache
class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        """
        Top down implementation

        state variables:
        i - current job
        day - current day

        We have to complete 1 job every day, so we need to consider how many 
        we should select on a given day to have remaining jobs available on future days.

        At a given job i and day we have (d - day) remaining, so we need to stop before
        < N - (d - day) in order to give us the opportunity to select at least 1 job on remaining 
        days.

        We know that the difficulty of a day is simply the max difficulty of all jobs selected on
        that day. So if we reached day == d (last day) and there were N - j tasks left, we would need
        to select the max(jobDifficulty[k]) for j <= k < N. We could precompute this as an array 
        at the start to find this value in O(1).
        """
        # edge case, if these are more days than tasks
        job_count = len(jobDifficulty)
        if d > job_count:
            return -1



        max_difficulty_rev = [jobDifficulty[-1]]

        for i in range(len(jobDifficulty) - 2, -1, -1):
            max_difficulty_rev.append(max(max_difficulty_rev[-1], jobDifficulty[i]))

        # reverse 
        max_difficulty_rev.reverse()

        # returns the min difficulty of job schedule starting from 
        # job (i) and day (day)
        @cache
        def dp(i, day):
            # base case
            if day == d:
                # last day needs to be max difficulty of remaining jobs
                return max_difficulty_rev[i]
            
            # recurrence relation 
            remaining_days = d - day 
            upper_limit = job_count - remaining_days # must leave enough days
            
            return min(max(jobDifficulty[i: j + 1]) + dp(j + 1, day + 1) for j in range(i, upper_limit))

        return dp(0, 1)

        