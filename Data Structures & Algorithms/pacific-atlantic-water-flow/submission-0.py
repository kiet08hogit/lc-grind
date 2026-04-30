class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows= len(heights)
        cols= len(heights[0])
        def dfs(r,c,visited):
            visited.add((r,c))                
            directions = [(0,1),(0,-1),(1,0),(-1,0)]
            for tr,tc in directions:
                nr = tr + r 
                nc = tc + c
                if nr < 0 or nc < 0 or nr >= rows or nc >= cols:
                    continue
                if (nr,nc) in visited:
                    continue
                if heights[nr][nc] >= heights[r][c]:
                    dfs(nr,nc,visited)
        pacific = set()
        atlantic= set()
        for c in range(cols):
            dfs(0, c, pacific)              # top
            dfs(rows - 1, c, atlantic)      # bottom

        for r in range(rows):
            dfs(r, 0, pacific)              # left
            dfs(r, cols - 1, atlantic)      # right
        res=[]
        print (pacific)
        print (atlantic)

        for r in range(rows):
            for c in range(cols):
                if (r,c) in pacific and (r,c) in atlantic:
                    res.append((r,c))
        return res