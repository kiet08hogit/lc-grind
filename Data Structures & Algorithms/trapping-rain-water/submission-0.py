class Solution:
    def trap(self, height: List[int]) -> int:
        l= 0 
        r= len(height)-1
        count= 0
        leftbar= height[l]
        rightbar= height[r]
        # move with the side with smaller max wall, that amount of water is already determined
        while l < r:
            if leftbar < rightbar:
                l+=1
                leftbar= max(leftbar, height[l])
                count+= leftbar - height[l]
            else:
                r-=1
                rightbar= max(rightbar, height[r])
                count+= rightbar - height[r]
        return count