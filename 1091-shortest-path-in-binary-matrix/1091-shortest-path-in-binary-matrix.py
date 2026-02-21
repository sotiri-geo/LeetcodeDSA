from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        """
        As we are attempting to find the shortest path between two points
        it makes sense to use BFS, so that we can count each 'wave' of steps 
        we need to make. When we first see the bottom right cell, we can guarentee
        that we arrived there at the min no. of steps.
        """
        # Unachievable as we can only traverse on cells with value 0
        if grid[0][0] == 1:
            return -1 
        start = (0, 0)
        n = len(grid)
        seen = set()
        queue = deque([start])
        # Why?
        # We are adding start position to seen. We know that the first time we visit
        # the cell as we are using bfs, we would have reached it with the minimum no. steps
        # hence we can disregard the node the next time we see it as we only care about the 
        # minimum no. of steps from point A -> B.
        seen.add(start)
        count = 1 # first cell counts as 1 
        # 8 directionally connected
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (-1, -1), (1, -1)]

        def is_valid(x, y):
            """Returns true if x, y in boundary and cell is traversable"""
            return 0 <= x < n and 0 <= y < n and grid[x][y] == 0
        # Time complexity is O(N + E) when N no. nodes and E no. edges
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if node == (n - 1, n - 1):
                    return count

                # In a single go, we look at all the nodes neighbours
                for dx, dy in directions:
                    nx, ny = node[0] + dx, node[1] + dy
                    if is_valid(nx, ny) and (nx, ny) not in seen:
                        # we can explore 
                        seen.add((nx, ny))
                        queue.append((nx, ny))
                # We've traversed one layer, we can increment count
            count += 1
        
        return -1 


