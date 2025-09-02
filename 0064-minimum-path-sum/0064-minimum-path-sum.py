class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row_size = len(grid)
        col_size = len(grid[0])
        def is_valid(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        @cache
        def dp(row, col):
            if row == row_size - 1 and col == col_size - 1:
                # bottom right
                return grid[row][col]
            
            # out of bounds
            if not is_valid(row, col):
                return float('inf')

            
            right = dp(row, col + 1) + grid[row][col]
            down = dp(row + 1, col) + grid[row][col]

            return min(right, down)

        return dp(0, 0)