class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        row= len(grid)
        cols= len(grid[0])
        count= 0
        def dfs(r,c):
            direction= [(0,1),(0,-1),(1,0),(-1,0)]
            if r < 0 or c < 0 or r >= row or c >= cols:
                return
            if grid[r][c] != '1':
                return
            grid[r][c]= '0'
            for tr, tc in direction:
                nr = tr+r
                nc =  tc+ c
                dfs(nr,nc)
        
        for r in range(row):
            for c in range(cols):
                if grid[r][c] == '1':
                    count+=1
                    dfs(r,c)
        return count
