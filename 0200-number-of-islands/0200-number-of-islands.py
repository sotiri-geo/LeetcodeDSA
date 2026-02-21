from collections import defaultdict

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        We look at the islands as connected components with 
        each section of the grid == 1 as a node.

        Returning the no. of islands is equivalent to returning
        the number of connected components.

        The input is not an adj matrix, we need to traverse the 
        grid, we start at a given point, and if its '1' then we 
        can then look left, right, up, down
        """

        graph = defaultdict(list)
        n, m = len(grid), len(grid[0])

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def is_valid(x, y):
            """Returns true if x, y within boundaries and is land"""
            return 0 <= x < n and 0 <= y < m and grid[x][y] == "1"

        # explore component
        def dfs(node):

            for dx, dy in directions:
                nei = node[0] + dx, node[1] + dy
                if is_valid(nei[0], nei[1]) and nei not in seen:
                    seen.add(nei)
                    dfs(nei)
        
        seen = set()
        islands = 0
        # O(N*M) time complexity
        for i in range(n):
            for j in range(m):
                if is_valid(i, j) and (i, j) not in seen:
                    islands += 1
                    seen.add((i, j))
                    dfs((i, j))

        return islands



        
                    
        