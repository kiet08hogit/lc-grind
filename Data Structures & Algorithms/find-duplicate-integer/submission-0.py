class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        tempdict= {}
        for i in range (len(nums)):
            tempdict[nums[i]]=tempdict.get(nums[i],0)+1
        for key, val in tempdict.items():
            if(val>1):
                return key
        