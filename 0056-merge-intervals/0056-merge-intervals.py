class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Consider two points

        i - 1, i 

        [[1,3],[2,6],[6,10],[15,18]]



        end(i - 1) >= start(i) -> merge these intervals
        """
        intervals.sort() # assume not sorted
        ans = [intervals[0]]
        
        for i in range(1, len(intervals)):
            top_s, top_e = ans[-1]
            curr_s, curr_e = intervals[i]
            if top_e >= curr_s:
                # merge 
                ans[-1] = [top_s, max(top_e, curr_e)]
            else:
                ans.append(intervals[i])
        
        return ans
