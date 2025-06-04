from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        fresh_oranges = 0
        rotten_q = deque()
        time = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    fresh_oranges += 1

                if grid[row][col] == 2:
                    rotten_q.append((row, col, time))
        # edge case if there are no fresh oranges to begin with
        if not fresh_oranges:
            return 0

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        def is_valid(r, c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])

        while rotten_q:

            for _ in range(len(rotten_q)):
                r, c, t = rotten_q.popleft()

                for dx, dy in directions:
                    new_r = r + dx
                    new_c = c + dy
                    # Changing grid value is similar to keeping a seen state
                    # We prevent modifying the same fresh orange more than once
                    if is_valid(new_r, new_c) and grid[new_r][new_c] == 1:
                        # we found a fresh orange that can go rotten in t + 1
                        fresh_oranges -= 1
                        grid[new_r][new_c] = 2
                        # add this to queue
                        rotten_q.append((new_r, new_c, t + 1))
                        if fresh_oranges == 0:
                            return t + 1

        return -1