class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict={}
        for i in range (0,len(nums)):
            num_dict[nums[i]]= i
        
        for i in range (0,len(nums)):
            result = target-nums[i]
            if result in num_dict and i!=num_dict[result]:
                return [i,num_dict[result]]
