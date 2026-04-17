class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        tempdict= {}
        for num in nums:
            tempdict[num]= tempdict.get(num,0) +1
        for key, value in tempdict.items():
            if value == 1:
                return key
        return 0
    