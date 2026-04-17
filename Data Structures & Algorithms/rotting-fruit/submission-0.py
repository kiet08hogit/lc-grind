class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows= len(grid)
        cols= len(grid[0])
        directions= [(0,1),(0,-1),(1,0),(-1,0)]
        q= deque()
        bfsres=0
        fresh=0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c]== 1:
                    fresh+=1
        while q and fresh > 0:
            for _ in range(len(q)):
                r,c = q.popleft()
                for dr,dc in directions:
                    nr= dr+r
                    nc= dc+c
                    if nr>=0 and nr < rows and nc >= 0 and nc < cols and grid[nr][nc]==1:
                        grid[nr][nc]= 2
                        fresh-=1
                        q.append((nr,nc))
            bfsres+=1
                
   
        
        return bfsres if fresh == 0 else -1