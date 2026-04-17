class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_dict = {}                
        for numbers in nums:
            if numbers in my_dict:
                return True  
            my_dict[numbers] = 1
        return False
            