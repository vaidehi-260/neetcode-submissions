class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = [[False]* cols for i in range(rows)]
        def dfs(i,j):
            if i<0 or i>=rows or j<0 or j>= cols:
                return 0
            if grid[i][j]==0 or visited[i][j]:
                return 0
            visited[i][j]=True
            area = 1 
            area += dfs(i+1, j)
            area += dfs(i-1, j)
            area += dfs(i, j+1)
            area += dfs(i, j-1)
            return area
        max_area = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1 and not visited[i][j]:
                    max_area = max(max_area, dfs(i,j))
        return max_area
