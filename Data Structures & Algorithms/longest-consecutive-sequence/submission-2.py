class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        streak=1
        best=1
        numset= sorted(set(nums))
        for i in range (1,len(numset)):
            if numset[i]== numset[i-1]+1:
                streak+=1
                best = max(streak,best)
            else:
                streak=1
        return best
                