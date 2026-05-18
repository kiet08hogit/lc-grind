class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows= len(matrix)
        cols= len(matrix[0])
        ROWS= [False] * rows
        COLS=  [False] * cols
        # ROWS= [False,True,False]
        # COLS= [False,True,False]
        for r in range (rows):
            for c in range (cols):
                if matrix[r][c] == 0:
                    ROWS[r]= True
                    COLS[c]= True

        for r in range(rows):
            for c in range(cols):
                if ROWS[r] or COLS[c]:
                    matrix[r][c] = 0
                    
        #         if status[r][c]:
        #             matrix[r]= [0] * len(matrix[r])
        #             for i in range(rows):
        #                 matrix[i][c] = 0