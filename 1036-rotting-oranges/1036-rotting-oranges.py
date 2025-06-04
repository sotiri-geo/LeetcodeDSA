from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        This looks like a bfs algo because we need to view this 
        grid where each cell is a node and 4 directionally across 
        each cell as edges. 

        We know that if we apply bfs starting at any rotton orange
        and traverse then when we have no more rotton oranges we know we
        would have the minimum time.
        """
        m = len(grid)
        n = len(grid[0])
        queue = deque()
        fresh_orange_count = 0
        # How do we start? we need to grab all the rotton oranges
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                if grid[i][j] == 1:
                    fresh_orange_count += 1

        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        # First round of rotton oranges isn't considered
        time = 0 

        def is_valid(row, col):
            return 0 <= row < m and 0 <= col < n

        # Key thing here is that we only iterate if we still have fresh oranges
        # to avoid overcounting the time
        while queue and fresh_orange_count > 0:

            # tracking rotton oranges at every given minute
            for _ in range(len(queue)):
                rotton = queue.popleft()
                old_row, old_col = rotton
                # move directionaly
                for dx, dy in directions:
                    new_row = dx + old_row
                    new_col = dy + old_col
                    if is_valid(new_row, new_col) and grid[new_row][new_col] == 1:
                        # make that orange rotton and explore neighbours
                        grid[new_row][new_col] = 2
                        queue.append((new_row, new_col))
                        fresh_orange_count -= 1
            time += 1
        
        return time if fresh_orange_count == 0 else -1