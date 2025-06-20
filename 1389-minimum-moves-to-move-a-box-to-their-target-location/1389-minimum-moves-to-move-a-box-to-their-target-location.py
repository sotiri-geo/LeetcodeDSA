from collections import deque
import heapq
class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        """
        Search state as
        player_row, player_col, box_row, box_col

        We could try to explore movements of the player 
        as the player dictates where the box is.

        Lets first attempt this with a BFS and optimise of A* algo
        """
        target = None
        box = None
        player = None
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "B":
                    box = (i, j)
                if grid[i][j] == "T":
                    target = (i, j)
                if grid[i][j] == "S":
                    player = (i, j)

        def is_valid(x, y):
            return 0 <= x < m and 0 <= y < n and grid[x][y] != "#"

        seen = set([(*player, *box)])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        # (player_row, player_col, box_row, box_col, pushes)
        queue = deque([(*player, *box, 0)])

        def heuristic(a, b):
            # manhattan distance
            return abs(a[0] - b[0]) + abs(a[1] - b[1])

        def can_reach(sx, sy, tx, ty, box_x, box_y):
            """Check if player can reach (tx, ty) without going throught the box
            Use A* algorithm.
            """
            # f = g + h, g, x, y
            heap = [(heuristic((sx, sy), (tx, ty)), 0, sx, sy)]
            visited = set()

            while heap:

                f, g, x, y = heapq.heappop(heap)
                if (x, y) == (tx, ty):
                    return True
                
                if (x, y) in visited:
                    continue
                
                visited.add((x, y))
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    # add extra constraint of box location
                    # as this moves dynamically with each iteration, we pass its location as variable
                    if is_valid(nx, ny) and (nx, ny) != (box_x, box_y):
                        heapq.heappush(heap, (
                            heuristic((nx, ny), (tx, ty)) + g + 1, g + 1, nx, ny
                        ))
            
            return False

        while queue:
            
            p_x, p_y, b_x, b_y, pushes = queue.popleft()

            if (b_x, b_y) == target:
                return pushes

            for dx, dy in directions:
                nb_x, nb_y = b_x + dx, b_y + dy

                # check if we can reach a pushable point
                # dx, dy determines directions
                push_x, push_y = b_x - dx, b_y - dy
                if can_reach(p_x, p_y, push_x, push_y, b_x, b_y):
                    # We can push in that direction. Players next step will take current box
                    # positiion. And box would move in that direction. We only really 
                    # need to check if the boxes next position is valid and if so then the players
                    # next step would automatically be valid as the box was previously there
                    if is_valid(nb_x, nb_y) and (push_x, push_y, nb_x, nb_y) not in seen:
                        queue.append((push_x, push_y, nb_x, nb_y, pushes + 1))
                        seen.add((push_x, push_y, nb_x, nb_y))
        
        return -1

                    

                    
