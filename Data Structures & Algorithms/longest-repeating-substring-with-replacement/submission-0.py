class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        res=0
        tempdict={}
        for r in range (len(s)):
           tempdict[s[r]]= tempdict.get(s[r],0)+1
           while (r-l+1) - max(tempdict.values())>k:
                tempdict[s[l]]-=1
                l+=1
           res= max(res, r-l+1)
        return res
