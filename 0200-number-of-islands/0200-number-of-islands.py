from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Implement a bfs algo
        """
        
        # explore each component

        islands = 0
        queue = deque()
        seen = set()
        m, n = len(grid), len(grid[0])

        def is_valid(x, y):
            return 0 <= x < m and 0 <= y < n and grid[x][y] == "1"

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def bfs(x, y):
            queue = deque()
            queue.append((x, y))
            
            while queue:
                currx, curry = queue.popleft()
                for dx, dy in directions:
                    new_pnt = (dx + currx, dy + curry)
                    if new_pnt not in seen and is_valid(new_pnt[0], new_pnt[1]):
                        seen.add(new_pnt)
                        queue.append(new_pnt)

            return 1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (i, j) not in seen:
                    islands += bfs(i, j)

        return islands