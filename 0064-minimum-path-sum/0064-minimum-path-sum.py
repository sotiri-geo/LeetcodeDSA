class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # Lets try do a bottom up solution
        # for a given grid[i][j] we could have come from above or to the left
        # then we need to work out the min cost of coming from the left or above
        # we can mutate just the grid because after we've visited (i, j) we can
        # guarentee we've come from a min

        row_size = len(grid)
        col_size = len(grid[0])

        for i in range(row_size):
            for j in range(col_size):
                curr_cost = grid[i][j]
                if i == 0 and j == 0:
                    # base case
                    continue
                above = grid[i - 1][j] if i > 0 else float('inf')
                left = grid[i][j - 1] if j > 0 else float('inf')
                # record the min cost to arrive at this point + cost of point itself
                grid[i][j] = min(above + curr_cost, left + curr_cost)
        
        return grid[row_size - 1][col_size - 1]
