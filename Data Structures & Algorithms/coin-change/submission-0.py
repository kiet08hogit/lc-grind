class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp= [amount + 1] * (amount + 1)
        dp[0]=0
        for i in range (1,amount+1):
            #  i stands for the amount we want and then try to get number of coin for that amount 
            for c in coins:
            #  we need to go through all the coins to find the min amount for a specific amount
                if i - c >=0:
                    dp[i]= min(dp[i],dp[i-c] + 1)
        return dp[amount] if dp[amount] != amount +1 else -1