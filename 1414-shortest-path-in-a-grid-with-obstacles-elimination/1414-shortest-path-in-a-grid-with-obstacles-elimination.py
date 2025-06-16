import heapq

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        """
        Lets try optimise with manhatten distance for heuristics 
        and use A* algorithm to optimise bfs
        (0, 0) -> (m - 1, n - 1)

        Need to keep track of k to see if we can remove an obsticle
        """
        m = len(grid)
        n = len(grid[0])
        start = (0, 0)
        target = (m - 1, n - 1)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def is_valid(x, y):
            return 0 <= x < m and 0 <= y < n

        def heuristic(x, y):
            # manhatten distance
            return abs(x - target[0]) + abs(y - target[1])
        # (f = g + h, g, k, (x, y))
        heap = [(heuristic(start[0], start[1]), 0, k, (0, 0))]

        seen = set()

        while heap:

            f, g, k, (x, y) = heapq.heappop(heap)

            if (x, y) == target:
                return g
            
            # optimisation step: visited before at a smaller g
            if (x, y, k) in seen:
                continue

            # Add only when exploring node as A* algo implies shortest g to this point
            seen.add((x, y, k))
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                # Only walk over obsticle if we have k > 0
                if is_valid(nx, ny):
                    f = heuristic(nx, ny) + g + 1
                    if k > 0 and grid[nx][ny] == 1:
                        heapq.heappush(heap, (f, g + 1, k - 1, (nx, ny)))
                    elif grid[nx][ny] == 0:
                        heapq.heappush(heap, (f, g + 1, k, (nx, ny)))
        
        return -1 




