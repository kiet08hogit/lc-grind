class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        numslen= len(nums)
        total=nums[0]
        for i in range(numslen):
            currtotal= 0
            for j in range (i,numslen):
                currtotal+=nums[j]
                total= max(currtotal,total)
        return total
            