class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        temp=[]
        def dfs(res,temp):
            if len(temp) == len(nums):
                res.append(temp.copy())
                return
            for i in range (len(nums)):
                if nums[i] not in temp:
                    temp.append(nums[i])
                    dfs(res,temp)
                    temp.pop()
        dfs(res,temp)
        return res
                 
                