class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        temp=[]
        def dfs(res,temp):
            if len(temp) == len(nums):
                res.append(temp.copy())
                temp=[]
                return
            for i in range (len(nums)):
                if nums[i] not in temp:
                    temp.append(nums[i])
                    print(temp)
                    dfs(res,temp)
                    temp.pop()
        dfs(res,temp)
        return res
                 
                