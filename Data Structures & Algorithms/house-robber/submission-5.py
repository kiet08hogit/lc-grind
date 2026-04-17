class Solution:


   
    def rob(self, nums: List[int]) -> int:
        if (len(nums)) == 1:
                return nums[0]
        def dp_max(nums):
            dp= {}
            for i in range (len(nums)):
                if i ==0 :
                    dp[i]= nums[i]
                elif i == 1:
                    dp[i]= max(nums[i],nums[i-1])
                else:
                    # skip, or take the other house
                    dp[i]= max(dp[i-1],nums[i]+dp[i-2])
            return dp[len(nums)-1]
        return dp_max(nums)