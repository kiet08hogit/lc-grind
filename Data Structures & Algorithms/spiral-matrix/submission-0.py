class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top = 0 
        bottom= len(matrix)-1
        left= 0
        right= len(matrix[0]) -1
        res= []
        while top <=bottom and left<= right:   
            for cols in range(left,right+1):
                res.append(matrix[top][cols])
            top+=1
            for rows in range (top,bottom+1):
                res.append(matrix[rows][right])
            right-=1
            if top <= bottom:
                for cols in range(right, left - 1, -1):
                    res.append(matrix[bottom][cols])
                bottom -= 1

            if left <= right:
                for rows in range(bottom, top - 1, -1):
                    res.append(matrix[rows][left])
                left += 1
        return res
