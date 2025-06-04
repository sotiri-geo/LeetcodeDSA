class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        """
        Sort and merge

        [[10,16],[2,8],[1,6],[7,12]]
        
        [[1,6],[2,4],[7,12],[10,16]]
        [[2,6],[10,12]]
        """
        
        points.sort()
        ans = [points[0]]

        for i in range(1, len(points)):
            top_s, top_e = ans[-1]
            curr_s, curr_e = points[i]

            if top_e >= curr_s:
                start = max(top_s, curr_s)
                end = min(top_e, curr_e)
                ans[-1] = [start, end]
            else:
                ans.append(points[i])
        
        return len(ans)

