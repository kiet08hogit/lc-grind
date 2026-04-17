class Solution:
    def isPalindrome(self, s: str) -> bool:
        newstr= ''
        for char in s: 
            if char.isalpha() or char.isdigit():
                newstr+= char.lower()
        
        return  newstr == newstr[::-1]