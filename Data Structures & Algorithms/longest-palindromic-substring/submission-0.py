class Solution:
    def longestPalindrome(self, s: str) -> str:
        def window(l, r):
            temp=""
            while l>= 0 and r < len(s) and  s[l] == s[r]:
                l-=1
                r+=1
            temp =s[l + 1:r]
            return temp
        res= ""
        odd= ""
        even= ""
        for i in range (len(s)):
            odd= window(i,i)
            even= window(i,i+1)
            if len(odd) > len(res):
                res= odd
            if len(even) > len(res):
                res = even
        return res