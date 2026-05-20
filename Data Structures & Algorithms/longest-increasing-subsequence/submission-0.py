class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = {}
        # dp = [1,1,2,2,3,3,4]
        for i in range (len(nums)):
            dp[i]= 1
            if i == 0:
                continue
            for j in range (i):
                if  nums[i] > nums[j]:
                    dp[i]= max(dp[i],dp[j]+1)
        return max(dp.values())