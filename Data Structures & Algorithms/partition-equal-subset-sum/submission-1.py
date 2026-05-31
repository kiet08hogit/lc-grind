class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        dp={}
        if sum(nums) % 2 != 0:
            return False
        total= sum(nums)
        target= total // 2
        def dfs(index, curr_sum):
            if curr_sum == target:
                return True
            if curr_sum > target:
                return False
            if index == len(nums):
                return False
            if (index,curr_sum) in dp:
                return dp[(index,curr_sum)]
            take_turn= dfs(index+1,curr_sum + nums[index])
            skip_turn= dfs(index+1,curr_sum)
            dp[(index,curr_sum)]= take_turn or skip_turn
            return dp[(index,curr_sum)]
        return dfs(0,0)
