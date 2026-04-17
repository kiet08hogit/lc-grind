class Solution:
    def search(self, nums: List[int], target: int) -> int:
        min=0
        max= len(nums) - 1
        while max >=min:
            mid= (max + min)//2
            if nums[mid]== target:
                return nums.index(nums[mid])
            if nums[mid]<target:
                min= mid+ 1
            else:
                max= mid-1
        return -1