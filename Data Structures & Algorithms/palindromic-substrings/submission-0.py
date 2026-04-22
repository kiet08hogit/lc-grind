class Solution:
    def countSubstrings(self, s: str) -> int:
        # aaaa
        # aaa

        def window(l, r):
            temp=0 
            while l>= 0 and r < len(s) and  s[l] == s[r]:
                temp +=1
                l-=1
                r+=1
            return temp
        res= 0
        for i in range (len(s)):
            res+= window(i,i)
            res += window(i,i+1)
        
        return res