class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        def dp_algo (nums):
            if not nums: return 0
            dp= {}
            for i in range(len (nums)):
                if i == 0:
                    dp[0]= nums[0]
                elif i == 1:
                    dp[1]= max(nums[0], nums[1])
                else:
                    dp[i]= max(dp[i-1], nums[i]+dp[i-2])
            return dp[len(nums)-1]
        first= dp_algo(nums[:-1])
        second=dp_algo(nums[1:])
        return max(first,second)