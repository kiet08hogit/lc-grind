class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result= []
        for i in range (0,len(nums)):
            total=1
            for j in range (0, len(nums)):
                if j == i:
                    continue

                else:
                    total *= nums[j]
            result.append(total)
        return result       