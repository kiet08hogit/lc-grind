class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left=0 
        right= len(heights)-1
        total=0
        while left < right:
            lowernum= min(heights[left],heights[right])
            width= right - left
            hold= width * lowernum
            total= max(hold,total)
            if heights[left] < heights[right]:
                left+=1
            elif heights[right] <= heights[left]:
                right-=1
           
        return total
