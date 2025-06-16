import heapq

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        """
        Optimise BFS using A* algo 

        source top left, goal bottom right. We can perform the a* algo in one step.
        Rather than other algos where we need to sort the input and compute shortest 
        step between.

        We need to compute f = g + h
        g = previous step
        h = heuristic estimation from current node to goal
        """
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]
        n = len(grid)
        goal = (n - 1, n - 1)
        # edge case, possible start and possible end
        if grid[0][0] != 0 or grid[n - 1][n - 1] != 0:
            return -1

        def is_valid(x, y):
            return 0 <= x < n and 0 <= y < n and grid[x][y] == 0

        def heuristic(source_x, source_y):
            """A metric to measure closeness. Chebyshev distance"""
            dest_x, dest_y = goal
            return max(abs(dest_x - source_x), abs(dest_y - source_y))

        

        # (f = g + h, g, x, y)
        # g = 1 treat the first step as a path of length 1
        # heuristic -> calculates the estimated cost to reach from current node to goal.
        heap = [(1 + heuristic(0, 0), 1, 0, 0)]
        seen = set()

        while heap:
            f, g, x, y = heapq.heappop(heap)
            if (x, y) == (n - 1, n - 1):
                return g
            
            # optimisation step: if we've seen then skip
            if (x, y) in seen:
                continue
            
            seen.add((x, y))

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if is_valid(nx, ny):
                    heapq.heappush(heap, (
                        g + 1 + heuristic(nx, ny), g + 1, nx, ny
                    ))

        return -1



