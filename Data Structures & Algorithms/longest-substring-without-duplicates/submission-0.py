class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        stringdict= {}
        l = 0 
        maxnum=0
        for r in range (len(s)):
            stringdict[s[r]]= 1 + stringdict.get(s[r],0)
            while stringdict[s[r]] > 1:
                stringdict[s[l]]-=1
                l+=1
            maxnum= max(r-l+1,maxnum)
        return maxnum