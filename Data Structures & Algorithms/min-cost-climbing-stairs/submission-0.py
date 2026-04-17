class Solution:


    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def dp_al(cost):
            dp = {}
            for i in range (len(cost)):
                if i <= 1:
                    dp[i]= cost[i]
                else:
                    dp[i]= cost[i] + min(dp[i-1],dp[i-2])
            return min(dp[len(cost)-1], dp[len(cost)-2])
        return dp_al(cost)
      
