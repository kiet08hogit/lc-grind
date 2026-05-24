class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        path=[]

        def isPalindrome(word):
            l= 0
            r= len(word) -1
            while l < r :
                if word[l] != word[r]:
                    return False
                l+=1
                r-=1
            return True

    
        def dfs(curr):
            if curr == len(s):
                res.append(path.copy())
                return
            for i in range (curr, len(s)):
                temp = s[curr:i+1]
                if isPalindrome(temp):
                    path.append(temp)     
                    dfs(i+1)   
                    path.pop()
        dfs(0)
        return res