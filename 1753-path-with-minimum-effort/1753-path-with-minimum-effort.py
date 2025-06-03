from collections import defaultdict
import heapq

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        """
        create a weight graph where the cells represent nodes and the
        edges represent the absolute diff between heights of two consecutive
        cells.

        Always take the min seen so far. Then the min effort required will be 
        what we see from the end node (rows - 1, cols - 1). We always maintain smallest
        we've seen. You can also do this with binary search.
        """

        # create graph
        graph = defaultdict(list)
        rows = len(heights)
        cols = len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        def is_valid(x, y):
            return 0 <= x < rows and 0 <= y < cols

        def get_neighbours_and_weights(x, y):
            nei = []
            for dx, dy in directions:
                new_x = x + dx
                new_y = y + dy
                if is_valid(new_x, new_y):
                    weight = abs(heights[x][y] - heights[new_x][new_y])
                    nei.append((new_x, new_y, weight))
            return nei

        for i in range(rows):
            for j in range(cols):
                graph[(i, j)] += get_neighbours_and_weights(i, j)
        
        
        diff = [[float('inf') for _ in range(cols)] for _ in range(rows)]

        diff[0][0] = 0

        # min heap (diff in heights, x, y)
        heap = [(0, 0, 0)]

        while heap:
            d, x, y = heapq.heappop(heap)

            # Optimisation step
            if d > diff[x][y]:
                continue
            
            for nei_x, nei_y, effort in graph[(x, y)]:
                # The maximum abs diff between any two cells on the path
                # we need to keep track of this
                new_effort = max(d, effort)
                if new_effort < diff[nei_x][nei_y]:
                    diff[nei_x][nei_y] = new_effort
                    heapq.heappush(heap, (new_effort, nei_x, nei_y))

        return diff[rows - 1][cols - 1]




