class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        # for each edge, if it is a border of grid or it is adjacent to water
        # then we will take it into final account perimeter

        def dfs(grid, r, c):
            if not (0 <= r < m and 0 <= c < n):
                return 1

            if grid[r][c] == 0:
                return 1
            
            if grid[r][c] == 2:  # already visited
                return 0
            
            grid[r][c] = 2  # mark visited
            
            # see the four neighbors, sum them up
            return dfs(grid, r-1, c) + dfs(grid, r+1, c) + dfs(grid, r, c-1) + dfs(grid, r, c+1)


        m, n = len(grid), len(grid[0])
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    return dfs(grid, r, c)
