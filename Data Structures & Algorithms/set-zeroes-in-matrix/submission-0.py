class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows= len(matrix)
        cols= len(matrix[0])
        status = [[False] * cols for _ in range(rows)]
        print (len(status))
        for r in range (rows):
            for c in range (cols):
                if matrix[r][c] == 0:
                    status[r][c]= True
        print(status)

        for r in range(rows):
            for c in range(cols):
                if status[r][c]:
                    matrix[r]= [0] * len(matrix[r])
                    for i in range(rows):
                        matrix[i][c] = 0
                    # matrix[r][c]= [0] * len(matrix[r])
                    # zero out row r
                    # zero out col c