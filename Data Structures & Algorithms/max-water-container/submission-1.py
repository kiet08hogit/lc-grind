class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left= 0
        right= len(heights)-1
        maxamount=0
        while left < right:
            width= right - left
            smallernum= min(heights[left],heights[right])
            res= width * smallernum
            maxamount= max(res,maxamount)
            if heights[left] < heights[right]:
                left +=1
            elif heights[right] <= heights[left]:
                right-=1
        return maxamount