class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low1= 0 
        high1 = len(matrix)-1
        chosen_row= -1
        while low1 <= high1:
            mid = (high1 + low1 )// 2
            if matrix[mid][0] <= target:
                chosen_row= mid
                low1=  mid + 1
            else:
                high1= mid - 1
        print(chosen_row)
        low2=0
        high2= len(matrix[0]) -1
        while low2 <= high2:
            mid =  (high2 + low2 )// 2
            if matrix[chosen_row][mid] == target:
                return True
            if  matrix[chosen_row][mid] < target:
                low2= mid + 1
            else:
                high2= mid -1
        return False