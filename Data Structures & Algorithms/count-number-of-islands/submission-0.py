class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(i, j):
            if i <0 or i>= rows or j <0 or j>= cols:
                return 
            if grid[i][j] == '0' or visited[i][j]:
                return 
            visited[i][j]=True
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
        rows = len(grid)
        cols = len(grid[0])
        visited=[[False]*cols for i in range(rows)]
        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=='1' and not visited[i][j]:
                    count+=1
                    dfs(i,j)
        return count