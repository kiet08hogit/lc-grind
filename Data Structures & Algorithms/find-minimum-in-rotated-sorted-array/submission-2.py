class Solution:
    def findMin(self, nums: List[int]) -> int:
        l =0 
        r = len(nums) -1
        final= nums[0]
        while l <= r:
            if nums[l] < nums[r]:
                final= min(nums[l],final)
                break
            mid = (r+l)//2
            final = min(nums[mid],final)
            if nums[mid] >= nums[l]:
                l = mid+1
            else:
                r = mid-1
        return final