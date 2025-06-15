from collections import deque
class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        """
        The goal is to use the bfs algorithm to find the minimum from one tree to the next
        then sum the number of steps it takes to reach the last tree.

        We need to first sort the trees in order to find source -> destination
        """
        m = len(forest)
        n = len(forest[0])
        
        # early break: edge case
        if not forest or not forest[0]:
            return -1

        trees = sorted(
            [(i, j, forest[i][j]) for i in range(m) for j in range(n) if forest[i][j] > 1],
            key=lambda x: x[2]
        )

        def is_valid(x, y):
            return 0 <= x < m and 0 <= y < n and forest[x][y] != 0

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(source_x, source_y, dest_x, dest_y):
            """Computes the min no. steps from (sx, sy) -> (dx, dy) if exits"""
            # early exit if the first cell needs cutting down 
            # this occurs if the first cell > 1
            if (source_x, source_y) == (dest_x, dest_y):
                return 0
            seen = set()
            queue = deque()

            # Init
            seen.add((source_x, source_y))
            # (x, y, steps) records
            queue.append((source_x, source_y, 0))

            while queue:
                for _ in range(len(queue)):
                    x, y, steps = queue.popleft()
                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy
                        # break if we find destination
                        if (nx, ny) == (dest_x, dest_y):
                            return steps + 1

                        if is_valid(nx, ny) and (nx, ny) not in seen:
                            queue.append((nx, ny, steps + 1))
                            seen.add((nx, ny))
            return -1

        # start journey
        source_x, source_y = 0, 0
        total = 0

        for dest_x, dest_y, height in trees:
            steps = bfs(source_x, source_y, dest_x, dest_y)
            if steps == -1:
                return -1
            total += steps
            # new source becomes previous destination
            source_x, source_y = dest_x, dest_y
        
        return total

        
