class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        row= len(grid)
        cols= len(grid[0])
        islcount= 0
        for r in range(row):
            for c in range(cols):
                if grid[r][c] == '1':
                    islcount+=1
                    self.dfs(grid,r,c) 
        return islcount
    
    def dfs(self,grid,r,c):
        row= len(grid)
        cols= len(grid[0])
        if r < 0 or c <0 or r >=row or c>= cols: 
            return
        if grid[r][c] == '0': 
            return
        grid[r][c]= '0'
        self.dfs(grid,r,c-1)
        self.dfs(grid,r,c+1)
        self.dfs(grid,r-1,c)
        self.dfs(grid,r+1,c)
        
