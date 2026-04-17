class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        row= len(grid)
        cols= len(grid[0])
        answer = grid[0][0]
        max_area= 0
        for r in range(row):

            for c in range(cols):
                self.count= 0


                if grid[r][c] == 1:
                    area = self.dfs(grid, r, c)
                    max_area = max(max_area, area)

        return max_area
    
    def dfs(self,grid,r,c):
        row= len(grid)
        cols= len(grid[0])
        if r < 0 or c <0 or r >=row or c>= cols: 
            return
        if grid[r][c] == 0: 
            return
        self.count+=1
        grid[r][c]= 0
        self.dfs(grid,r,c-1)
        self.dfs(grid,r,c+1)
        self.dfs(grid,r-1,c)
        self.dfs(grid,r+1,c)
        return self.count