class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result= []
        tempsubset=[]
        def dfs(i):
            if i == len(nums):
                result.append(tempsubset.copy())
                return
            tempsubset.append(nums[i])
            dfs(i+1)

            tempsubset.pop()
            dfs(i+1)
        dfs(0)
        return result


       


